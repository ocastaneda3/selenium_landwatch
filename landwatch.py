import sys

# https://levelup.gitconnected.com/8-tips-to-master-web-control-with-selenium-ab120004753a

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import lxml

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
WINDOW_SIZE = '1920,1080'

# Listings
# class="d99b8"

# Text Data
# class="_78864"

# Navivation
# class="_3e4ea"

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
        # Get
        driver.get('https://www.landwatch.com/land')

        _listings = driver.find_elements_by_class_name('d99b8')

        for index, x in enumerate( _listings):
            _data = x.find_element_by_class_name('_78864').find_elements_by_tag_name('div')[:2]
            for y in _data:
                print( y.text )
            if index == 0:
                break

    except Exception as e:
        print( e )
    finally:
        driver.close()

if __name__ == '__main__':
    sys.exit( main() )