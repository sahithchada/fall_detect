import requests
from bs4 import BeautifulSoup
import os

def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    response = requests.get(url, stream=True)
    file_name = os.path.join(dest_folder, url.split('/')[-1])
    with open(file_name, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f'Downloaded: {file_name}')

def download_images_from_rgb_directory(url, dest_folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    
    for link in links:
        href = link.get('href')
        if href.endswith(('.jpg', '.png', '.jpeg')):
            img_url = url + href
            download_file(img_url, dest_folder)

def find_rgb_directories_and_download(base_url, main_page_url, dest_folder):
    response = requests.get(main_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    
    for link in links:
        href = link.get('href')
        if href.endswith('/'):
            sub_dir_url = main_page_url + href
            rgb_dir_url = sub_dir_url + 'rgb/'
            new_dest_folder = os.path.join(dest_folder, href.strip('/'), 'rgb')
            download_images_from_rgb_directory(rgb_dir_url, new_dest_folder)

# URL of the main data directory
base_url = 'https://www.falldataset.com/'
main_page_url = base_url + 'data/'

# Destination folder for downloads
dest_folder = '/Users/sahithreddy/Desktop/fall_detect/Human-Falling-Detect-Tracks/videos/fall_videos_website'

find_rgb_directories_and_download(base_url, main_page_url, dest_folder)
