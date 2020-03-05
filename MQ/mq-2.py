#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO # 导入库，并进行别名的设置
import time

CHANNEL=7 # 确定引脚口。按照真实的位置确定
GPIO.setmode(GPIO.BOARD) # 选择引脚系统，这里我们选择了BOARD
GPIO.setup(CHANNEL,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#初始化引脚，将36号引脚设置为输入下拉电阻，因为在初始化的时候不确定的的引电平，因此这样设置是用来保证精准，（但是也可以不写“pull_up_down=GPIO.PUD_DOWN”）

# 带有异常处理的主程序
try:
    while True: # 执行一个while死循环
        status=GPIO.input(CHANNEL) # 检测36号引脚口的输入高低电平状态
        #print(status) # 实时打印此时的电平状态
        if status == True: # 如果为高电平，说明MQ-2正常，并打印“OK”
            print ( ' 正常 ' )      
        else:    # 如果为低电平，说明MQ-2检测到有害气体，并打印“dangerous”
            print ( ' 检测到危险气体 ! ! ! ' )
            time.sleep(0.1) # 睡眠0.1秒，以后再执行while循环
except KeyboardInterrupt: # 异常处理，当检测按下键盘的Ctrl+C，就会退出这个>脚本
    GPIO.cleanup() # 清理运行完成后的残余
