# 비디오 프레임 모듈
import cv2
import os

class Video_To_Image:

    def __init__(self, VideoFile=None, PATH=None):  # 시작 변수
        self.VideoFile = VideoFile
        self.PATH = PATH
        self.Image_Folder = None
        self.cam = None  # 카메라 data
        self.currentframe = None  # 프레임 임의 이름 태그

    def Bool_DTest(self):  # 파일 존재 유무 테스트
        print("파일 테스트")
        Img_Name = self.VideoFile.split('.')[0]
        try:
            if not os.path.exists('data'):
                os.makedirs('data')
            try:
                if not os.path.exists(f'./data/{Img_Name}'):
                    os.makedirs(f'./data/{Img_Name}')

            # 에러 처리
            except OSError:
                raise OSError('Error: Please Creating directory of Image_Folder')
        except OSError:
            raise OSError('Error: Please Creating directory of data')
        print("완료")

    def Frame_slicing_Run(self):
        print("비디오 처리 중 . . .")
        if self.PATH == None:
            self.cam = cv2.VideoCapture(self.VideoFile)
        else:
            self.cam = cv2.VideoCapture(f"{self.PATH}/{self.VideoFile}")
        self.currentframe = 0

        self.Frame_Slicing(self.currentframe)  # 프레임 생성 메서드
        self.cam.release()
        print("완료")

        cv2.destroyAllWindows()  # window에 보여주기


    def Frame_Slicing(self, currentframe=None):
        ret, frame = self.cam.read()
        Img_Name = self.VideoFile.split('.')[0]

        if ret:
            name = f'./data/{Img_Name}/' + str(currentframe) + '.jpg'
            print(f'Creating... {name}')  # 이미지 저장 경로 설정

            cv2.imwrite(name, frame)  # 이미지 저장
            self.currentframe += 1

            return self.Frame_Slicing(currentframe=self.currentframe)


    def Running(self):  # 실제 실행 메서드
        self.Bool_DTest()
        self.Frame_slicing_Run()