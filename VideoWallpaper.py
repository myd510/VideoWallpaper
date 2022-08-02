from win32gui import FindWindow, FindWindowEx, ShowWindow, SendMessageTimeout, SetParent, EnumWindows, GetWindowText
from win32con import SW_HIDE, SMTO_ABORTIFHUNG,SW_SHOW


def _MyCallback(hwnd, extra):#遍历窗口函数的回调函数（提前return退出遍历会报错）
    #当前窗口中查找图标窗口
    icon_window = FindWindowEx(hwnd, None, "SHELLDLL_DefView", None)
    if(icon_window):#当前窗口包含图标窗口
        #查找静态壁纸窗口并保存
        extra[0] = FindWindowEx(None, hwnd, "WorkerW", None)

def RunVideoWallpaper(player_window_handel):#设置视频壁纸
    if(player_window_handel):
        #查找桌面窗口
        desktop_window_handel = FindWindow("Progman", "Program Manager")
        #设置player_window为desktop_window的子窗口
        SetParent(player_window_handel, desktop_window_handel)
        #核心语句，向desktop_window发送0x52C启用Active Desktop
        SendMessageTimeout(desktop_window_handel, 0x52C, 0, 0, SMTO_ABORTIFHUNG, 500)
        #因为有两个同类同名的WorkerW窗口，所以遍历所有顶层窗口
        workerw=[0]
        EnumWindows(_MyCallback, workerw)
        #获取player_windows名称
        player_windows_name = GetWindowText(player_window_handel)
        while(True):#防止win+tab导致静态壁纸窗口重新出现及将player_window发送到图标窗口的父窗口(原因不明)
            #隐藏静态壁纸窗口
            ShowWindow(workerw[0], SW_HIDE)
            #判断player_window是否在desktop_window下
            player_under_desktop = FindWindowEx(desktop_window_handel, None, "SDL_app", player_windows_name)
            if(player_under_desktop==0):#如果player_window位置不正确
                #将player_window设置为desktop_window的子窗口
                SetParent(player_window_handel, desktop_window_handel)
