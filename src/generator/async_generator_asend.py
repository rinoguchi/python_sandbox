
import asyncio
from typing import AsyncGenerator
from random import randint


async def main():
    gen: AsyncGenerator[int, None] = async_generate()
    i: int = 0
    while True:
        try:
            print(f'before anext. i: {i}')
            i = await gen.__anext__()
            print(f'after anext. i: {i}')
            send_value: int = randint(1, 10)
            print(f'before anext. i: {i}, send_value: {send_value}')
            await gen.asend(send_value)
            print(f'after anext. i: {i}, send_value: {send_value}')
        except StopAsyncIteration:
            break


async def async_generate() -> AsyncGenerator[int, None]:
    print('async_generate started.')
    for i in range(10):
        print(f'before yield. i: {i}')
        received_value: int = (yield i)
        print(f'after yield. i: {i}, received_value: {received_value}')
        if received_value is not None and received_value > 5:
            print('finish async_generate because received_value > 0.')
            break  # 受け取った値が5より大きかったら終了する
        await asyncio.sleep(1)
    print('async_generate finished.')


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(
        main()
    )
