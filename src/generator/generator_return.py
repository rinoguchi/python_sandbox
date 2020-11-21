import time
from typing import Generator


def main():
    gen: Generator[int, None, str] = generate()
    i: int = 0
    while True:
        try:
            print(f'before next. i: {i}')
            i: int = next(gen)
            print(f'after next. i: {i}')
            time.sleep(1)
        except StopIteration as e:
            print(f'StopIteration raised. return_value: {e.value}')
            break


def generate() -> Generator[int, None, str]:
    print('generate started.')
    for i in range(3):
        yield i
    print('generate finished.')
    return '##return_value##'


if __name__ == "__main__":
    main()
