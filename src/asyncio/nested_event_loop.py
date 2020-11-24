from pyppeteer.browser import Browser
from pyppeteer.page import Page
from pyppeteer.launcher import launch
from typing import List
import datetime
import requests
from asyncio import AbstractEventLoop
import asyncio
import nest_asyncio
nest_asyncio.apply()


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
    htmls: List[str] = []
    for url in URLS:
        htmls.append(scrape_one_page(url))
    log(f'htmls count: {len(htmls)}')
    log('main finished.')


def scrape_one_page(url: str) -> str:
    """ひとつのページをpyppeteerもしくはrequestsでスクレイピングして、HTMLを返す"""
    if 'qiita' in url:
        # qiitaの場合は、pyppeteerを使って非同期処理でHTMLを取得
        event_loop: AbstractEventLoop = asyncio.get_event_loop()
        return event_loop.run_until_complete(scrape_by_pyppeteer(url))
    else:
        # それ以外は、requestsを使って同期処理でHTMLを取得
        return requests.get(url).text


async def scrape_by_pyppeteer(url: str) -> str:
    """pyppeteerでスクレイピングしてHTMLを返す"""
    try:
        browser: Browser = await launch()
        page: Page = await browser.newPage()
        await page.goto(url)
        html: str = await page.content()
        return html
    finally:
        await page.close()
        await browser.close()


if __name__ == "__main__":
    event_loop: AbstractEventLoop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
