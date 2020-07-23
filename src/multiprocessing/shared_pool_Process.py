from multiprocessing import Value, Array, Process
from typing import List


def parallel_func(number: int, squared_nums: Array, squared_nums_total: Value):
    squared_num: int = number * number
    squared_nums[number] = squared_num
    squared_nums_total.value += squared_num


def main():
    nums: List[int] = [0, 1, 2, 3, 4, 5]
    squared_nums: Array = Array('i', len(nums))
    squared_nums_total: Value = Value('i', 0)

    processes: List[Process] = []
    for num in nums:
        p: Process = Process(target=parallel_func, args=(num, squared_nums, squared_nums_total))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'squared_nums: {squared_nums[:]}')
    print(f'squared_nums_total: {squared_nums_total.value}')


if __name__ == "__main__":
    main()
