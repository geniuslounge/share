video_id = input("What is the video ID? ")
full_video = "https://youtu.be/" + video_id
import os
from bs4 import BeautifulSoup
import urllib.request
with urllib.request.urlopen(full_video) as response:
    html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')
# Set the refresh to the real page
refresh_html= '<meta http-equiv="refresh" content="0; ' + full_video + '">'


# OG items
#Set the OG Title
og_title = soup.find("meta", {"property":"og:title"})["content"]
og_title_html = '<meta property="og:title" content="' + og_title + '"/>'


#Set the OG Image
og_image = soup.find("meta", {"property":"og:image"})["content"]
og_image_html = '<meta property="og:image" content="' + og_image + '"/>'

# Set the OG Description
og_description = soup.find("meta", {"property":"og:description"})["content"]
og_description_html = '<meta property="og:description" content="' + og_description + '"/>'

# set the og icon
og_icon = 'https://geniuslounge.github.io/share/icon.png'
og_icon_html = '<meta property="og:icon" content="' + og_icon + '"/>'


# Twitter items
# Set twitter card type
twitter_card = "summary_large_image"
twitter_card_html = '<meta name="twitter:card" content="' + twitter_card + '"/>'

# Set twitter site
twitter_site = "@geniuslounge"
twitter_site_html = '<meta name="twitter:site" content="' + twitter_site + '"/>'

# Set twitter creator
twitter_creator = "@geniuslounge"
twitter_creator_html = '<meta name="twitter:creator" content="' + twitter_creator + '"/>'

# Set twitter title
twitter_title = soup.find("meta", {"name":"twitter:title"})["content"]
twitter_title_html = '<meta name="twitter:title" content="' + twitter_title + '"/>'

# Set twitter description
twitter_description = soup.find("meta", {"name":"twitter:description"})["content"]
twitter_description_html = '<meta name="twitter:description" content="' + twitter_description + '"/>'


# Set twitter image
twitter_image = soup.find("meta", {"name":"twitter:image"})["content"]
twitter_image_html = '<meta name="twitter:image" content="' + twitter_image + '"/>'


html_output = '<!DOCTYPE html><html><head>'+ refresh_html + og_title_html + og_image_html + og_description_html + og_icon_html + twitter_card_html + twitter_site_html + twitter_creator_html + twitter_title_html + twitter_description_html + twitter_image_html + '</head><body></body></html>'
soup = BeautifulSoup(html_output, 'html.parser')
html_output = soup.prettify()
os.system('clear')
print(html_output)