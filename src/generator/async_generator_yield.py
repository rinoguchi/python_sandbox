
import asyncio
from typing import AsyncGenerator


async def main():
    print('====== async forの例 ======')
    async for i in async_generate():
        print(f'started loop. i: {i}')
        await asyncio.sleep(1)

    print('====== generatorを取得してwhileで回す例 ======')
    gen: AsyncGenerator[int, None] = async_generate()
    i: int = 0
    while True:
        try:
            print(f'before anext. i: {i}')
            i = await gen.__anext__()
            print(f'after anext. i: {i}')
        except StopAsyncIteration:
            break


async def async_generate() -> AsyncGenerator[int, None]:
    print('async_generate started.')
    for i in range(3):
        print(f'before yield. i: {i}')
        yield i
        print(f'after yield. i: {i}')
        await asyncio.sleep(1)
    print('async_generate finished.')


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(
        main()
    )
