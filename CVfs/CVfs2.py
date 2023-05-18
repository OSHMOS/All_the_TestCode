from PIL import Image

# gif 파일 경로 및 파일명
filename = "/Users/seunghyunoh/desktop/All_the_TestCode/CVfs/hit2.gif"

# 저장할 경로 설정
path = ""

try:
    # gif 파일 오픈
    with Image.open(filename) as im:
        # gif 파일의 각 프레임 수 추출
        frame_cnt = im.n_frames
        pre_frame = None

        # 등분된 프레임 수 설정
        split_frame = 120

        # 분할된 초 단위 시간 간격 계산
        interval = im.info['duration'] / 1000.0 / split_frame

        for i in range(split_frame):
            # 이미지 파일로 저장할 이름 생성
            img_filename = path + \
                filename.split('.gif')[0] + '_' + str(i) + '.png'

            # 초 단위 프레임 위치 계산
            frame_time_sec = i * interval
            im.seek(int(frame_time_sec * frame_cnt / split_frame))
            # 현재 위치의 이미지 저장
            curr_frame = im.copy().convert('RGBA')
            curr_frame.save(img_filename)

        # 이미지 파일 닫기
        im.close()

except Exception as e:
    print("An error occurred: ", e)
