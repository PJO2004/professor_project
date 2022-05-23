from video_to_slicing import Video_To_Image
import os
from Gui_screen import Image_PR_GUI

Video_File = "opencv_Sample_Data.mp4"

if __name__ == "__main__":
    try:
        if not os.path.exists('data'):
            if not os.path.exists(f"./data/{Video_File.split('.')[0]}"):  # 파일 유무 확인
                CTest = Video_To_Image(VideoFile=Video_File, PATH="./Video")  # 비디오 처리 모듈에 MP4파일 넣음
                CTest.Running()
    except:
        pass

PR = Image_PR_GUI()
# 이미지 라벨 생성
img = PR.change_image()
PR.create_label(img)

PR.RGB_Wiget()
# 버튼 생성
PR.create_button("다음 사진", PR.change_img)
PR.create_button("이전 사진", PR.change_back_img)
PR.create_button("반전", PR.reverse_Button)

PR.Sw()