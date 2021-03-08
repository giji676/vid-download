from selenium import webdriver
from moviepy.editor import *
import pytube
import os


def convert(path):
    file = os.listdir(path)
    for f in file:
        if f[-1] == "4":
            f = path + r"/" + f
            new_name = list(f)
            new_name[-1] = "3"
            new_name = "".join(new_name)

            mp4_file = f
            mp3_file = new_name
            videoclip = VideoFileClip(mp4_file)
            audioclip = videoclip.audio
            audioclip.write_audiofile(mp3_file)
            audioclip.close()
            videoclip.close()

    for f in file:
        if f[-1] == "4":
            new_path = path + r"/" + f
            os.remove(new_path)


def download_vid(url, path):
    print(url)
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download(path)


def download(playlist_link, path):
    driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
    driver.get(playlist_link)

    def collect_inks():
        elements = []
        elems = driver.find_elements_by_xpath("//a[@href]")
        print("Collecting links...")
        for elem in elems:
            elem = str(elem.get_attribute("href"))
            if "index=" in elem and elem not in elements:
                elements.append(elem)

        print(len(elements))

        return elements

    link_list = collect_inks()
    driver.quit()

    if not os.path.exists(path):
        os.mkdir(path)

    for url in link_list:
        print(url)
        download_vid(url, path)
