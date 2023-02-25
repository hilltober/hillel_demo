import os
import subprocess

version_info = subprocess.check_output(['google-chrome', '--version']).decode('utf-8')
version = version_info.strip().split(' ')[2]
version_without_minor = '.'.join(version.split('.')[:3])
os.system(f'wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{version_without_minor}')
full_version = subprocess.check_output(['cat', f'LATEST_RELEASE_{version_without_minor}']).decode('utf-8')

file_link = f'https://chromedriver.storage.googleapis.com/{full_version}/chromedriver_linux64.zip'

os.system(f"wget {file_link}")
os.system("unzip chromedriver_linux64.zip")
os.system("rm -rf chromedriver_linux64.zip")

os.system("mkdir /usr/share/chromedriver")
os.system("cp -r chromedriver /usr/share/chromedriver")
os.system("rm -rf chromedriver")

os.system("ln -s /usr/share/chromedriver/chromedriver /usr/local/bin/chromedriver")
