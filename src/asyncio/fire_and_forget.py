import datetime
import asyncio
import time


def main():
    log('main started.')
    asyncio.get_event_loop().run_in_executor(None, wait, 10)
    log('main finished.')


def wait(second: int):
    """投げっぱなしにしたい処理"""
    log('wait started.')
    time.sleep(second)
    log('wait finished.')


def log(message: str):
    print(f'{datetime.datetime.now()} {message}')


if __name__ == "__main__":
    main()
