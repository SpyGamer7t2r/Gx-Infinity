import os
import pyzipper
from zipfile import ZipFile, BadZipFile

def unzip_file(zip_path, extract_to, password=None):
    try:
        if password:
            with pyzipper.AESZipFile(zip_path, 'r') as zipf:
                zipf.setpassword(password.encode())
                zipf.extractall(path=extract_to)
        else:
            with ZipFile(zip_path, 'r') as zipf:
                zipf.extractall(path=extract_to)
        return True, f"✅ Extracted to: {extract_to}"
    except RuntimeError as e:
        return False, f"❌ Wrong password: {e}"
    except BadZipFile as e:
        return False, f"❌ Bad zip file: {e}"
    except Exception as e:
        return False, f"❌ Error: {e}"
