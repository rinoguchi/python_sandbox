"""
サーバプロセスで管理するオブジェクトを取得して、
そのインスタンス変数を変更してもサーバプロセス上のオブジェクトには反映されない
"""
from multiprocessing import Manager
from typing import List
import dataclasses

MAX_WORKERS = 3


@dataclasses.dataclass
class Num:
    num: int


def main():
    with Manager() as manager:
        nums: List[Num] = manager.list()
        nums.append(Num(1))
        num_before = nums[0]
        print(f'num_before: {num_before.num}')
        num_before.num = 9
        print(f'num_before: {num_before.num}')
        num_after = nums[0]
        print(f'num_after: {num_after.num}')


if __name__ == "__main__":
    main()
