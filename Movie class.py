class Movie:
    def __init__(self,title,dor,dircetor,rating,genre,cast):
        self.title=title
        self.cast=cast
        self.dor=dor
        self.dircetor=dircetor
        self.genre=genre
        self.rating=rating
        self.movie_title_list=[]
        self.movie_dor_list=[]
    def __str__(self):
        return f"Movie's title: {self.title}\nDate of realase: {self.dor}\nDirector(s): {self.dircetor}\nRating: {self.rating}\nGenre: {self.genre}\nCast: {self.cast}"
    
    def tarr(self,movie):
        self.movie_title_list.append(movie.title)

    
    def __tsort__(self):
        print(movie_title_list.sort())
    
movie1=Movie()
movie1=Movie("The Shawshank Redemption",1994,"Frank Darabont","R","Drama","[Tim Robbins, Morgan Freeman]"))
movie2=Movie("Pulp Fiction",1994,"Quentin Tarantino","R","Crime","[John Travolta, Uma Thurman, Samuel L. Jackson]"))
movie1=Movie("The Godfather",1972,"Francis Ford Coppola","R","Crime","[Marlon Brando, Al Pacino, James Caan]"))
movie1=Movie("Inception",2010," Christopher Nolan","PG-13","Sci-Fi","[Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page]"))
movie1=Movie("The Matrix",1999,"Lana Wachowski, Lilly Wachowski","R","Sci-Fi","[Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss]"))
movie1=Movie("Forrest Gump",1994,"Robert Zemeckis","PG-13","Drama"," [Tom Hanks, Robin Wright, Gary Sinise]"))
movie1=Movie("The Dark Knight",2008,"Christopher Nolan","PG-13","Action"," [Christian Bale, Heath Ledger, Aaron Eckhart]"))
movie1=Movie("Schindler's List",1993,"Steven Spielberg","R","Drama","[Liam Neeson, Ben Kingsley, Ralph Fiennes]"))
movie1=Movie("Fight Club",1999,"David Fincher","R","Drama","[Brad Pitt, Edward Norton, Helena Bonham Carter]"))
movie1=Movie("Goodfellas",1990,"Martin Scorsese","R","Crime","[Robert De Niro, Ray Liotta, Joe Pesci]"))
movie1=Movie("The Silence of the Lambs",1991,"Jonathan Demme","R","Thriller","[Jodie Foster, Anthony Hopkins, Scott Glenn]"))
movie1=Movie("Titanic",1997,"James Cameron","PG-13","Romance","[Leonardo DiCaprio, Kate Winslet, Billy Zane]"))
movie1=Movie("The Lord of the Rings: The Fellowship of the Ring",2001,"Peter Jackson","PG-13","Fantasy","[Elijah Wood, Ian McKellen, Orlando Bloom]"))
movie1=Movie("Gladiator",2000,"Ridley Scott","R","Action","[Russell Crowe, Joaquin Phoenix, Connie Nielsen]"))
movie1=Movie("The Green Mile",1999,"Frank Darabont","R","Drama","[Tom Hanks, Michael Clarke Duncan, David Morse]"))
movie1=Movie("Saving Private Ryan",1998,"Steven Spielberg","R","War","[Tom Hanks, Matt Damon, Tom Sizemore]"))
movie1=Movie("Jurassic Park",1993,"Steven Spielberg","PG-13","Adventure","[Sam Neill, Laura Dern, Jeff Goldblum]"))
movie1=Movie("The Departed",2006,"Martin Scorsese","R","Crime","[Leonardo DiCaprio, Matt Damon, Jack Nicholson]"))
movie1=Movie("The Lion King",1994,"Roger Allers, Rob Minkoff","G","Animation","[Matthew Broderick, Jeremy Irons, James Earl Jones]"))
movie1=Movie("Eternal Sunshine of the Spotless Mind",2004,"Michel Gondry","R","Romance","[Jim Carrey, Kate Winslet, Kirsten Dunst]"))
