import win32api

def extract_metadata(file_path):
    try:
        info = win32api.GetFileVersionInfo(file_path, "\\")
        file_version = info.get('FileVersion', 'Unknown')
        publisher = info.get('CompanyName', 'Unknown')

        return {'publisher': publisher, 'version': file_version}
    except:
        return {'publisher': 'Unknown', 'version': 'Unknown'}
