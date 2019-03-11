# NOTES: In order to use this script properly, you need to download Selenium API and the specific driver 
#       for your browser: In this case I'm using Chrome Driver. 
# LINKS: 
#           - http://chromedriver.chromium.org/downloads
#           - https://www.seleniumhq.org/


from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time 

#Getting the Options from chrome
options = Options()
options.add_argument("user-data-dir=C:\\Users\\javif\\ChromeProfiles\\BotUser\\User Data")


# I had a problem setting the path of the chromedriver, so instead of that
# the script downloads it every time you want to send a message.
# TODO: Set a right path to avoid the download part.
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

# Set the website, in this case is web.whatsapp.com
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group
# TODO: Set this within the arguments on the script. 
target = '"Sami LS"'

# Replace the below string with your own message
# TODO: Set this within the arguments on the script.
string = " exams "

# Looking for the contact (this might take a while)
# TODO: Find a way to scroll down if the contact isn't visible.
x_arg = '//span[contains(@title,' + target + ')]'
group_title = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click() 

# Typing the message and sending it. 
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'    #'//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = WebDriverWait(driver,150).until(EC.presence_of_element_located(( 
	By.XPATH, inp_xpath))) 

for i in range(10):
    input_box.send_keys(string + Keys.ENTER)




