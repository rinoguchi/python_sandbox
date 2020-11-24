from pyppeteer.browser import Browser
from pyppeteer.page import Page
from pyppeteer.launcher import launch
from typing import List
import datetime
from asyncio import AbstractEventLoop
import asyncio

URLS: List[str] = [
    'https://qiita.com/search?q=1',
    'https://qiita.com/search?q=2',
    'https://www.google.com/search?q=1',
    'https://www.google.com/search?q=2',
    'https://search.yahoo.co.jp/search?p=1',
    'https://search.yahoo.co.jp/search?p=2',
]


def log(message: str):
    print(f'{datetime.datetime.now()} {message}')


async def main():
    log('main started.')
    browser: Browser = await launch()
    try:
        htmls: List[str] = []
        for url in URLS:
            html: str = await scrape_one_page(browser, url)
            htmls.append(html)
    finally:
        await browser.close()
    log(f'htmls count: {len(htmls)}')
    log('main finished.')


async def scrape_one_page(browser: Browser, url: str) -> str:
    """ひとつのページをスクレイピングして、HTMLを返す"""
    log(f'scrape_one_page started. url: {url}')
    log(f'task count: {len(asyncio.all_tasks())}')
    page: Page = await browser.newPage()
    try:
        await page.goto(url)
        html: str = await page.content()
        return html
    finally:
        await page.close()
        log(f'scrape_one_page finished. url: {url}')


if __name__ == "__main__":
    event_loop: AbstractEventLoop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
