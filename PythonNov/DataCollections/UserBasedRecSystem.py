dataset = {
    "action" : ["Ironman","Thor","KGF", "Batman","Superman","Aquaman","Hulk","Baahubali",
                "Master","Avengers"],
    "comedy" : ["Thor","Golmaal","Hera Pheri", "Dhamaal", "Yes man", "The mask"],
    "sci-fi" : ["Ironman","Interstellar", "Gravity"],
    "thriller" : ["Oculus","KGF","Superman","Master","Avengers","It","Kahani"],
    "horror" : ["Oculus","It","The Nun"]
}

user_1 = {"Ironman","Avengers","Gravity","It","The mask","Thor","Hulk","Batman","KGF"}
user_2 = {"Ironman","Master","Avengers","It","Golmaal","Thor","Aquaman","KGF"}

commonMovies = user_1.intersection(user_2)
scores = {}
for key in dataset:
    movies = set(dataset[key])
    numer = movies.intersection(commonMovies)
    denom = movies.union(commonMovies)
    score = len(numer) / len(denom)
    # score = len(movies.intersection(user)) / len(movies.union(user))
    scores[key] = round(score,2)

print(scores)

max_value = max(scores.values())
for key in scores:
    if scores[key] == max_value:
        category = key
        break

rec_user_2 = set(dataset[category]).intersection(user_1) - user_2
print("Recommended Movies for User_2 :",rec_user_2)