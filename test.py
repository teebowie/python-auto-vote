import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

VOTESITE = "https://mvhatquocca.truyenhinhthanhnien.com.vn/khoi-5-tieu-hoc-minh-khai-1227-tin237"
VOTESITETITLE = "Khối 5, Tiểu học Minh Khai | 1227"
DELAYTIME = 5 

def vote():
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get(VOTESITE)

	if driver.title == VOTESITETITLE:
		print("Successfully connected to the Website!")

		voteBtn = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[3]/button[1]")
		voteBtn.location_once_scrolled_into_view
		voteBtn.click()

		print("Vote submitted! Closing...")
		time.sleep(DELAYTIME)
		driver.quit()

	else:
		print("Something went wrong! Retrying...")
		os.system("taskkill /f /im chrome.exe")

for x in range(10000):
	vote()