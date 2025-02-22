import time
import re
import requests
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "R3CWC0D5LZL"  # 실제 연결된 기기 이름
options.app_package = "com.sec.android.app.popupcalculator"  # 삼성 계산기 패키지명
options.app_activity = ".Calculator"  # 계산기 액티비티명
options.automation_name = "UiAutomator2"
options.no_reset = True  # 앱 데이터 초기화 방지

driver = webdriver.Remote("http://localhost:4723", options=options)

# 확인된 UI 요소 ID로 변경 (수정 필수)
el1 = driver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_02")  # 숫자 2 버튼
el1.click()

el2 = driver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_add")  # 더하기 버튼
el2.click()

el3 = driver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_03")  # 숫자 3 버튼
el3.click()

el4 = driver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal")  # = 버튼
el4.click()

time.sleep(1)

result = driver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_edt_formula").text
# 정규식 (Regex) 활용
result = re.search(r"\d+", result).group() # 숫자만 추출
print(f"계산기 결과 : {result}")

driver.terminate_app("com.sec.android.app.popupcalculator")

# Appium 종료
driver.quit()

# API 요청을 보내서 결과 확인
api_url = "https://api.mathjs.org/v4/"
data = {"expr": "2+3"}
response = requests.post(api_url, json=data)
api_result = response.json()["result"]

print(f"API 계산 결과: {api_result}")

# 검증 (계산기 결과와 API 결과 비교)
assert result == api_result, "❌계산 결과가 일치하지 않습니다!"
print("✅계산 검증 완료 !")