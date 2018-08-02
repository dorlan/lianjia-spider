# -*- coding: utf-8 -*-
#这里需要引入三个模块
import time, os, sched

# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数
# 第二个参数以某种人为的方式衡量时间
schedule = sched.scheduler(time.time, time.sleep)

def perform_command(cmd):
    try:
        os.system(cmd)
    except Exception as e:
        print("Execute {}, Catch Exception: {}".format(cmd, e.message))

def timming_exe(cmd, inc = 60):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(inc, 0, perform_command, cmd)
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()

print(u"开始采集珠海 [新房] 数据...")
perform_command("python ./loupan.py zh")

print(u"开始采集珠海 [二手房] 数据...")
perform_command("python ./ershou.py zh")

print(u"开始采集珠海 [租房] 数据...")
perform_command("python ./zufang.py zh")
