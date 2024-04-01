import pyautogui
import time

# 延迟一段时间，以便你有足够的时间将鼠标移动到目标位置
time.sleep(3)

while True:
    # 获取鼠标当前位置
    x, y = pyautogui.position()

    # 模拟鼠标点击
    pyautogui.click(x, y)
    print(f'clicking {x, y}')
    
    time.sleep(3)