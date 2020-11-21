import time
from typing import Generator, Optional
from random import randint


def main():
    gen: Generator = generate()  # Generatorオブジェクト生成
    i: int = 0
    while True:
        try:
            print(f'before next. i: {i}')
            i = next(gen)
            print(f'after next. i: {i}')
            time.sleep(1)
            send_value: int = randint(1, 10)  # 1〜10のランダムな整数を取得
            print(f'before send. i: {i}, send_value: {send_value}')
            gen.send(send_value)
            print(f'after send. i: {i}, send_value: {send_value}')

        except StopIteration:
            print('StopIteration raised.')
            break


def generate() -> Generator[int, int, None]:
    print('generate started')
    i: int = 1
    while True:
        print(f'before yield. i: {i}')
        received_value: Optional[str] = (yield i)  # next()でもsend()でもここに来る。next()だとreceived_valueはNone
        print(f'after yield. i: {i}, received_value: {received_value}')
        if received_value is not None:
            i = i + received_value  # Noneじゃなければiに受け取った値を加算
        if i > 10:  # 10を超えたらloop終了
            break
    print('generate finished')


if __name__ == "__main__":
    main()
