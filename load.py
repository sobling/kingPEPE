from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# Chrome 드라이버 경로 설정 (사용자가 다운로드한 경로로 수정)
CHROME_DRIVER_PATH = '/path/to/chromedriver'

# 확장 프로그램이 있는 폴더 경로 설정 (압축 해제된 확장 파일 경로)
EXTENSION_PATH = '/path/to/extension'

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # 창을 최대화해서 시작
#chrome_options.add_argument("--disable-extensions")  # 기존 확장 프로그램을 비활성화

# Chrome 드라이버 실행
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# chrome://extensions 페이지 열기
driver.get("chrome://extensions")

# 개발자 모드 활성화
time.sleep(2)  # 페이지 로드 대기
toggle_button = driver.find_element(By.CSS_SELECTOR, 'cr-toggle')
toggle_button.click()

# '압축 해제된 확장 프로그램 로드' 버튼 클릭
time.sleep(2)  # 버튼 로드 대기
load_extension_button = driver.find_element(By.CSS_SELECTOR, 'extensions-manager').shadow_root.find_element(By.CSS_SELECTOR, '#toolbar').shadow_root.find_element(By.CSS_SELECTOR, 'cr-toolbar').shadow_root.find_element(By.CSS_SELECTOR, 'cr-toolbar').shadow_root.find_element(By.CSS_SELECTOR, 'cr-icon-button[title="Load unpacked"]')
load_extension_button.click()

# 확장 프로그램 경로 로드
time.sleep(2)  # 파일 선택 대기
os.system(f'osascript -e \'tell application "System Events" to keystroke "{EXTENSION_PATH}"\'')
time.sleep(1)
os.system('osascript -e \'tell application "System Events" to key code 36\'')  # Enter 키 누름

# 작업 완료 후 드라이버 종료
time.sleep(5)
driver.quit()
