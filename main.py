import pandas as pd
from request import ImdbRequest

movie_title = input("movie title : ")


# For loop does the request and append them in the dataframe.

df= []
titles = ImdbRequest.get_titles(movie_title).json()
for title in titles['results']:
    id = title['id']
    rating = ImdbRequest.get_rating(id).json()
    user_rating = ImdbRequest.get_user_rating(id).json()

    df.append(
        {
            'title': title['title'],
            'imDb rating': rating['imDb'],
            'rottenTomatoes rating': rating['rottenTomatoes'],
            'metacritic rating': rating['metacritic'],
            'theMovieDb': rating['theMovieDb']

        }
    )
    #print(title['title'])
    #print("imDb :", rating['imDb'])

df = pd.DataFrame(df)
print(df.head(10))