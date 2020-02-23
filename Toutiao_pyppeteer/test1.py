# -*- coding: utf-8 -*-
# __author__="maple"
"""
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import asyncio
from pyppeteer import launch


async def main(url):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.setViewport(viewport={'width': 1366, 'height': 768})
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3494.0 Safari/537.36')

    # 是否启用js
    await page.setJavaScriptEnabled(enabled=True)

    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate(
        '''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate(
        '''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')

    await page.goto(url,options={'timeout': 5000})

    # await asyncio.sleep(5)
    # 打印页面文本
    return await page.content()

tlist = ["https://www.toutiao.com/a6794863795366789636/",
             "https://www.toutiao.com/a6791790405059871236/",
             "https://www.toutiao.com/a6792756350095983104/",
             "https://www.toutiao.com/a6792852490845946376/",
             "https://www.toutiao.com/a6795883286729064964/",
         ]

task = [main(url) for url in tlist]

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*task))
for res in results:
    print(res)

