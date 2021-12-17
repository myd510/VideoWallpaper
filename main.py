import VideoWallpaper
if __name__ == "__main__":
    #视频地址
    video_path = r"C:\Users\admin\Videos\testvideo.mp4"
    #自定义播放设置：静音
    custom_settings = '-an'
    #开始视频壁纸
    RunVideoWallpaper(video_path, custom_settings)
    #暂停程序
    input()
