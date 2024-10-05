import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image

DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Normalize the file path
        event_path = os.path.normpath(event.src_path)

        if not event.is_directory and event_path.endswith(".webp"):
            # Adding a small delay to ensure the file is completely written to disk
            time.sleep(1)
            self.convert_to_png(event_path)

    def convert_to_png(self, webp_path):
        if not os.path.exists(webp_path):
            print(f"File does not exist after delay: {webp_path}")
            return

        # Convert .webp to .png by changing the extension
        png_path = os.path.splitext(webp_path)[0] + ".png"
        try:
            with Image.open(webp_path) as img:
                img.save(png_path, "PNG")
            print(f"Converted: {webp_path} -> {png_path}")
            
            # Delete the original .webp file
            os.remove(webp_path)
            print(f"Deleted original file: {webp_path}")
        except Exception as e:
            print(f"Failed to convert {webp_path}: {e}")

def main():
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, DOWNLOADS_FOLDER, recursive=False)
    observer.start()
    print(f"Watching {DOWNLOADS_FOLDER} for new WebP files...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    main()
