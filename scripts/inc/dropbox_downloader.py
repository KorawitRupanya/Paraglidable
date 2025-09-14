import os
import zipfile
import subprocess

def download(dropbox_url, dest_dir, file_name, delete_zip=False):
    """
    Download a file from Dropbox using wget, and unzip if it's a valid zip file.

    Args:
        dropbox_url: The full Dropbox link (with ?dl=1 for direct download).
        dest_dir: Destination folder where file will be saved.
        file_name: Local filename to save as.
        delete_zip: If True, delete the zip file after extraction.
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

    # Try to unzip, even if extension is not .zip
    try:
        with zipfile.ZipFile(dest_path, "r") as zip_ref:
            zip_ref.extractall(dest_dir)
        print(f"Unzipped {file_name} into {dest_dir}")

        if delete_zip:
            os.remove(dest_path)
            print(f"Deleted zip file {file_name}")
    except zipfile.BadZipFile:
        print(f"{file_name} is not a zip archive. Skipping unzip.")
