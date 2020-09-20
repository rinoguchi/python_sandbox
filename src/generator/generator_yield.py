import time
from typing import Generator


def main():
    for i in generate():
        print(f'get: {i}')
        time.sleep(1)


def generate() -> Generator[int, None, None]:
    print('started')
    for i in range(3):
        yield i
        print(f'yielded: {i}')
    print('finished')


if __name__ == "__main__":
    main()
