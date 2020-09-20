import time
from typing import Generator


def main():
    gen: Generator[int, None, str] = generate()
    while True:
        try:
            i: int = next(gen)
            print(f'get: {i}')
            time.sleep(1)
        except StopIteration as e:
            print(e.value)
            break


def generate() -> Generator[int, None, str]:
    print('started')
    for i in range(3):
        yield i
    print('finished')
    return 'generator finished !!!!!'


if __name__ == "__main__":
    main()
