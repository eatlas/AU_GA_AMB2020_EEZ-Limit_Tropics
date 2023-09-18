# Requires Python 3.5+

from urllib import request
from pathlib import Path
import os
import sys
import time
import zipfile
import tempfile
import shutil
import glob


def download(url, path):
    if os.path.exists(path):
        print(f"Skipping download of {path}; it already exists")
        return

    print(f"Downloading from {url}")

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
    }

    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    
    total_size = int(response.getheader('Content-Length', 0))
    
    chunk_size = 1024*100  # size of chunks in bytes

    with open(path, 'wb') as file:
        if total_size == 0:
            print("Could not determine file size.")
            bytes_downloaded = 0
            while chunk := response.read(chunk_size):
                file.write(chunk)
                bytes_downloaded += len(chunk)
                print(f"\rDownloaded {bytes_downloaded} bytes", end='')
        else:
            num_bars = total_size // chunk_size
            for chunk in range(num_bars+1):
                file.write(response.read(chunk_size))
                print(f"\rDownloaded Chunk {chunk} of {num_bars}", end='')
        print()  # Newline at end of progress output

    print("Download complete")


# Unzip the specified file to the unzipPath. This will create the unzipPath
# if necessary. This will skip the unzip if the unzip directory already
# exists.
def unzip(zip_file_path, unzip_path):
    print("Unzipping " + zip_file_path + " to " + unzip_path)
    Path(unzip_path).mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(unzip_path)

def move_files(patterns, source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
        print(f'Making destination directory {destination_directory}')
        
    # Find and move files matching the patterns
    for pattern in patterns:
        for filepath in glob.glob(os.path.join(source_directory, pattern)):
            # Get the filename from the filepath
            filename = os.path.basename(filepath)
            
            # Construct the destination filepath
            destination_filepath = os.path.join(destination_directory, filename)
            
            # Move the file to the destination directory
            shutil.move(filepath, destination_filepath)
            print(f"Moved {filepath} to {destination_filepath}")


def download_unzip_keep_subset(url, zip_file_patterns, destination_directory):
    with tempfile.TemporaryDirectory() as temp_dir:

        download(url, os.path.join(temp_dir,'download.zip'))
        unzip(os.path.join(temp_dir,'download.zip'), os.path.join(temp_dir,'download'))

        # Only keep a subset of the files to limit the storage used
        move_files(zip_file_patterns, os.path.join(temp_dir,'download'), destination_directory)
    # Outside the block, the temporary directory and its contents will be automatically deleted


src_data = 'src-data'

# Download the zipped collection of shapefiles, unpack them into a temporary
# directory then move the relevant datasets into the original folder.
# Finally remove the tmp folder.
data_dir = 'AU_GA_AMB_2020'

# EEZ
# https://pid.geoscience.gov.au/dataset/ga/144571
direct_download_url = 'https://d28rz98at9flks.cloudfront.net/144571/144571_01_0.zip'
# Define the patterns to search for
patterns = [
    os.path.join('Shapefiles', 'Exclusive_Economic_Zone_AMB2020_Limits.*'),
]
download_unzip_keep_subset(direct_download_url, patterns, os.path.join(src_data, 'AU_GA_AMB_2020'))


direct_download_url = 'https://d28rz98at9flks.cloudfront.net/61395/61395_shp.zip'
# Define the patterns to search for
patterns = [
    os.path.join('australia', 'cstauscd_r.*'),
]
download_unzip_keep_subset(direct_download_url, patterns, os.path.join(src_data, 'AU_GA_Coast-100k_2004'))

