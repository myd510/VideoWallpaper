import VideoWallpaper
from win32process import CreateProcess, STARTUPINFO
from win32gui import FindWindow
from time import sleep

if __name__ == "__main__":
    #视频地址
    video_path = r".\videos\N0va LookDev Test - 3.横屏_60fps(Av968128488,P3).mp4"
    #自定义播放设置：静音
    #custom_settings = '-an'
    custom_settings =''
    #默认播放设置：全屏，无限循环，无输出
    cmdline = "-fs -loop 0 \"{}\" -loglevel quiet".format(video_path) + custom_settings
    #播放器地址
    ffplay_path=r".\ffmpeg-win64\ffplay.exe"
    #创建播放器进程
    CreateProcess(ffplay_path, cmdline, None, None, 0, 0, None, None, STARTUPINFO())
    while(True):#等待播放器窗口创建完毕
        #查找播放器窗口
        player_window_handel = FindWindow("SDL_app", video_path)
        if(player_window_handel!=0):#找到播放器窗口
            #视频窗口窗口原点会不在00，sleep一个极短的时间可以解决
            sleep(0.01)
            break
    #开始视频壁纸
    VideoWallpaper.RunVideoWallpaper(player_window_handel)
