# from typing import List
from asyncio import AbstractEventLoop
import asyncio
import datetime


def log(message: str):
    print(f'{datetime.datetime.now()} {message}')


async def cube(number: int) -> int:
    log(f'cube started. number: {number}')
    await asyncio.sleep(5)  # ここで5秒待ちに入った際に、イベントループ内の別のコルーチンが呼び出される
    cubed_number: int = number * number * number
    log(f'cube finished. cubed_number: {cubed_number}')  # このログは5秒ずつ間隔が空くことなく、ほぼ一斉に出力される
    return cubed_number


async def async_main():
    coroutines = []
    for i in range(10):
        coroutines.append(cube(i))
    cubed_numbers = await asyncio.gather(*coroutines)  # ここで複数のコルーチンを同じイベントループの中でまとめて実行
    log(f'cubed_numbers: {cubed_numbers}')


if __name__ == "__main__":
    loop: AbstractEventLoop = asyncio.get_event_loop()
    results = loop.run_until_complete(async_main())
