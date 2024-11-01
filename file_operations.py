import shutil
import os
import config

def send_to_pendrive(file_path, usb_drive_path=config.USB_DRIVE_PATH):
    try:
        shutil.copy(file_path, usb_drive_path)
        print(f"File {file_path} copied to {usb_drive_path}")
    except Exception as e:
        print(f"Error copying file: {e}")

def delete_setup(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted {file_path}")
    else:
        print(f"{file_path} does not exist!")
