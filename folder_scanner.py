import os
from database_setup import SoftwareSetup
from metadata_extractor import extract_metadata

def scan_folder(directory):
    # Get the list of files in the directory
    files_in_folder = {os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(('.exe', '.msi'))}
    
    # Get the list of files currently in the database
    files_in_db = {setup.path for setup in SoftwareSetup.select()}

    # Add new files to the database
    for file_path in files_in_folder:
        if not SoftwareSetup.get_or_none(SoftwareSetup.path == file_path):
            file_name = os.path.basename(file_path)
            metadata = extract_metadata(file_path)
            SoftwareSetup.create(
                name=file_name,
                publisher=metadata.get('publisher', 'Unknown'),
                category='Uncategorized',
                version=metadata.get('version', 'Unknown'),
                path=file_path
            )
            print(f"Added {file_name} to the database.")

    # Remove files from the database that are no longer in the directory
    for setup in SoftwareSetup.select():
        if setup.path not in files_in_folder:
            setup.delete_instance()
            print(f"Removed {setup.name} from the database.")

    print("Folder scan completed and database updated.")
