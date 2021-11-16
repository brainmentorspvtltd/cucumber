dataset = {
    "action" : ["Ironman","Thor","KGF", "Batman","Superman","Aquaman","Hulk","Baahubali",
                "Master","Avengers"],
    "comedy" : ["Thor","Golmaal","Hera Pheri", "Dhamaal", "Yes man", "The mask"],
    "sci-fi" : ["Ironman","Interstellar", "Gravity"],
    "thriller" : ["Oculus","KGF","Superman","Master","Avengers","It","Kahani"],
    "horror" : ["Oculus","It","The Nun"]
}

user = {"Ironman","Avengers","Gravity","It","The mask","Thor","Hulk","Batman","KGF"}
scores = {}

for key in dataset:
    movies = set(dataset[key])
    numer = movies.intersection(user)
    denom = movies.union(user)
    score = len(numer) / len(denom)
    # score = len(movies.intersection(user)) / len(movies.union(user))
    scores[key] = round(score,2)

print(scores)

max_value = max(scores.values())
for key in scores:
    if scores[key] == max_value:
        category = key
        break

rec_movies = set(dataset[category]) - user
print("Recommended Movies are :",rec_movies)