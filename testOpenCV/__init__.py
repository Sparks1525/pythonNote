import cv2
from PIL import Image
import operator
import numpy as np
import cv2

# img = cv2.imread('../images/login.png',1)
# # cv2.imshow('img',img)
# # cv2.namedWindow('showing', cv2.WINDOW_NORMAL)
# cv2.imshow("showing",img)
# cv2.waitKey(0)
# # cv2.destroyAllWindows()


# login=Image.open("../images/login.png")
# logo=Image.open("../images/logo.png")

def match(img1, img2):
	# 图像匹配
	# img1为即时截图，
	# img2为匹配图
	res = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
	return res

login = cv2.imread('../images/login.png',0)
logo = cv2.imread('../images/logo.png',0)
re = cv2.matchTemplate(login, login, cv2.TM_CCOEFF_NORMED)

print(re)




# c=operator.eq(login,logo)
# print(c)
