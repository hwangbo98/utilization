import csv

# txt 파일 경로와 이름 설정
txt_file = "/home/hwangbo/yolov7/csv_result/1_2weights_5155.txt"

# CSV 파일 경로와 이름 설정
csv_file = "example.csv"

# txt 파일 읽기 모드로 열기
with open(txt_file, "r") as input_file:

    # csv 파일 쓰기 모드로 열기
    with open(csv_file, "w", newline='') as output_file:

        # csv writer 객체 생성
        writer = csv.writer(output_file)

        # 각 줄마다 읽어오기
        for line in input_file:

            # 줄바꿈 문자 제거
            line = line.strip()

            # ',' 문자열 기준으로 나누어서 리스트로 저장
            data = line.split('\t')

            # csv 파일에 데이터 쓰기
            writer.writerow(data)

print("파일 변환 완료!")
