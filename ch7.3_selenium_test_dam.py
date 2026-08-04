# https://www.saucedemo.com/                    로그인 / 상품목록 / 장바구니 테스트
# username  	standard_user
# password  	secret_sauce


# http://uitestingplayground.com                여러 컴포넌트 / 비동기 딜레이

# https://letcode.in/test                       여러 컴포넌트 / 비동기 딜레이


# 다음

# 네이버


# https://www.saucedemo.com/                    로그인 / 상품목록 / 장바구니 테스트
# username  	standard_user
# password  	secret_sauce


# import json
# from selenium import webdriver
# from selenium.common.exceptions import (
#     ElementNotInteractableException,
#     NoSuchElementException,
#     TimeoutException,
# )
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import tempfile

# options = Options()

# options.add_argument("--window-size=1080,720")  # --start
# options.add_argument("--headless")              #GUI 업이 실행
# options.add_argument("--disable-gup")           # headless 상태에서 gpu 충돌방지, headless 에서 필수
# options.add_argument("--no-sandbox")            # root 권한으로 실행하거나 도커의 네임스페이스 제한 환경에서는 크롬이 시작되지 않음.
# options.add_argument("--disable-dev-shm-usage") #도커에서 실행시 공유메모리를 작게 잡는다. 갑자기 종료되는 걸 방지

# 비밀번호 화면으로 인해 브라우저 시스템 팝업 창 문제가 발생
# 매번 임시 프로필을 생성
# profile_dir = tempfile.mkdtemp(prefix="chrome_clean_")
# options.add_argument(f"--user-data-dir={profile_dir}")

# 비밀번호 보안 관련 차단
# options.add_argument("--disable-password-manager")
# options.add_argument("--disable-password-generation")
# options.add_argument("--disable-save-password-bubble")
# options.add_argument("--disalber-notifications")
# options.add_argument("--disable-features=PasswordManager")
# options.add_argument("--disable-features=PasswordImport")


# prefs = {
#     "credentials_enable_service": False,
#     "profile.password_manager_enabled": False,
#     "profile.default_content_setting_values.notifications": 2,
#     "safebrowing.enabled": False,
# }
# options.add_experimental_option("prefs", prefs)
# options.add_argument("--disable-features=PasswordLeakDetection")

# prefs = {
#     "credentials_enable_service": False,
#     "profile.password_manager_enabled": False,
#     "profile.password_manager_leak_detection": False,  # 🔥 [핵심] 유출 탐지 기능을 프로필 단위에서 꺼버립니다.
# }
# options.add_experimental_option("prefs", prefs)

# # 💡 2. 시스템 자격 증명 창 및 암호 저장소 연동 해제
# options.add_argument(
#     "--password-store=basic"
# )  # 🔥 [핵심] 운영체제 및 구글 계정 암호 저장소 연동을 완전히 끊어 팝업을 방지합니다.
# options.add_argument(
#     "--disable-features=PasswordLeakDetection,AutofillServerCommunication"
# )

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
# wait = WebDriverWait(driver, 10)

# try:
#     driver.get("https://www.saucedemo.com/")
#     wait.until(EC.presence_of_all_elements_located((By.ID, "user-name")))
#     wait.until(EC.presence_of_all_elements_located((By.ID, "password")))
#     wait.until(EC.presence_of_all_elements_located((By.ID, "login-button")))

#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     time.sleep(1)
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     time.sleep(1)
#     driver.find_element(By.ID, "login-button").click()

#     wait.until(
#         EC.presence_of_all_elements_located(
#             (By.CLASS_NAME, "inventory_item_description")
#         )
#     )
#     items = driver.find_elements(By.CLASS_NAME, "inventory_item_description")

#     # 자식 노드가 보이지 않을 때, 확인 하는 방법으로 쓴다.
#     # children = cart.find_elements(By.XPATH, "./*")
#     # for child in children:
#     #     print("자식 태그:", child.tag_name)
#     #     print("자식 클래스:", child.get_attribute("class"))
#     #     print("자식 텍스트:", child.text)
#     # print( cart.get_attrivute("outerHTML"))  # 현재 태그 포함 하위 태그 모두

