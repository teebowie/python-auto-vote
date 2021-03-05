# Made by Teebowie (github.com/teebowie)

# Library import
import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# Constant
VOTESITE = "https://mvhatquocca.truyenhinhthanhnien.com.vn/khoi-5-tieu-hoc-minh-khai-1227-tin237"
VOTESITETITLE = "Khối 5, Tiểu học Minh Khai | 1227"
XPATH_1 = "/html/body/section/div/div/div[1]/div[3]/button[2]"
XPATH_2 = "/html/body/section/div/div/div[1]/div[3]/button[1]"

# Main func
def vote():
	# Open Chrome and connect to vote site
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get(VOTESITE)

	# Verify the website's title, wait an amount of time then click ok when alert is present
	if driver.title == VOTESITETITLE:
		# try:
		# 	WebDriverWait(driver, 25).until(EC.alert_is_present())
		# 	driver.switch_to.alert.accept()
		# 	print('alert accepted')
		# except TimeoutException:
		# 	print('no alert found')
		# 	WebDriverWait(driver, 5).until(EC.alert_is_present())
		# 	driver.switch_to.alert.accept()

		# Locate element, then click vote
		print("Successfully connected to the Website!")
		time.sleep(25)
		html = driver.find_element_by_tag_name('html')
		html.send_keys(Keys.END)

		try:
			voteBtn_1 = driver.find_element_by_xpath(XPATH_1)
			voteBtnText_1 = voteBtn_1.text
			if voteBtnText_1 == "BÌNH CHỌN":
				voteBtn_1.click()
		except NoSuchElementException:
			print('btn 1 not found, trying with btn 2')
			
		try:
			voteBtn_2 = driver.find_element_by_xpath(XPATH_2)
			voteBtnText_2 = voteBtn_2.text
			if voteBtnText_2 == "BÌNH CHỌN":
				voteBtn_2.click()
		except NoSuchElementException:
			print('something went wrong')
	# If title of the page is wrong, kill chrome and run again
	else:
		os.system("taskkill /f /im chrome.exe")
		print('Can not connect to the website! Retrying...')

	print("Vote submitted! Closing...")
	print(x)
	# 3 : so thoi` gian doi sau khi da vote thanh` cong (da binh` chon)
	time.sleep(3)
	driver.quit()

# Vote looping
for x in range(10000):
	print(time.ctime(time.time()))
	vote()
	print("Voted! Waiting a few seconds...")
	time.sleep(15)
	# 15 : so thoi` gian doi sau moi lan` vote 


