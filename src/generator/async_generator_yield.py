
import asyncio
from typing import AsyncGenerator


async def main():
    # async for i in async_generate():
    #     print(f'get: {i}')
    #     await asyncio.sleep(1)

    gen: AsyncGenerator[int, None] = async_generate()
    while True:
        try:
            i: int = await gen.__anext__()
            print(f'get: {i}')
        except StopAsyncIteration:
            break


async def async_generate() -> AsyncGenerator[int, None]:
    print('started')
    for i in range(3):
        yield i
        await asyncio.sleep(1)
        print(f'yielded: {i}')
    print('finished')


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(
        main()
    )
