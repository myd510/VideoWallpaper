import VideoWallpaper
from win32process import CreateProcess, CREATE_NO_WINDOW, STARTUPINFO
from win32gui import FindWindow
from win32api import GetSystemMetrics
from win32con import SM_CXSCREEN, SM_CYSCREEN
from time import sleep

if __name__ == "__main__":
    #获得屏幕分辨率
    screen_width = GetSystemMetrics(SM_CXSCREEN)
    screen_screen = GetSystemMetrics(SM_CYSCREEN)
    #视频地址
    video_path = r".\videos\N0va LookDev Test - 3.横屏_60fps(Av968128488,P3).mp4"
    #自定义播放设置：不显示字幕，静音
    custom_settings = '-sn -an'
    #自定义播放设置：初始音量10
    #custom_settings ='-volume 10'
    #默认播放设置：全屏，强制分辨率，无限循环，无输出
    cmdline = "-fs -x {0} -y {1} -loop 0 \"{2}\" -loglevel quiet ".format(screen_width, screen_screen, video_path) + custom_settings
    #播放器地址
    ffplay_path=r".\ffmpeg-win64\ffplay.exe"
    #创建播放器进程(无窗口)
    CreateProcess(ffplay_path, cmdline, None, None, 0, CREATE_NO_WINDOW, None, None, STARTUPINFO())
    while(True):#等待播放器窗口创建完毕
        #查找播放器窗口
        player_window_handel = FindWindow("SDL_app", video_path)
        if(player_window_handel!=0):#找到播放器窗口
            #视频窗口窗口原点会不在00，sleep可以解决
            sleep(0.1)
            break
    #开始视频壁纸
    VideoWallpaper.RunVideoWallpaper(player_window_handel)
