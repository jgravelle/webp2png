import time
import win32serviceutil
import win32service
import win32event
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
import os

DOWNLOADS_FOLDER = r"C:\Users\j\Downloads"

class WebPToPNGHandler(FileSystemEventHandler):
    def on_created(self, event):
        event_path = os.path.normpath(event.src_path)
        if not event.is_directory and event_path.endswith(".webp"):
            time.sleep(1)
            self.convert_to_png(event_path)

    def convert_to_png(self, webp_path):
        if not os.path.exists(webp_path):
            print(f"File does not exist after delay: {webp_path}")
            return

        png_path = os.path.splitext(webp_path)[0] + ".png"
        try:
            with Image.open(webp_path) as img:
                img.save(png_path, "PNG")
            os.remove(webp_path)
            print(f"Converted and deleted: {webp_path} -> {png_path}")
        except Exception as e:
            print(f"Failed to convert {webp_path}: {e}")

class WebPToPNGService(win32serviceutil.ServiceFramework):
    _svc_name_ = "WebPToPNGService"
    _svc_display_name_ = "WebP to PNG Converter Service"
    _svc_description_ = "Automatically converts .webp files in Downloads to .png format."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.observer = Observer()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.observer.stop()
        self.observer.join()

    def SvcDoRun(self):
        event_handler = WebPToPNGHandler()
        self.observer.schedule(event_handler, DOWNLOADS_FOLDER, recursive=False)
        self.observer.start()
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(WebPToPNGService)