#     # 장바구니 담기 전
#     cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
#     try:
#         before = int(cart.find_element(By.CLASS_NAME, "shopping_cart_badge").text)
#     except:
#         before = 0

#     # 첫번째 제품 장바구니 담기
#     wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
#     items[0].find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

#     # 장바구니 담은 후
#     try:
#         after = int(cart.find_element(By.CLASS_NAME, "shopping_cart_badge").text)
#     except:
#         after = 0

#     # 장바구니 확인
#     assert after == before + 1, print(f"장바구니 담기 실패: 이전 {before} 이후 {after}")
#     print(f"장바구니 담기 성공:{before} => {after}")

#     # 상품 리스트 json 배열로 저장
#     product_list = []
#     print("상품수:", len(items))
#     for item in items:
#         product_name = item.find_element(By.CLASS_NAME, "inventory_item_name")
#         product_price = item.find_element(By.CLASS_NAME, "inventory_item_price")
#         product_detail = (
#             item.find_element(By.TAG_NAME, "a").get_attribute("href").strip()
#         )

#         print("상품명:", product_name.text.strip())
#         print("가격:", product_price.text.strip())

#         product_list.append(
#             {
#                 "product_name": product_name.text.strip(),
#                 "product_price": product_price.text.strip(),
#                 "product_detail": product_detail.strip(),
#             }
#         )
#     with open("src/simple/product.json", "w", encoding="utf-8") as f:
#         json.dump(product_list, f, ensure_ascii=False, indent=4)
#     print("제품목록을 저장했습니다.")

#     time.sleep(10)
# except NoSuchElementException:
#     print("해당 요소가 없습니다.")
# except ElementNotInteractableException:
#     print("해당 요소가 비활성화 돼 있습니다.")
# except TimeoutException:
#     print("대기시간이 종료됐습니다.")
# except Exception as e:  # 나머지 예외는 모두 처리해라. 반드시 맨 아래 적용해야 한다.
#     print(e)
# finally:
#     driver.quit()

# 다음 실시간 뉴스
# https://www.daum.net 실시간 뉴스 크롤링 완벽본
import logging
import logging_config
import time
from selenium import webdriver
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--window-size=1080,720")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--headless")
options.add_argument("--disable-gpu")  # 💡 gup -> gpu 오타 수정
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

logging_config.setup_logger()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.daum.net")

    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "li[data-tid='news-277'] a.link_item")
        )
    )
    articles = driver.find_elements(
        By.CSS_SELECTOR, "li[data-tid='news-277'] a.link_item"
    )
    logging.info(f"기사 수 : {len(articles)}")

    # 💡 [1단계] 메인 페이지에 머무는 동안 "제목"과 "URL 문자열"만 빠르게 수집하기
    news_list = []
    for article in articles:
        try:
            title = article.find_element(
                By.CSS_SELECTOR, "div.wrap_cont strong.tit_item"
            ).text
            url = article.get_attribute("href")
            if url:
                news_list.append({"title": title, "url": url})
        except NoSuchElementException:
            continue

    # 💡 [2단계] 메인 페이지 엘리먼트 참조가 끊겨도 상관없음! 저장된 순수 주소록으로 순회하기
    for news in news_list:
        print(f"<<< {news['title']} >>>")
        print()

        driver.get(news["url"])
        time.sleep(2)  # 상세 페이지 본문이 안정적으로 로딩될 시간 제공

        ps = driver.find_elements(By.CSS_SELECTOR, "section p")
        for p in ps:
            print(p.text.strip())

        print("\n" + "=" * 60 + "\n")  # 기사 간 구분을 위한 분리선

except NoSuchElementException:
    print("해당 요소가 없습니다.")
except ElementNotInteractableException:
    print("해당 요소가 비활성화 돼 있습니다.")
except TimeoutException:
    print("대기시간이 종료됐습니다.")  # 💡 int -> print 오타 수정
except Exception as e:
    print(e)
finally:
    driver.quit()
