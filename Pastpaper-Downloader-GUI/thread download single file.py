from PyQt5.QtCore import pyqtSignal
import time
import requests

class WorkThread(QThread):
    progressBarValue = pyqtSignal(int)
    # trigger2 = pyqtSignal(str)
    url = ""
    basedir = "./"
    def __init__(self):
        super(WorkThread, self).__init__()
        # self.url = file_url
        # self.path = file_path+file_name
        # self.name = file_name
        # if not os.path.isdir(file_path):
        #     os.makedirs(file_path)
        # else:
        #     if os.path.isfile(file_path+file_name):
        #         print(file_name,'has downloaded previously!')
        #         return None
    def run(self):
        print("thread run..")
        print("down file:" + self.url)
        start = time.time()
        size = 0
        r = requests.get(self.url, stream=True)  # stream 必须带上
        chunk_size = 1024  # 每次下载大小
        content_size = int(r.headers['content-length'])
        if r.status_code == 200:
            print("[文件大小]:%.2f MB" % (content_size / chunk_size / 1024))
            with open(self.path, "wb") as file:
                for data in r.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    size += len(data)  # 已下载大小
                    num = int(size / content_size * 100)
                    self.progressBarValue.emit(num)
                    # \r 指定第一个字符开始，搭配end属性完成覆盖进度条
                    print("\r" + "[下载进度]：%s%.2f%%" % (
                        ">" * int(size * 50 / content_size), float(size / content_size * 100)), end="")
            end = time.time()  # 结束时间
            # self.trigger2.emit("下载完成！用时%.2f秒" % (end - start))
            print("\n" + "全部下载完成！用时%.2f秒" % (end - start))


def download_files_start(self):
    ui.download.setText("正在下载...")
    ui.download.setDisabled(True)
    # for i in pa.files_pools:
    self.workthread = WorkThread()
    self.workthread.progressBarValue.connect(ui.single_progressBar.setValue)#act.set_progressbar_value)
    self.workthread.start()