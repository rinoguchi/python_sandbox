"""
サーバプロセス × ProcessPoolExecutor

独自クラス内でマネージャーオプジェクトを管理するケースを試してみる
"""
from multiprocessing import Manager
from multiprocessing.managers import SyncManager
from concurrent import futures
from concurrent.futures import Future, ProcessPoolExecutor
from threading import Lock
from typing import List
import time
import os
import random
import string

MAX_WORKERS = 3


class Cluster:
    def __init__(self):
        self.name: str = ''.join(random.choices(string.ascii_lowercase, k=5))
        self.is_using: bool = True

    def __eq__(self, other):
        return self.name == other.name

    def submit_pyspark_job(self, num: int):
        squared_num: int = num * num
        time.sleep(1)  # 本当はここでPySparkのジョブを実行する
        print(f'job finished. num: {num}, squared_num: {squared_num}, pid: {os.getpid()}, cluster_name: {self.name}')
        return num * num  # サンプルなので、numの二乗を返しておく


class ClusterPool:
    def __init__(self, manager: SyncManager):
        self.clusters: List[Cluster] = manager.list()  # インスタンス変数にサーバプロセスで管理するListを保持
        self.lock: Lock = manager.Lock()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.clusters[:] = []  # withブロックを抜ける時にサーバプロセスのListを空に

    def get_or_create_cluster(self) -> Cluster:
        self.lock.acquire(blocking=True)
        try:
            for i, existing_cluster in enumerate(self.clusters):
                if not existing_cluster.is_using:
                    existing_cluster.is_using = True
                    self.clusters[i] = existing_cluster
                    return existing_cluster
            else:
                new_cluster: Cluster = Cluster()
                self.clusters.append(new_cluster)
                return new_cluster
        finally:
            self.lock.release()

    def release_cluster(self, cluster: Cluster):
        cluster.is_using = False
        self.clusters[self.clusters.index(cluster)] = cluster


def parallel_func(num: int, cluster_pool: ClusterPool) -> int:
    cluster: Cluster = cluster_pool.get_or_create_cluster()
    result: int = cluster.submit_pyspark_job(num)
    cluster_pool.release_cluster(cluster)
    return result


def main():
    nums: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    with Manager() as manager:
        with ClusterPool(manager) as cluster_pool:
            future_list: List[Future] = []
            squared_nums: List[int] = []
            with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
                for num in nums:
                    future: Future = executor.submit(
                        parallel_func,
                        num=num,
                        cluster_pool=cluster_pool,
                    )
                    future_list.append(future)
                for future in futures.as_completed(fs=future_list):
                    squared_nums.append(future.result())

        print(f'squared_nums: {squared_nums}')


if __name__ == "__main__":
    main()
