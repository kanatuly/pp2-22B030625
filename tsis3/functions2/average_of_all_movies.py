from movies import movies as movies_dict


def compute():
    sum = 0
    for movie in movies_dict:
        sum += movie['imdb']
    return sum/len(movies_dict)


print(compute())