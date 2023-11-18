import time


def focus_clock(minutes):


start_time = time.time()


end_time = start_time + minutes * 60


while time.time() < end_time:


print("专注中...")


time.sleep(60) # 每分钟更新一次


print("专注时间结束！")


# 调用函数，设定专注时间为25分钟


focus_clock(25)
