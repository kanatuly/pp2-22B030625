from movies import movies as movies_dict

def filter(category):
    movies_list = []
    for movie in movies_dict:
        if movie['category'] == category:
            movies_list.append(movie)
    return movies_list

print(filter('Romance'))