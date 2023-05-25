import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'Archivo creado: {event.src_path}')
    
    def on_modified(self, event):
        print(f'Archivo modificado: {event.src_path}')
    
    def on_deleted(self, event):
        print(f'Archivo eliminado: {event.src_path}')


def watch_dir(path, callback):
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            callback()
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



if __name__ == '__main__':
    def on_change():
        print('¡Cuidado con los cambios en el directorio!')
    watch_dir("src", on_change)