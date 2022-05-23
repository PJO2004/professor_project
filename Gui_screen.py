#Import the required library
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import image_processing as IP
import cv2

class Image_PR_GUI:

    resolution = (640, 400)
    # resolution = (480, 852)
    count = 0
    window = Tk()
    window.geometry("640x600+100+100")
    window.title("이미지 처리 프로그램")

    def change_image(self):
        img = cv2.imread(f"data/opencv_Sample_Data/{self.count}.jpg")
        img = cv2.resize(img, self.resolution)
        img = Image.fromarray(img)
        return ImageTk.PhotoImage(image=img)

    def image_pr(self):
        IPC = IP.Image_processing(f"./data/opencv_Sample_Data/{self.count}.jpg")
        print(type(self.R.get()))
        PImg = IPC.Image_Slicing(R=self.R.get(), G=self.G.get(), B=self.B.get())
        cv2.imwrite("GUI_show_Image.jpg", PImg)

    def create_label(self, img):
        self.label = Label(self.window, image=img)
        self.label.pack()

    # 이미지 변경 설정
    def reverse_Image(self):
        IPC = IP.Image_processing("GUI_show_Image.jpg")
        PImg = IPC.Image_reverse()
        cv2.imwrite("GUI_show_Image.jpg", PImg)

    def change_img(self):
        self.next_image()
        img = self.change_image()
        self.label.configure(image=img)
        self.label.image = img

    def change_back_img(self):
        self.back_image()
        img = self.change_image()
        self.label.configure(image=img)
        self.label.image = img

    # 이미지 번호 설정
    def next_image(self):
        self.count += 1

    def back_image(self):
        if self.count < 0:
            self.count += 1
        else:
            self.count -= 1

    def create_button(self, text, image):
        V = Button(self.window, text=text, font=('Helvetica 13 bold'), command=image)
        V.pack()

    # 윈도우 창 띄우기
    def Sw(self):
        self.window.mainloop()

    def reverse_Button(self):
        self.reverse_Image()
        img = cv2.imread("GUI_show_Image.jpg")
        img = cv2.resize(img, self.resolution)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)
        self.label.configure(image=img)
        self.label.image = img

    # 버튼 이벤트 함수
    def click_me(self):
        print(f"R: {self.R.get()} G: {self.G.get()} B: {self.B.get()}")
        self.image_pr()
        img = cv2.imread("GUI_show_Image.jpg")
        img = cv2.resize(img, self.resolution)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)
        self.label.configure(image=img)
        self.label.image = img

    def pack(self, variable):
        ttk.Entry(self.window, width=12, textvariable=variable).pack()

    def Integer(self):
        return tk.IntVar()

    def RGB_Wiget(self):
        self.R = self.Integer()
        self.pack(self.R)
        self.G = self.Integer()
        self.pack(self.G)
        self.B = self.Integer()
        self.pack(self.B)

        self.create_button("이미지 변환", self.click_me)