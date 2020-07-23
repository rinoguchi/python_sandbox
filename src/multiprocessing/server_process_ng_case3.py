"""
`if __name__ == "__main__":`を指定しないと
"""
from multiprocessing import Manager, Value
from concurrent import futures
from concurrent.futures import Future, ProcessPoolExecutor
from typing import List
import dataclasses

MAX_WORKERS = 3


@dataclasses.dataclass
class SquaredNum:
    num: int
    squared_num: int


def parallel_func(num: int, squared_nums: List[SquaredNum], squared_nums_total: Value):
    squared_num: int = num * num
    squared_nums.append(SquaredNum(num, squared_num))
    squared_nums_total.value += squared_num


nums = [0, 1, 2, 3, 4, 5]

with Manager() as manager:
    squared_nums: List[SquaredNum] = manager.list()
    squared_nums_total: Value = manager.Value('i', 0)
    future_list: List[Future] = []
    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
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
    print(f'squared_nums: {squared_nums}')
    print(f'squared_nums_total: {squared_nums_total.value}')
