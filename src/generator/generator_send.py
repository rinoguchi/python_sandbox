import time
from typing import Generator, Optional


def main():
    gen: Generator = generate()
    print('get generator')

    try:
        # nextした場合の挙動を確認
        i: int = 0
        for _ in range(3):
            i = next(gen)
            time.sleep(1)
            print(f'get value: {i}')

        # 次にsendした場合の挙動を確認
        for _ in range(3):
            i = gen.send(i * i)
            time.sleep(1)
            print(f'send value: {i * i}')
    except StopIteration:
        print('generator stopped')


def generate() -> Generator[int, int, None]:
    print('started')
    i: int = 1
    while True:
        r: Optional[str] = (yield i)
        print(f'recieved value: {r}')  # 受け取った値を確認
        if r is not None:
            i = i + r  # Noneじゃなければiに受け取った値を加算
        if i > 10:  # 10を超えたらloop終了
            break
    print('finished')


if __name__ == "__main__":
    main()
