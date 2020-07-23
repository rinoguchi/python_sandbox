"""
共有メモリ × ProcessPoolExecutor

RuntimeError: SynchronizedArray objects should only be shared between processes through inheritance
が発生するので使えない
"""
from multiprocessing import Value, Array
from concurrent import futures
from concurrent.futures import Future
from typing import List

MAX_WORKERS = 3


def parallel_func(num: int, squared_nums: Array, squared_nums_total: Value):
    squared_num: int = num * num
    squared_nums[num] = squared_num
    squared_nums_total.value += squared_num


def main():
    nums = [0, 1, 2, 3, 4, 5]
    squared_nums: Array = Array('i', len(nums))
    squared_nums_total: Value = Value('i', 0)

    future_list: List[Future] = []
    with futures.ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for num in nums:
            future: Future = executor.submit(
                parallel_func,
                num=num,
                squared_nums=squared_nums,
                squared_nums_total=squared_nums_total,
            )
            future_list.append(future)
        for future in futures.as_completed(fs=future_list):
            future.result()

    print(f'squared_nums: {squared_nums[:]}')
    print(f'squared_nums_total: {squared_nums_total.value}')


if __name__ == "__main__":
    main()
