import requests
from bs4 import BeautifulSoup

links = []
videos = []

videos_url = "https://sample-videos.com/"

url = "https://sample-videos.com/index.php#sample-mp4-video"

r = requests.get (url)
html_content = r.content
soup = BeautifulSoup (html_content, 'html.parser')

for a in soup.find_all('a', href=True):
    videos.append(a['href'])

videos = videos[26:len(videos)-1]


for i in range(len(videos)):
  links.append(videos_url + videos[i])

def download_video_series(video_links):
	for link in video_links:
		file_name = link.split('/')[-1]
		r = requests.get(link, stream = True)
		with open(file_name, 'wb') as f:
			for chunk in r.iter_content(chunk_size = 1024*1024):
				if chunk:
					f.write(chunk)
	return
#temp = links[0:2]

download_video_series(links)