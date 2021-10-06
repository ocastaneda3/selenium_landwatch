import sys
import time
import re

# https://levelup.gitconnected.com/8-tips-to-master-web-control-with-selenium-ab120004753a

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import lxml
import json

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
WINDOW_SIZE = '1920,1080'

# Listings
# class="d99b8"
LISTING = "d99b8"
# Image
# class="_651f4"
IMAGE = "_651f4"
# Text Data
# class="_78864"
TEXT = "_78864"
# Navivation
# class="_3e4ea"
NEXT = "_3e4ea"

def main():
    try:
        options = Options()
        options.add_argument( '--headless') 
        options.add_argument( '--window-size=%s' % WINDOW_SIZE )
        options.add_argument( '--no-sandbox' )

        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

        # Establish Driver
        driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH, options=options )
        # Delete Cookies
        driver.delete_all_cookies()
        # Pause
        driver.implicitly_wait(10)
        # Get Page
        driver.get('https://www.landwatch.com/land')

        number_of_pages = int( driver.find_elements_by_class_name( 'd41b7' )[-1].text )

        for index in range( number_of_pages - 1):
            _listings = driver.find_elements_by_class_name(LISTING)

            for land in _listings :
                _data = {}

                _text = land.find_element_by_class_name(TEXT).find_elements_by_tag_name('div')[:2]
                _city, _state, _county = re.search(r'(.+?), +(.+?) \(+(.+?)\)', _text[-1].text.split( ' - ' )[-1]).groups()

                _data['price'] = _text[0].text
                _data['size'] = _text[-1].text.split( ' - ' )[0]
                _data['city'] = _city
                _data['state'] = _state
                _data['county'] = _county

                print( json.dumps( _data, indent=4), '\n' )
            
            # time.sleep( 10 )
            # driver.find_elements_by_class_name(NEXT)[-1].click()
            # time.sleep( 10 )

            if index == 0:
                break
    except Exception as e:
        print( e )
    finally:
        driver.close()

if __name__ == '__main__':
    sys.exit( main() )


# Next
# class="_3e4ea"

# End of List
# class="ca906"