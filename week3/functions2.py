def is_movie55(name, movies):
    for i in movies:
        if(i['name'] == name and i['imdb'] > 5.5):
            return True
    return False

def all_movies55(movies):
    movies55 = []
    for i in movies:
        if(i['imdb'] > 5.5):
            movies55.append(i['name'])
    return movies55

def movies_by_categ(category, movies):
    mov_in_categ = []
    for i in movies:
        if(i['category'] == category):
            mov_in_categ.append(i['name'])
    return mov_in_categ

def av_by_names(names, movies):
    sum = 0
    cnt = 0
    for i in movies:
        if i['name'] in names:
            cnt += 1
            sum += i['imdb']
    return (sum / cnt)

def av_by_cat(category, movies):
    sum = 0
    cnt = 0
    for i in movies:
        if(i['category'] == category):
            sum += i['imdb']
            cnt += 1
    return (sum / cnt)

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
movie_name = input('Check if movie imdb is above 5.5 by name:')
higher55 = is_movie55(movie_name, movies)
print(higher55)

#2
movies_higher55 = all_movies55(movies)
for i in movies_higher55:
    print(i, end= '   ')
print('\n')

#3
category = input('Get list of movies in category:')
mov_in_cat = movies_by_categ(category, movies)
print(category, 'movies: ', end= '')
for i in mov_in_cat:
    print(i, end= "   ")
print('\n')

#4
list_mov = input('Write movies to get average imdb:').split(',')
average4 = av_by_names(list_mov, movies)
print('Average = ', average4)

#5
cat_for_av = input('Get average imdb in category:')
average5 = av_by_cat(cat_for_av, movies)
print('Average = ', average5)
