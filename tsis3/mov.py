def movies(romans):
    for m in movies:
        if m["name"] == romans and m["imdb"] > 5.0 and m["imdm"]<7.0: 
            imdb_score = True 
        elif m["name"] == romans and m["imdb"] < 5.5:
            imdb_score = "Sorry, score less than 5.5"
    return imdb_score