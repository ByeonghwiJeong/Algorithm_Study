import pandas as pd
from notion_client import Client
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# 노션 API 설정
NOTION_KEY = os.getenv('NOTION_KEY')
NOTION_DATABASE_ID_1 = os.getenv('NOTION_DATABASE_ID_1')
notion = Client(auth=NOTION_KEY)
database_id = NOTION_DATABASE_ID_1

def load_excel_data(file_path):
    """
    엑셀 파일에서 데이터를 읽어와 리스트로 변환
    """
    df = pd.read_excel(file_path)
    result = []

    for i in range(len(df)):
        result.append({
            '번호': df['번호'][i].item(),
            '분류': df['분류'][i],
            '문제번호': df['문제번호'][i].item(),
            '문제 제목': df['문제 제목'][i],
            '문제 URL': df['문제 URL'][i],
            '제출 횟수': df['제출 횟수'][i].item(),
            '정답률': df['정답률'][i].item()
        })
    return result

def fetch_all_pages(database_id):
    """
    노션 데이터베이스에서 모든 데이터를 가져오기
    """
    all_results = []
    next_cursor = None

    while True:
        # API 호출
        response = notion.databases.query(
            database_id=database_id,
            start_cursor=next_cursor,
            page_size=100  # 최대 100개
        )

        # 결과 저장
        all_results.extend(response.get('results', []))

        # 다음 페이지가 없으면 종료
        next_cursor = response.get('next_cursor')
        if not next_cursor:
            break

    return all_results

def get_existing_problem_numbers(read_results):
    """
    기존 데이터에서 '문제번호' 추출
    """
    return [
        result['properties']['문제번호']['number']
        for result in read_results
        if '문제번호' in result['properties'] and 'number' in result['properties']['문제번호']
    ]

def add_to_notion(database_id, new_data, existing_nums):
    """
    새 데이터를 노션 데이터베이스에 추가
    """
    num = 1
    for row in new_data:
        # 진행 상황 표시
        print(f'{num / len(new_data) * 100:.2f}% 진행중...')
        num += 1

        # 중복 데이터 확인
        if row['문제번호'] in existing_nums:
            continue

        # 데이터 추가
        notion.pages.create(
            parent={'database_id': database_id},
            properties={
                'NO': {'number': row['번호']},
                '분류': {'rich_text': [{'text': {'content': row['분류']}}]},
                '문제번호': {'number': row['문제번호']},
                '제목': {'title': [{'text': {'content': row['문제 제목']}}]},
                'URL': {'url': row['문제 URL']},
                '제출횟수': {'number': row['제출 횟수']},
                '정답률': {'number': row['정답률']}
            }
        )

def main():
    # 1. 엑셀 데이터 로드
    print("엑셀 데이터를 로드합니다...")
    new_data = load_excel_data('algo_list.xlsx')
    print(f"로드된 데이터 수: {len(new_data)}")

    # 2. 기존 노션 데이터 가져오기
    print("노션 데이터베이스에서 기존 데이터를 가져옵니다...")
    read_results = fetch_all_pages(database_id)
    existing_nums = get_existing_problem_numbers(read_results)
    print(f"기존 데이터 수: {len(existing_nums)}")

    # 3. 새 데이터 추가
    print("새 데이터를 추가합니다...")
    # add_to_notion(database_id, new_data, existing_nums)
    print("완료!")

# 실행
if __name__ == "__main__":
    main()