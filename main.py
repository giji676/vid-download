from selenium import webdriver
from moviepy.editor import *
import pytube
import os


def download(playlist_link, mp):
    quit()
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

    file_list = os.listdir()

    if not os.path.isfile("Music"):
        os.mkdir("Music")

    for i in link_list:
        print(i)
        url = i
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download("Music")

    path = "Music"

    file = os.listdir(path)

    if mp == "mp3":
        for f in file:
            if f[-1] == "4":
                f = path + "/" + f
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

        path = "Music/"
        for f in file:
            if f[-1] == "4":
                new_path = path + f
                os.remove(new_path)