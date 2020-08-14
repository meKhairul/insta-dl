import requests
from bs4 import BeautifulSoup
import lxml
import wget
def instadl():
    url=input("Enter the URL: ")
    page=requests.get(url)
    soup = BeautifulSoup(page.text,"lxml")
    image = soup.find("meta",  property="og:image")
    imagelink= image["content"] if image else None
    video = soup.find("meta",  property="og:video")
    videolink= video["content"] if video else None
    wget.download(videolink) if videolink else wget.download(imagelink)
instadl()