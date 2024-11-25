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
    
    
movie1=Movie("The Shawshank Redemption",1994,"Frank Darabont","R","Drama","[Tim Robbins, Morgan Freeman]")
movie2=Movie("Pulp Fiction",1994,"Quentin Tarantino","R","Crime","[John Travolta, Uma Thurman, Samuel L. Jackson]")
movie3=Movie("The Godfather",1972,"Francis Ford Coppola","R","Crime","[Marlon Brando, Al Pacino, James Caan]")
movie4=Movie("Inception",2010," Christopher Nolan","PG-13","Sci-Fi","[Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page]")
movie5=Movie("The Matrix",1999,"Lana Wachowski, Lilly Wachowski","R","Sci-Fi","[Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss]")
movie6=Movie("Forrest Gump",1994,"Robert Zemeckis","PG-13","Drama"," [Tom Hanks, Robin Wright, Gary Sinise]")
movie7=Movie("The Dark Knight",2008,"Christopher Nolan","PG-13","Action"," [Christian Bale, Heath Ledger, Aaron Eckhart]")
movie8=Movie("Schindler's List",1993,"Steven Spielberg","R","Drama","[Liam Neeson, Ben Kingsley, Ralph Fiennes]")
movie9=Movie("Fight Club",1999,"David Fincher","R","Drama","[Brad Pitt, Edward Norton, Helena Bonham Carter]")
movie10=Movie("Goodfellas",1990,"Martin Scorsese","R","Crime","[Robert De Niro, Ray Liotta, Joe Pesci]")
movie11=Movie("The Silence of the Lambs",1991,"Jonathan Demme","R","Thriller","[Jodie Foster, Anthony Hopkins, Scott Glenn]")
movie12=Movie("Titanic",1997,"James Cameron","PG-13","Romance","[Leonardo DiCaprio, Kate Winslet, Billy Zane]")
movie13=Movie("The Lord of the Rings: The Fellowship of the Ring",2001,"Peter Jackson","PG-13","Fantasy","[Elijah Wood, Ian McKellen, Orlando Bloom]")
movie14=Movie("Gladiator",2000,"Ridley Scott","R","Action","[Russell Crowe, Joaquin Phoenix, Connie Nielsen]")
movie15=Movie("The Green Mile",1999,"Frank Darabont","R","Drama","[Tom Hanks, Michael Clarke Duncan, David Morse]")
movie16=Movie("Saving Private Ryan",1998,"Steven Spielberg","R","War","[Tom Hanks, Matt Damon, Tom Sizemore]")
movie17=Movie("Jurassic Park",1993,"Steven Spielberg","PG-13","Adventure","[Sam Neill, Laura Dern, Jeff Goldblum]")
movie18=Movie("The Departed",2006,"Martin Scorsese","R","Crime","[Leonardo DiCaprio, Matt Damon, Jack Nicholson]")
movie19=Movie("The Lion King",1994,"Roger Allers, Rob Minkoff","G","Animation","[Matthew Broderick, Jeremy Irons, James Earl Jones]")
movie20=Movie("Eternal Sunshine of the Spotless Mind",2004,"Michel Gondry","R","Romance","[Jim Carrey, Kate Winslet, Kirsten Dunst]")
def main():
    What_do_you_want = 0
    Movie_title_list=[movie1.title,movie2.title,movie3.title,movie4.title,movie5.title,movie6.title,movie7.title,movie8.title, movie9.title, movie10.title,movie11.title,movie12.title,movie13.title,movie14.title,movie15.title,movie16.title,movie17.title,movie18.title, movie19.title, movie20.title]
    Movie_dor_list={movie1.dor:movie1.title,movie2.dor:movie1.title,movie3.dor,movie4.dor,movie5.dor,movie6.dor,movie7.dor,movie8.dor, movie9.dor, movie10.dor,movie11.dor,movie12.dor,movie13.dor,movie14.dor,movie15.dor,movie16.dor,movie17.dor,movie18.dor, movie19.dor, movie20.dor:movie}
    Movie_list=[movie1,movie2,movie3,movie4,movie5,movie6,movie7,movie8,movie9,movie10,movie11,movie12,movie13,movie14,movie15,movie16,movie17,movie18,movie19,movie20]
    while What_do_you_want != 5:
        What_do_you_want=int(input("Do you wan't to see a movie list sorted by alphabetical order(1),chronilagical order(2),or just the plain list with all of the info of the movie(3)?(If you wan't to end the program press 5): "))
        if What_do_you_want == 1:
            Movie_title_list.sort()
            print(Movie_title_list)
        elif What_do_you_want == 2: 
            Movie_dor_list.sort()
            print(Movie_dor_list)
        elif What_do_you_want == 3: 
            for movie in Movie_list:
                print(movie)
main()