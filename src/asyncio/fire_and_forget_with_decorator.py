import datetime
import asyncio
import time


def fire_and_forget(f):
    """対象関数を非同期で投げっぱなしにするためのデコレータ"""
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
    return wrapped


def main():
    log('main started.')
    wait(10)
    log('main finished.')


@fire_and_forget
def wait(second: int):
    """投げっぱなしにしたい処理"""
    log('wait started.')
    time.sleep(second)
    log('wait finished.')


def log(message: str):
    print(f'{datetime.datetime.now()} {message}')


if __name__ == "__main__":
    main()
