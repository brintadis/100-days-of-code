from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

films = soup.find_all(name="h3", class_="title")
films_list = [film.getText() for film in films]
films_list.reverse()
# print(films)
# print(films_list)

with open("movies.txt", "w", encoding="utf-8") as file:
    for film in films_list:
        file.write(f"{film}\n")