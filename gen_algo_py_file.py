import os
import pandas as pd

def load_excel_data(file_path):
    """
    엑셀 파일에서 데이터를 읽어와 리스트로 변환
    """
    df = pd.read_excel(file_path)
    result = []

    for i in range(len(df)):
        result.append({
            '번호': f"{int(df['번호'][i]):03d}",  # 번호를 3자리로 0 채움
            '분류': df['분류'][i],
            '문제번호': df['문제번호'][i],
            '문제 제목': df['문제 제목'][i],
            '문제 URL': df['문제 URL'][i],
            '제출 횟수': df['제출 횟수'][i],
            '정답률': df['정답률'][i]
        })
    return result

def generate_problem_files_and_readme(data, base_folder):
    """
    문제 파일 및 README 파일 생성
    """
    # 폴더 생성
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)
    
    readme_lines = [
        "# 알고리즘 문제 목록",
        "| 번호 | 문제번호 | 문제 제목 | 문제 URL | 풀이 링크 | 분류 | 제출 횟수 | 정답률 |",
        "|:----:|:-------:|:---------:|:--------:|:---------:|:----:|:-------:|:-----:|"
    ]

    # 각 문제 파일 생성
    for problem in data:
        file_name = f"{problem['번호']}_{problem['문제번호']}.py"
        file_path = os.path.join(base_folder, file_name)

        # 파일 내용 생성
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"'''\n{problem['문제 URL']}\n제목 : {problem['문제 제목']}\n\n문제)\n-\n\n입력)\n\n출력)\n'''\n")
            f.write("import sys\ninput = sys.stdin.readline\n\n")

        # README.md에 문제 정보 추가
        readme_lines.append(
            f"| {problem['번호']} | {problem['문제번호']} | {problem['문제 제목']} | [문제 링크]({problem['문제 URL']}) | [풀이 보기](./{file_name}) | {problem['분류']} | {problem['제출 횟수']} | {problem['정답률']} |"
        )
    
    # README.md 파일 생성
    readme_path = os.path.join(base_folder, "ALGO_README.md")
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write("\n".join(readme_lines))

if __name__ == "__main__":
    # 엑셀 파일 경로
    excel_file_path = "algo_list.xlsx"  # 여기에 실제 엑셀 파일 경로 입력
    output_folder = "./05_Study/2025"

    # 데이터 로드 및 파일 생성
    problem_data = load_excel_data(excel_file_path)
    generate_problem_files_and_readme(problem_data, output_folder)