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
import pyppeteer

print(pyppeteer.__chromium_revision__)

print(pyppeteer.chromium_downloader.chromiumExecutable.get('win64'))

print(pyppeteer.chromium_downloader.downloadURLs.get('win64'))

def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height

import asyncio
from pyppeteer import launch

async def main():
    # browser = await launch()
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.setViewport(viewport={'width': 1366, 'height': 768})
    # await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3494.0 Safari/537.36')

    await page.goto('https://www.toutiao.com')
    # 是否启用js
    await page.setJavaScriptEnabled(enabled=True)
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate(
        '''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate(
        '''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')


    await page.goto('https://www.toutiao.com/search/?keyword=%E5%B0%8F%E7%B1%B310')

    # 打印cookie页面
    print(await page.cookies())

    await asyncio.sleep(5)

    # # 打印页面文本
    print(await page.content())
    #
    # # 打印当前首页的标题
    print(await page.title())
    with open('toutiao.html', 'w', encoding='utf-8') as f:
        f.write(await page.content())

    await browser.close()

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(main())
loop.run_until_complete(task)
