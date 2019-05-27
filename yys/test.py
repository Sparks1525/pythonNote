# coding=utf-8
import cv2
from PIL import ImageGrab

box = 100, 200, 300, 400
insScreenshot = ImageGrab.grab(box)  # 截图
insScreenshot.save('.\pic\insScr.png')  # 截图保存
position = 'yuling'
picName = 'victoryPic'
str = '.\pic\%s\%s.png' % (position, picName)
img = cv2.imread(str)
cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey (0)
print(str)



"""
使用cv2.imshow()的时候，
如果图片太大，会显示不全并且无法调整，因
此在cv2.imshow()的前面加上这样的一个语句：
cv2.namedWindow('image', 0)，
得到的图像框就可以自己调整大小，
按住四个角会出来小箭头可以拉伸调整。
"""