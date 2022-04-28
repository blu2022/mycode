#!/usr/bin/env python3
import requests

URL= "http://www.omdbapi.com/?apikey=875c4c78&s="

# question link: https://github.com/csfeeser/Python/blob/master/challenges/API_OMDB.md
def main():
    choice= input("Enter a movie title:\n>")

    full_url= URL + choice

    movies= requests.get(full_url).json()

    #print(movies)
    #print(full_url)

    #for loop - title
    # answer 1 and 2
    for x in movies['Search']:
        print(x['Title'])
        print(f"{x['Title']} was released in {x['Year']}")
    # answer 3
    for x in movies['Search']:
        if x['Type'] == 'movie':
            print(f"{x['Title']} was released in {x['Year']}")
    # Answer 4
    count = 0
    for x in movies['Search']:
        if x['Type'] == 'movie':
            print(f"{x['Title']} was released in {x['Year']}")

            if count == 0:
                poster_url = x['Poster']
                wget.download(poster_url, "/home/student/static/")
                print(f"Downloaded first movie poster for {x}.")
                count += 1





if __name__ == "__main__":
    main()

