import os
import pyzipper
from zipfile import ZipFile

def zip_file(file_path):
    zip_path = file_path + ".zip"
    with ZipFile(zip_path, 'w') as zipf:
        zipf.write(file_path, arcname=os.path.basename(file_path))
    return zip_path

def zip_with_password(file_path, password):
    zip_path = file_path + ".zip"
    with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(password.encode())
        zipf.write(file_path, arcname=os.path.basename(file_path))
    return zip_path

def zip_multiple_files(file_paths, output_zip, password=None):
    if password:
        with pyzipper.AESZipFile(output_zip, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
            zipf.setpassword(password.encode())
            for file_path in file_paths:
                zipf.write(file_path, arcname=os.path.basename(file_path))
    else:
        with ZipFile(output_zip, 'w') as zipf:
            for file_path in file_paths:
                zipf.write(file_path, arcname=os.path.basename(file_path))
    return output_zip
