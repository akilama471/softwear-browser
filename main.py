from database_setup import initialize_database
from folder_scanner import scan_folder
from file_watcher import start_watcher
from search_software import search_software
from file_operations import send_to_pendrive, delete_setup
import config

# Initialize the database
initialize_database()

# Scan the folder for existing setups
scan_folder(config.SETUPS_FOLDER_PATH)

# Start watching the folder for new setups
start_watcher(config.SETUPS_FOLDER_PATH)

# Example search
search_software(name="Photoshop")

# Send a setup file to a pendrive
send_to_pendrive("C:/Path/To/Your/Setup.exe", config.USB_DRIVE_PATH)

# Delete a setup file
delete_setup("C:/Path/To/Your/Setup.exe")
