import time
import re
import requests
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "R3CWC0D5LZL"  # 실제 연결된 기기 이름
options.platform_version = "14"
options.app_package = "com.sec.android.app.popupcalculator"  # 삼성 계산기 패키지명
options.app_activity = ".Calculator"  # 계산기 액티비티명
options.automation_name = "UiAutomator2"
options.no_reset = True  # 앱 데이터 초기화 방지

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

time.sleep(2)  # 앱이 완전히 로드될 때까지 대기


# 연산을 수행하는 함수 정의
def calculate(num1, operator, num2):
    """
    숫자 1개, 연산자, 숫자 1개를 입력 후 결과 반환
    """
    # 숫자 여러번 입력할 경우
    for digit in str(num1):
        driver.find_element(AppiumBy.ID, f"com.sec.android.app.popupcalculator:id/calc_keypad_btn_0{digit}").click()

    driver.find_element(AppiumBy.ID, f"com.sec.android.app.popupcalculator:id/calc_keypad_btn_{operator}").click()

    for digit in str(num2):
        driver.find_element(AppiumBy.ID, f"com.sec.android.app.popupcalculator:id/calc_keypad_btn_0{digit}").click()

    driver.find_element(AppiumBy.ID, "com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal").click()

    time.sleep(1)  # 결과가 표시될 시간을 기다림

    result = driver.find_element("id", "com.sec.android.app.popupcalculator:id/calc_edt_formula").text
    result = re.search(r"\d+", result).group()  # 숫자만 추출
    # 결과 출력 후 C로 입력 제거(값 초기화)
    driver.find_element(AppiumBy.ID, "com.sec.android.app.popupcalculator:id/calc_keypad_btn_clear").click()
    return result

# 테스트 케이스 실행
test_cases = [
    (2, "add", 3, "5"),  # 2 + 3 = 5
    (5, "sub", 2, "3"),  # 5 - 2 = 3
    (4, "mul", 3, "12"),  # 4 × 3 = 12
    (8, "div", 2, "4"),  # 8 ÷ 2 = 4
    (5, "div", 0, "Error"),  # 5 ÷ 0 (예외처리)
    (9, "mul", 9999999, "89999991")  # 큰 숫자 입력 테스트
]

for num1, operator, num2, expected in test_cases:
    result = calculate(num1, operator, num2)
    print(f"테스트: {num1} {operator} {num2} = {result} (예상: {expected})")

driver.terminate_app("com.sec.android.app.popupcalculator")

# 앱 종료
driver.quit()