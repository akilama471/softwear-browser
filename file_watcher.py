from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from folder_scanner import scan_folder  # Update this if needed

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(('.exe', '.msi')):
            print(f"New file detected: {event.src_path}")
            scan_folder(os.path.dirname(event.src_path))  # Assuming scan_folder needs a directory

def start_watcher(directory):
    observer = Observer()
    event_handler = Handler()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()
