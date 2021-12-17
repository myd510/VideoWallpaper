from win32gui import FindWindow, FindWindowEx, ShowWindow, SendMessageTimeout, SetParent, EnumWindows
from win32con import SW_HIDE, SMTO_ABORTIFHUNG
from win32process import CreateProcess, STARTUPINFO
from time import sleep

def _MyCallback(hwnd, extra):#遍历窗口函数的回调函数（提前return退出遍历会报错）
    #查找当前被遍历顶层窗口包含的桌面图标所在窗口
    icon_window = FindWindowEx(hwnd, None, u"SHELLDLL_icon_window", None)
    if(icon_window!=0):#当前被遍历顶层窗口包含桌面图标所在窗口
        #查找下一个类名为WorkerW的顶层窗口（即静态壁纸所在窗口）
        workerw = FindWindowEx(None, hwnd, u"WorkerW", None)
        #隐藏静态壁纸所在窗口
        ShowWindow(workerw, SW_HIDE)

def RunVideoWallpaper(video_path, custom_settings='', ffplay_path=r".\ffmpeg-win64\ffplay.exe"):#设置视频壁纸
    #查找桌面窗口
    desktop_window = FindWindow(u"Progman", "Program Manager")
    #默认播放设置：全屏，无限循环，无输出
    cmdline = "-fs -loop 0 {} \"{}\" -loglevel quiet".format(custom_settings, video_path)
    #创建播放器进程
    CreateProcess(ffplay_path, cmdline, None, None, 0, 0, None, None, STARTUPINFO())
    while(True):#等待播放器窗口创建完毕
        #查找播放器窗口
        player_window = FindWindow(u"SDL_app", video_path)
        if(player_window!=0):#找到播放器窗口
            #视频窗口窗口原点会不在00，sleep一个极短的时间可以解决
            sleep(0.001)
            break
    #核心语句，向desktop_window发送0x52C启用Active Desktop
    SendMessageTimeout(desktop_window, 0x52C, 0, 0, SMTO_ABORTIFHUNG, 100)
    #将player_window设置为desktop_window的子窗口
    SetParent(player_window, desktop_window)
    #因为有两个同类同名的WorkerW窗口，所以遍历所以顶层窗口
    EnumWindows(_MyCallback, None)
