from PIL import Image

# gif 파일 경로 및 파일명
filename = "/Users/seunghyunoh/desktop/All_the_TestCode/CVfs/hit2.gif"

# 저장할 경로 설정
path = ""

# gif 파일 오픈
with Image.open(filename) as im:
    # gif 파일의 각 프레임 수 추출
    frame_cnt = im.n_frames
    pre_frame = None

    # 등분된 프레임 수 설정
    split_frame = 120

    # 프레임당 등분 간격 계산
    interval = frame_cnt // split_frame

    for i in range(split_frame):
        # 이미지 파일로 저장할 이름 생성
        img_filename = path + filename.split('.gif')[0] + '_' + str(i) + '.png'

        # 현재 불러온 프레임의 위치가 저장할 프레임 위치와 일치하면 해당 프레임을 이미지 파일로 저장
        frame_idx = i * interval
        im.seek(frame_idx)
        curr_frame = im.copy().convert('RGBA')
        curr_frame.save(img_filename)

# 이미지 파일 닫기
im.close()
