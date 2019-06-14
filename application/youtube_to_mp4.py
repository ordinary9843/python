import winreg
import base64
import os
import threading
import pytube
from tkinter import *
from icon import img

def download():
    global progress_var

    # 建立執行緒
    thread = threading.Thread(target = youtube_to_mp4)

    # 執行緒執行完畢後自動回收
    thread.start()

def youtube_to_mp4():
    global desktop_path, download_button, url_entry, filename_var, progress_var

    # 禁用按鈕
    download_button.config(state = 'disabled')

    # 取得輸入連結
    url = url_entry.get()

    if url == '':
        progress_var.set('Please enter url')

        # 恢復按鈕
        download_button.config(state = 'normal')
    else:
        progress_var.set('Please wait')

        try :

            # 建立 youtube 物件並傳入影片連結
            yt = pytube.YouTube(url)

            # 取得下載進度
            yt.register_on_progress_callback(progress)

            # 取得影片串流
            stream = yt.streams.first()

            # 取得檔案名稱
            filename_var.set(yt.title)

            # 下載檔案
            stream.download(desktop_path)

        except Exception:
            progress_var.set('This url invalid')

            # 恢復按鈕
            download_button.config(state = 'normal')

def progress(stream, _chunk, _file_handle, bytes_remaining):
    global download_button, progress_var

    # 檔案大小
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = int(bytes_downloaded / total_size * 100)

    if percentage_of_completion < 100:
        progress_var.set('Progress (' + str(percentage_of_completion) + '%)')
    else:
        progress_var.set('Success (' + str(percentage_of_completion) + '%)')

        # 恢復按鈕
        download_button.config(state = 'normal')

    window.update()

# 版本號
version = '(0.0.0.1)'

# 取得桌面路徑
winreg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
desktop_path = winreg.QueryValueEx(winreg_key, 'Desktop')[0]

# 建立 tkinter 物件
window = Tk()
window.title('Youtube to mp4 ' + version)

# 視窗寬與高
w = 800
h = 100

# 取得螢幕寬與高
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()

# 計算 x 與 y 位置
x = int(window_width / 2) - int(w / 2)
y = int(window_height / 2) - int(h / 2)

# 使視窗置中於螢幕
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

# 透過 icon.py 將圖片轉為 base64 編碼在做icon使用
tmp = open('tmp.ico', 'wb+')
tmp.write(base64.b64decode(img))
tmp.close()
window.iconbitmap('tmp.ico')
os.remove('tmp.ico')

# 禁止視窗改變大小
window.resizable(0, 0)

# Youtube Url 標籤
youtube_label = Label(window, text = 'Youtube Url')
youtube_label.place(x = 20, y = 20)

# 連結輸入框
url_entry = Entry(window, bd = 1)
url_entry.place(x = 120, y = 20, width = 560)

# Download 按鈕
download_button = Button(window, text = 'Download', command = download)
download_button.place(x = 695, y = 15)

# 檔案名稱
filename_var = StringVar()
filename_var.set('')
filename_label = Label(window, textvariable  = filename_var)
filename_label.place(x = 20, y = 60, width = 560)

# 下載進度
progress_var = StringVar()
progress_var.set('Youtube to mp4')
progress_label = Label(window, textvariable  = progress_var)
progress_label.place(x = 595, y = 60, width = 185)

window.mainloop()