from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

display = Display(visible=0, size=(800, 600))
display.start()
print("Display OK...")

options = webdriver.ChromeOptions()
options.set_headless(headless=True)
options.add_argument('no-sandbox')
options.add_argument('--disable-extensions')
options.add_argument('headless')
options.add_argument('--disable-gpu')
print("Options OK...")

driver = webdriver.Chrome(chrome_options=options)

def getLastPost(URL):
    print("Starting driver...")
    driver.get(URL)
    lastPost = driver.find_element_by_xpath("(//div[@class='Nnq7C weEfm'])[1]//a")
    lastPostURL = lastPost.get_attribute('href')
    print(lastPostURL)
    driver.get(lastPostURL)
    likes = driver.find_element_by_xpath("//span[@class='zV_Nj']//span")
    print("LIKES: "+likes.text)
    postDate = driver.find_element_by_xpath("//time[@class='_1o9PC Nzb55']").get_attribute('dateTime')
    print("POST DATE: "+postDate)

getLastPost("https://www.instagram.com/badunishka/")
getLastPost("https://www.instagram.com/lalamoose/")
