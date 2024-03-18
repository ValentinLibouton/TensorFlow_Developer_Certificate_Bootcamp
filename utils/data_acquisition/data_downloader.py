import os
import zipfile
import subprocess
import tarfile
try:
    import magic
except ImportError:
    magic = None
try:
    import py7zr
except ImportError:
    py7zr = None

def extract_zip_file(filename, destination=None):
    print(f"Extracting {filename} as ZIP...")
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(path=destination)
    print(f"{filename} has been extracted to {destination if destination else 'current directory'}.")

def extract_tar_file(filename, destination=None):
    print(f"Extracting {filename} as TAR.GZ...")
    with tarfile.open(filename, 'r:gz') as tar_ref:
        tar_ref.extractall(path=destination)
    print(f"{filename} has been extracted to {destination if destination else 'current directory'}.")

def extract_7z_file(filename, destination=None):
    if py7zr:
        print(f"Extracting {filename} as 7z...")
        with py7zr.SevenZipFile(filename, mode='r') as zip_ref:
            zip_ref.extractall(path=destination)
        print(f"{filename} has been extracted to {destination if destination else 'current directory'}.")
    else:
        print("py7zr module not available. Unable to extract .7z files.")

def extract_archive_file(filename, destination=None):
    if magic:
        mime_type = magic.from_file(filename, mime=True)
        if mime_type == 'application/zip':
            extract_zip_file(filename, destination)
        elif mime_type in ['application/gzip', 'application/x-gzip']:
            extract_tar_file(filename, destination, mode='r:gz')
        elif mime_type == 'application/x-tar':
            extract_tar_file(filename, destination, mode='r:')
        elif mime_type == 'application/x-bzip2':
            extract_tar_file(filename, destination, mode='r:bz2')
        elif mime_type == 'application/x-7z-compressed':
            extract_7z_file(filename, destination)
        else:
            print(f"Archive type {mime_type} not supported")
    else:
        print("magic module not available. Unable to determine archive type. "
              "Please install python-magic to enable this feature.")


def download_data(url, filename, extract=False, destination=None, remove_archive=False):
    if not os.path.exists(filename):
        # Download the file using wget
        subprocess.run(["wget", "-nc", url, "-O", filename])
        print(f"{filename} has been downloaded.")
    else:
        print(f"The file {filename} already exists.")

    if extract:
        extract_archive_file(filename, destination)

        # Remove the archive file if requested
        if remove_archive:
            os.remove(filename)
            print(f"{filename} has been removed after extraction.")
