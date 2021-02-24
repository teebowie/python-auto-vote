import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

VOTESITE = "https://mvhatquocca.truyenhinhthanhnien.com.vn/khoi-5-tieu-hoc-minh-khai-1227-tin237"
VOTESITETITLE = "Khối 5, Tiểu học Minh Khai | 1227"
DELAYTIME = 5 

def vote():
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get(VOTESITE)

	assert VOTESITETITLE in driver.title
	print("connected to website")

	voteBtn = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[3]/button[1]")
	voteBtn.location_once_scrolled_into_view
	voteBtn.click()

	print("voted")
	time.sleep(DELAYTIME)
	driver.quit()
for x in range(100):
	vote()