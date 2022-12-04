import requests
key = 'k_m28t7fwl'

class ImdbRequest:
    _base_url = "https://imdb-api.com/en/API/"
        
    @classmethod
    def get_titles(cls, movie_title):
        url = cls._base_url+"SearchMovie/"+key+"/"+movie_title
        print("url :", url)
        return requests.get(url)

    def get_rating(id):
        url = "https://imdb-api.com/en/API/Ratings/"+key+"/"+id
        print(url)
        return requests.get(url)
    
    def get_user_rating(id):
        url = "https://imdb-api.com/en/API/UserRatings/"+key+"/"+id
        return requests.get(url)

