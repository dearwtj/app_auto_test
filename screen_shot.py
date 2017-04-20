#coding:utf8
import os


class Screenshot:
    def __init__(self,phone_filepath_filename,window_filepath_filename):
#         adb shell /system/bin/screencap -p /sdcard/01.png
#         adb pull /sdcard/01.png d:\01.png
        try:
#             截图并保存到本地指令
            shot_command = 'adb shell /system/bin/screencap -p'+' '+ phone_filepath_filename
#             将图片从手机转移到电脑指令
            trans_command = 'adb pull'+' '+phone_filepath_filename+' '+window_filepath_filename
            os.popen(shot_command)
            os.popen(trans_command)
        except Exception as e:
            print e