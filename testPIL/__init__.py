import win32gui
import PIL
from PIL import ImageGrab, Image


def get_window_info():  # 获取窗口信息
    wdname = u'钻石茶苑 20190523_154601_x.log'
    handle = win32gui.FindWindow(0, wdname)  # 获取窗口句柄
    if handle == 0:
        # text.insert('end', '提示：\n')
        # text.see('end')  # 自动显示底部
        return None
    else:
        return win32gui.GetWindowRect(handle)
# 左上角的x值，左上角的y值，右下角的x值，右下角的y值
print(get_window_info())
window_size = get_window_info()

def get_posx(x, window_size):  # 返回x相对坐标
    return (window_size[2] - window_size[0]) * x / 850

def get_posy(y, window_size):  # 返回y相对坐标
    return (window_size[3] - window_size[1]) * y / 590

# print(get_posx(600, window_size))
# print(get_posy(800, window_size))

topx, topy = window_size[0], window_size[1]
# img_ready = ImageGrab.grab((topx + get_posx(500, window_size), topy + get_posy(480, window_size),
# 							topx + get_posx(540, window_size), topy + get_posy(500, window_size)))

img_ready = ImageGrab.grab(get_window_info())
# 查看图片
img_ready.show()

def get_hash(img):
    img = img.resize((16, 16), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
    avg = sum(list(img.getdata())) / 256  # 计算像素平均值
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))  # 每个像素进行比对,大于avg为1,反之为0
    return ''.join(map(lambda j: '%x' % int(s[j:j+4], 2), range(0, 256, 4)))



print(get_hash(img_ready))


def hamming(hash1, hash2, n=20):
    b = False
    assert len(hash1) == len(hash2)
    if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
        b = True
    return b


ready_hash = get_hash(img_ready)

print(hamming(get_hash(img_ready), ready_hash, 10))