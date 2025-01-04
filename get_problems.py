from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

# 워크북 링크 목록
links = [
    "https://www.acmicpc.net/workbook/view/9381",
    "https://www.acmicpc.net/workbook/view/9382",
    "https://www.acmicpc.net/workbook/view/9383",
    "https://www.acmicpc.net/workbook/view/9384",
    "https://www.acmicpc.net/workbook/view/9386",
    "https://www.acmicpc.net/workbook/view/9387",
    "https://www.acmicpc.net/workbook/view/9388",
    "https://www.acmicpc.net/workbook/view/9389",
    "https://www.acmicpc.net/workbook/view/9390",
    "https://www.acmicpc.net/workbook/view/9391",
    "https://www.acmicpc.net/workbook/view/9392",
    "https://www.acmicpc.net/workbook/view/9393",
    "https://www.acmicpc.net/workbook/view/9394",
    "https://www.acmicpc.net/workbook/view/9395",
    "https://www.acmicpc.net/workbook/view/9396",
]

# Selenium WebDriver 설정
driver = webdriver.Chrome()  # ChromeDriver 설치 필요

# 로그인 페이지로 이동
driver.get("https://www.acmicpc.net/login")
time.sleep(2)  # 페이지 로드 대기


all_results = []

num = 1
for i, link in enumerate(links):
    print(f"Processing {i+1}/{len(links)}: {link}")
    driver.get(link)

    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    # 페이지 로드 대기
    time.sleep(2)

    # BeautifulSoup으로 페이지 파싱
    soup = BeautifulSoup(driver.page_source, "html.parser")
    rows = soup.select("body > div.wrapper > div.container.content > div.row > div:nth-child(3) > div > table > tbody > tr")

    print(f"rows: {len(rows)}")
    category_title = soup.select_one(
        "body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > blockquote"
    ).text.strip()
    print(f"대분류: {category_title}")

    for row in rows:
        # 문제 번호
        problem_number = row.select_one("td:nth-of-type(1)").text.strip()

        # 제목
        title_tag = row.select_one("td:nth-of-type(2) a")
        title = title_tag.text.strip() if title_tag else "Unknown"
        
        # 문제 링크
        problem_link = title_tag["href"] if title_tag else "#"
        full_link = f"https://www.acmicpc.net{problem_link}"
        
        # 결과 저장
        all_results.append({
            "NUM": num,
            "분류": category_title,
            "문제 번호": problem_number,
            "제목": title,
            "링크": full_link,
        })
        num += 1

driver.quit()  # 브라우저 닫기

import json
print(json.dumps(all_results, indent=4, ensure_ascii=False))


# DataFrame 생성
df = pd.DataFrame(all_results)

# 엑셀로 저장
output_file = "./problems_selenium2.xlsx"
df.to_excel(output_file, index=False)

print(f"엑셀 파일이 생성되었습니다: {output_file}")