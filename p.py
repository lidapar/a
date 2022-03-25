import asyncio
from pyppeteer import launch
import time

async def main():
    browser = await launch(options={'args': ['--no-sandbox'], 'devtools':True, 'headless':True})
    page = await browser.newPage()
    await page.goto('https://codehs.com/sandbox/id/python-3-3dplai')
    
    for x in range(500):
        try:
            await page.waitForSelector('#panels > div.__abacus_tab-container > div.__abacus_tab-content > div:nth-child(1) > div > div.__abacus_run-bar.__abacus_light-mode > button.StyledButtonKind-sc-1vhfpnt-0.eZfslY.__abacus_button.__abacus_runButton')
            await page.click('#panels > div.__abacus_tab-container > div.__abacus_tab-content > div:nth-child(1) > div > div.__abacus_run-bar.__abacus_light-mode > button.StyledButtonKind-sc-1vhfpnt-0.eZfslY.__abacus_button.__abacus_runButton')
            time.sleep(65)
            # await page.screenshot({'path': "e{x}.png".format(x=x)})
        except:
            # await page.screenshot({'path': "err{x}.png".format(x=x)})
            await page.reload()
            time.sleep(5)
        
    await page.screenshot({'path': 'e.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())