# Now, you’ll put it all together. 
# Don’t forget to copy all of the functions that you have previously defined into this code window. 
# Define a function get_sorted_recommendations. 
# It takes a list of movie titles as an input. 
# It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. 
# The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. 
# Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
import requests_with_caching
import json


def get_movies_from_tastedive(movie_or_music_artist_name):
    end_points = "https://tastedive.com/api/similar"      # url according to condition
    Parameters = {} # parameter dictionary
    Parameters["q"] = movie_or_music_artist_name
    Parameters["type"] = "movies"
    Parameters["limit"] = 5
    this_page_cache = requests_with_caching.get(end_points, params = Parameters) # it return a object
    return this_page_cache.json() # retun a dictionary


def extract_movie_titles(Dict):
    #print(Dict) # dictonary
    #print(Dict['Similar']) #dictionary
    #print(Dict['Similar'].keys()) # two keys : info and result
    #print(Dict['Similar']['Results'])   #list 
    #print(Dict['Similar']['Results'][0]) # above list 1st element(dictionary)
    list_of_movie_title = []
    for d in Dict['Similar']['Results']:
        list_of_movie_title.append(d['Name'])
    return list_of_movie_title
        
def get_related_titles(lst_of_movie_titles):
    lst = []
    for movie in lst_of_movie_titles:
        lst.extend(extract_movie_titles(get_movies_from_tastedive(movie))) #extend function = addition of two list
    return list(set(lst))


def get_movie_data(title_of_movie):
    endpoint = "http://www.omdbapi.com/"
    parameter = {}
    parameter["t"] = title_of_movie
    parameter["r"] = "json"
    this_page_cache = requests_with_caching.get(endpoint, params=parameter)
    return json.loads(this_page_cache.text)
    


def get_movie_rating(Dict):
    #print(Dict) #return from get_movie_data()
    #print(Dict.keys()) #find out the rating key
    #print(Dict['Ratings']) #of rating key, it is a list of dictionaries
    #print(Dict['Ratings'][0]) #first element of above list,it is a dictonary,with two keys,source and value
    for item in Dict['Ratings']:
        if item['Source'] == 'Rotten Tomatoes' :
            return int((item['Value'][:-1]))
    return 0    
    
            
def get_sorted_recommendations(lst_of_movie_title):
    new_lst = get_related_titles(lst_of_movie_title) 
    new_dict = {}
    for movie in new_lst:
        rating = get_movie_rating(get_movie_data(movie))
        new_dict[movie] = rating
    #print(new_lst) #list of movies
    #print(new_dict)#dictionary of above list with their rating
    #print(sorted(new_dict, reverse=True)) #list of movie names in reverse order of their name
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]

print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])) #lsit of decreasing order of rating of the list of reverse order of movies

