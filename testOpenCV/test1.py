# coding=utf-8
'''win32控制台'''
import win32gui
import win32con
import win32api
import win32con

'''移动鼠标需要'''
from ctypes import *

'''图片处理cv'''
import cv2

'''随机数'''
import random

'''截图'''
from PIL import ImageGrab

'''时间库'''
import time


def clickLeftCur():
	# 点击鼠标 需要管理员权限
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def moveCurPos(x, y):  # 移动鼠标
	windll.user32.SetCursorPos(x, y)


def getWindowInfo():
	# 获得句柄
	wdname = u'钻石茶苑 20190523_154601_x.log'
	handle = win32gui.FindWindow(0, wdname)  # 获得句柄
	x1, y1, x2, y2 = win32gui.GetWindowRect(handle)  # 获得窗口坐标
	box = x1, y1, x2, y2
	# print (x1, y1, x2, y2)
	return box



def screenShot(box):
	# 截图
	# box为窗口坐标
	randomDelay(0.5,1)
	insScreenshot = ImageGrab.grab(box)  # 截图
	insScreenshot.save('d:\yys\insScr.png')  # 截图保存
	img = cv2.imread('d:\yys\insScr.png', 0)  # 打开图片
	return img

def match(img1, img2):
	# 图像匹配
	# img1为即时截图，
	# img2为匹配图
	res = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
	return res


def randomDelay(a, b):
	# 随机延迟
	time.sleep(random.uniform(a, b))


def randomLocation(x, y):
	# 随机位置
	# x,y均为数组
	xl = random.randint(x[0], x[1])
	yl = random.randint(y[0], y[1])
	return xl, yl

def getPoint(res, upperLeftCornerXCoordinate, upperLeftCornerYCoordinate, clickRange):
	# 点击坐标
	# res为图像匹配返回二维图像
	# upperLeftCornerXCoordinate为窗口左上角的x坐标
	# upperLeftCornerXCoordinate为窗口左上角的y坐标
	# clickRange为匹配图像的像素
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	xRange = [upperLeftCornerXCoordinate + max_loc[0], upperLeftCornerXCoordinate + max_loc[0] + clickRange[0]]
	yRange = [upperLeftCornerYCoordinate + max_loc[1], upperLeftCornerYCoordinate + max_loc[1] + clickRange[1]]
	x, y = randomLocation(xRange, yRange)
	return x, y


box = getWindowInfo()
insInterface = screenShot(box)

username=cv2.imread('../images/username.png',0)
res1 = match(insInterface, username)
sp1 = username.shape
clickRange1 = [sp1[1], sp1[0]-5]
x1, y1 = getPoint(res1, box[0], box[1], clickRange1)
moveCurPos(x1, y1)
clickLeftCur()


randomDelay(1, 3)

username=cv2.imread('../images/net.png',0)
res2 = match(insInterface, username)
sp2 = username.shape
clickRange2 = [sp2[1], sp2[0]-5]
x2, y2 = getPoint(res2, box[0], box[1], clickRange2)
moveCurPos(x2, y2)
clickLeftCur()

randomDelay(1, 3)

login=cv2.imread('../images/login.png',0)
res = match(insInterface, login)
sp = login.shape
clickRange = [sp[1], sp[0]-5]
x, y = getPoint(res, box[0], box[1], clickRange)
moveCurPos(x, y)
clickLeftCur()

randomDelay(1, 3)