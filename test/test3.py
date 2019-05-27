

# print(b'1024')
# print(ord('O'))
# print(chr(99))

# print(ord(chr(99)))
# print(chr(ord('T')))

# print(ord('T'))
# print(chr(88))
#
# print(len(b'102454'))

# print('ABC'.encode('UTF-8') , len('ABC'.encode('UTF-8')))
# print('ABC'.encode('ascii'), len('ABC'.encode('ascii')))
#
# print(b'ABC'.decode('ascii'))
# print(b'ABC'.decode('UTF-8'))
#
# print('hello %x' % 123)
#
# print(ord('P'))
# print(chr(99))
#
# print('hello {0}, xxx {1:.2f}'.format('abc',80))
import time
import win32gui
import win32api
import win32con
from ctypes import *
SW = 1377
SH = 768


def mouse_absolute(x,y,x2,y2):
    time.sleep(2)
    windll.user32.SetCursorPos(x, y)    #鼠标移动到
    time.sleep(2)
    windll.user32.SetCursorPos(200, 300)  # 鼠标移动到
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(2)


    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)    #左键按下
    # time.sleep(0.2)
    # mw = int(x2 * 65535 / SW)
    # mh = int(y2 * 65535 / SH)
    # win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, mw, mh, 0, 0)
    # time.sleep(0.2)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

mouse_absolute(200,500,300,400)