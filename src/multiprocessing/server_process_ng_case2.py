"""
マネージャオブジェクトをマルチプロセスで利用する引数に含めることはできない
"""
from multiprocessing import Manager
from concurrent.futures import Future, ProcessPoolExecutor

MAX_WORKERS = 3


def parallel_func(cluster_pool):
    pass


class ClusterPool:
    def __init__(self):
        self.manager = Manager()
        self.clusters = self.manager.list()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.manager.__exit__(exc_type, exc_value, tb)


def main():
    with ClusterPool() as cluster_pool:
        with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future: Future = executor.submit(
                parallel_func,
                cluster_pool=cluster_pool,
            )
            future.result()


if __name__ == "__main__":
    main()
