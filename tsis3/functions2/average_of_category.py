from movies import movies as movies_dict


def compute(category):
    sum = 0
    cnt = 0
    for movie in movies_dict:
        if movie['category'] == category:
            sum += movie['imdb']
            cnt += 1
    return sum/cnt


print(compute('Action'))