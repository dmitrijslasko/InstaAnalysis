from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def getLastPost(URL):
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
