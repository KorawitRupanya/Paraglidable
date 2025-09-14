import os
import zipfile
import subprocess

def download(dropbox_url, dest_dir, file_name):
    """
    Download a file from Dropbox using wget.

    Args:
        dropbox_url: The full Dropbox link (with ?dl=1 for direct download).
        dest_dir: Destination folder where file will be saved.
        file_name: Local filename to save as.
    """
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, file_name)

    try:
        subprocess.run(
            ["wget", "-O", dest_path, dropbox_url],
            check=True
        )
        print(f"Downloaded {file_name} to {dest_dir}")
    except subprocess.CalledProcessError:
        raise RuntimeError(f"Failed to download {file_name} from {dropbox_url}")
