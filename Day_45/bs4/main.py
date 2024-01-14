import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.findAll(name="h3", class_="title")

movies_title = [title.getText() for title in all_movies]

movies = movies_title[::-1]

with open("../Day_45/bs4/movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")



