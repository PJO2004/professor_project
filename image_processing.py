import cv2
import numpy as np

class Image_processing:

    # 초기 설정
    def __init__(self, _PATH_ = None):
        self._PATH_ = _PATH_

    # 이미지 처리 과정
    def Image_Slicing(self, B=1000, G=1000, R=1000): # Image change to gray
        print("이미지 처리 중. . . .")
        Img = cv2.imread(self._PATH_)
        self.PImg = np.ones(np.shape(Img))
        self.Gray = []

        for cnt, i in enumerate(Img):
            self.PImg[:,:,0][cnt] = (Img[:,:,0][cnt]/B) # B
            self.PImg[:,:,1][cnt] = (Img[:,:,1][cnt]/G) # G
            self.PImg[:,:,2][cnt] = (Img[:,:,2][cnt]/R) # R
            self.Gray.append((Img[:,:,0][cnt] + Img[:,:,1][cnt] + Img[:,:,2][cnt])/1000)

        self.PImg = np.array(self.PImg)
        self.Gray = np.array(self.Gray)

        print("완료")
        return self.PImg #, self.Gray

    def Image_reverse(self):
        print("이미지 처리 중. . . .")
        self.PImg = cv2.imread(self._PATH_)
        a = f"{np.shape(self.PImg)}"
        x, y = a.split(",")[0][1:], a.split(",")[1]
        for i in range(int(x)):
            for j in range(int(y)):
                reversal_0 = 255 - self.PImg[i][j][0]
                reversal_1 = 255 - self.PImg[i][j][1]
                reversal_2 = 255 - self.PImg[i][j][2]
                self.PImg[i][j] = reversal_0, reversal_1, reversal_2

        print("완료")
        return self.PImg

    # 이미지 출력
    def Image_Show(self, Img=None, Name="defalt"):
        print("이미지 출력 중 . . .")
        self.Img = Img
        self.Name = Name

        cv2.imshow(self.Name, self.Img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 이미지 저장
    def Save_to_Image(self, Filename="Defalt", Img=None):
        self.Filename = Filename + ".jpg"
        cv2.imwrite(self.Filename, Img)
