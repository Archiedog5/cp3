class Movie:
    def __init__(self,title,dor,dircetor,rating,genre,cast):
        self.title=title
        self.cast=cast
        self.dor=dor
        self.dircetor=dircetor
        self.genre=genre
        self.rating=rating
    def __str__(self):
        return f"Movie's title: {self.title}\nDate of realase: {self.dor}\nDirector(s): {self.dircetor}\nRating: {self.rating}\nGenre: {self.genre}\nCast: {self.cast}\nNext movie:\n"
    
    
movie1=Movie("The Shawshank Redemption",1994,"Frank Darabont","R","Drama","Tim Robbins, Morgan Freeman")
movie2=Movie("Pulp Fiction",1994,"Quentin Tarantino","R","Crime","John Travolta, Uma Thurman, Samuel L. Jackson")
movie3=Movie("The Godfather",1972,"Francis Ford Coppola","R","Crime","Marlon Brando, Al Pacino, James Caan")
movie4=Movie("Inception",2010," Christopher Nolan","PG-13","Sci-Fi","Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page")
movie5=Movie("The Matrix",1999,"Lana Wachowski, Lilly Wachowski","R","Sci-Fi","Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss")
movie6=Movie("Forrest Gump",1994,"Robert Zemeckis","PG-13","Drama","Tom Hanks, Robin Wright, Gary Sinise")
movie7=Movie("The Dark Knight",2008,"Christopher Nolan","PG-13","Action"," Christian Bale, Heath Ledger, Aaron Eckhart")
movie8=Movie("Schindler's List",1993,"Steven Spielberg","R","Drama","Liam Neeson, Ben Kingsley, Ralph Fiennes")
movie9=Movie("Fight Club",1999,"David Fincher","R","Drama","Brad Pitt, Edward Norton, Helena Bonham Carter")
movie10=Movie("Goodfellas",1990,"Martin Scorsese","R","Crime","Robert De Niro, Ray Liotta, Joe Pesci")
movie11=Movie("The Silence of the Lambs",1991,"Jonathan Demme","R","Thriller","Jodie Foster, Anthony Hopkins, Scott Glenn")
movie12=Movie("Titanic",1997,"James Cameron","PG-13","Romance","Leonardo DiCaprio, Kate Winslet, Billy Zane")
movie13=Movie("The Lord of the Rings: The Fellowship of the Ring",2001,"Peter Jackson","PG-13","Fantasy","Elijah Wood, Ian McKellen, Orlando Bloom")
movie14=Movie("Gladiator",2000,"Ridley Scott","R","Action","Russell Crowe, Joaquin Phoenix, Connie Nielsen")
movie15=Movie("The Green Mile",1999,"Frank Darabont","R","Drama","Tom Hanks, Michael Clarke Duncan, David Morse")
movie16=Movie("Saving Private Ryan",1998,"Steven Spielberg","R","War","Tom Hanks, Matt Damon, Tom Sizemore")
movie17=Movie("Jurassic Park",1993,"Steven Spielberg","PG-13","Adventure","Sam Neill, Laura Dern, Jeff Goldblum")
movie18=Movie("The Departed",2006,"Martin Scorsese","R","Crime","Leonardo DiCaprio, Matt Damon, Jack Nicholson")
movie19=Movie("The Lion King",1994,"Roger Allers, Rob Minkoff","G","Animation","Matthew Broderick, Jeremy Irons, James Earl Jones")
movie20=Movie("Eternal Sunshine of the Spotless Mind",2004,"Michel Gondry","R","Romance","Jim Carrey, Kate Winslet, Kirsten Dunst")
def main():
    What_do_you_want = 0
    Movie_title_list=[movie1.title,movie2.title,movie3.title,movie4.title,movie5.title,movie6.title,movie7.title,movie8.title, movie9.title, movie10.title,movie11.title,movie12.title,movie13.title,movie14.title,movie15.title,movie16.title,movie17.title,movie18.title, movie19.title, movie20.title]
    Movie_dor_list={movie1.dor:movie1.title,movie2.dor:movie2.title,movie3.dor:movie3.title,movie4.dor:movie4.title,movie5.dor:movie5.title,movie6.dor:movie6.title,movie7.dor:movie7.title,movie8.dor:movie8.title,movie9.dor:movie9.title,movie10.dor:movie10.title,movie11.dor:movie11.title,movie12.dor:movie12.title,movie13.dor:movie13.title,movie14.dor:movie14.title,movie15.dor:movie15.title,movie16.dor:movie16.title,movie17.dor:movie17.title,movie18.dor:movie18.title,movie19.dor:movie19.title, movie20.dor:movie20.title}
    Movie_director_list={movie1.dircetor:movie1.title,movie2.dircetor:movie2.title,movie3.dircetor:movie3.title,movie4.dircetor:movie4.title,movie5.dircetor:movie5.title,movie6.dircetor:movie6.title,movie7.dircetor:movie7.title,movie8.dircetor:movie8.title,movie9.dircetor:movie9.title,movie10.dircetor:movie10.title,movie11.dircetor:movie11.title,movie12.dircetor:movie12.title,movie13.dircetor:movie13.title,movie14.dircetor:movie14.title,movie15.dircetor:movie15.title,movie16.dircetor:movie16.title,movie17.dircetor:movie17.title,movie18.dircetor:movie18.title,movie19.dircetor:movie19.title, movie20.dircetor:movie20.title}
    Movie_list=[movie1,movie2,movie3,movie4,movie5,movie6,movie7,movie8,movie9,movie10,movie11,movie12,movie13,movie14,movie15,movie16,movie17,movie18,movie19,movie20]
    Movie_genre_list={movie1.genre:movie1.title,movie2.genre:movie2.title,movie3.genre:movie3.title,movie4.genre:movie4.title,movie5.genre:movie5.title,movie6.genre:movie6.title,movie7.genre:movie7.title,movie8.genre:movie8.title,movie9.genre:movie9.title,movie10.genre:movie10.title,movie11.genre:movie11.title,movie12.genre:movie12.title,movie13.genre:movie13.title,movie14.genre:movie14.title,movie15.genre:movie15.title,movie16.genre:movie16.title,movie17.genre:movie17.title,movie18.genre:movie18.title,movie19.genre:movie19.title, movie20.genre:movie20.title}
    Movie_cast_list={movie1.cast:movie1.title,movie2.cast:movie2.title,movie3.cast:movie3.title,movie4.cast:movie4.title,movie5.cast:movie5.title,movie6.cast:movie6.title,movie7.cast:movie7.title,movie8.cast:movie8.title,movie9.cast:movie9.title,movie10.cast:movie10.title,movie11.cast:movie11.title,movie12.cast:movie12.title,movie13.cast:movie13.title,movie14.cast:movie14.title,movie15.cast:movie15.title,movie16.cast:movie16.title,movie17.cast:movie17.title,movie18.cast:movie18.title,movie19.cast:movie19.title, movie20.cast:movie20.title}
    while What_do_you_want != 7:
        What_do_you_want=int(input("Do you wan't to see a movie list sorted by alphabetical order(1),chronilagical order(2),or just the plain list with all of the info of the movie(3)? If none of those do you want to search for a movie by director(4), genre(5), or cast(6)?(If you wan't to end the program press 7): "))
        if What_do_you_want == 1:
            Movie_title_list.sort()
            print(Movie_title_list)
        elif What_do_you_want == 2: 
            myKeys = list(Movie_dor_list.keys())
            myKeys.sort()
            sd = {i: Movie_dor_list[i] for i in myKeys}
            print(sd)
        elif What_do_you_want == 3: 
            for movie in Movie_list:
                print(movie)
        elif What_do_you_want == 4:
            question= input("What directors work do you want to watch: ")
            Director_work=[]
            i=0
            for movie in Movie_list:
                if question in movie.dircetor:
                    Director_work.append(Movie_list[i])
                i+=1
            if Director_work == []:
                print("There are no movies by that director on the list")
            else:
                print("Here is all of the work from that director in this data base:")
                for movie in Director_work:
                    print(movie)
        elif What_do_you_want == 5:
            question= input("What genre do you want to watch?: ")
            if question in Movie_genre_list.keys():
                print("Here is one movie in that genre\n"+Movie_genre_list[question])
            else:
                print("There is no movie in that genre.")
        elif What_do_you_want == 6:
            question= input("What cast members do you want to watch?: ")
            if question in Movie_cast_list.keys():
                print("Here is one movie with those cast mebers\n"+Movie_cast_list[question])
            else:
                print("There is no movie with that cast.")

main()