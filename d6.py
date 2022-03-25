import asyncio
from pyppeteer import launch
import time

async def main():
    browser = await launch(options={'args': ['--no-sandbox'], 'devtools':True, 'headless':True})
    page = await browser.newPage()
    await page.goto('https://codehs.com/sandbox/id/python-3-rXxIho')
  
    for x in range(3000):
        try:
            time.sleep(10)
            await page.mouse.click(580,125,{'button': 'left'})
            await page.screenshot({'path': "d6.png"})
        except:
            # await page.screenshot({'path': "fail/err{x}.png".format(x=x)})
            await browser.close()
            # time.sleep(5)
        
    # await page.screenshot({'path': 'e.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
