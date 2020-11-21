import time
from typing import Generator


def main():
    for i in generate():
        print(f'get. i: {i}')
        time.sleep(1)


def generate() -> Generator[int, None, None]:
    print('generate started.')
    for i in range(3):
        print(f'before yield. i: {i}')
        yield i
        print(f'after yield. i: {i}')
    print('generate finished.')


if __name__ == "__main__":
    main()
