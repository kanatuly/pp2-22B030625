from movies import movies as movies_dict
from check import check


def filter():
    movies_list = []
    for movie in movies_dict:
        if check(movie):
            movies_list.append(movie)
    return movies_list


print(filter())