class movie:
    def __init__(self,title,dor,dircetor,rating,genre,cast):
        self.title=title
        self.cast=cast
        self.dor=dor
        self.dircetor=dircetor
        self.genre=genre
        self.rating=rating
    def __str__(self):
        return f"Movie's title: {self.title}\nDate of realase: {self.dor}\nDirector(s): {self.dircetor}\nRating: {self.rating}\nGenre: {self.genre}\nCast: {self.cast}"
    
    def __tsort__(self):
        return tarr.sort()

movie1=movie("The Shawshank Redemption",1994,"Frank Darabont","R","Drama","[Tim Robbins, Morgan Freeman]")
movie2=movie("Pulp Fiction",1994,"Quentin Tarantino","R","Crime","[John Travolta, Uma Thurman, Samuel L. Jackson]")
movie3=movie("The Godfather",1972,"Francis Ford Coppola","R","Crime","[Marlon Brando, Al Pacino, James Caan]")
movie4=movie("Inception",2010," Christopher Nolan","PG-13","Sci-Fi","[Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page]")
movie5=movie("The Matrix",1999,"Lana Wachowski, Lilly Wachowski","R","Sci-Fi","[Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss]")
movie6=movie("Forrest Gump",1994,"Robert Zemeckis","PG-13","Drama"," [Tom Hanks, Robin Wright, Gary Sinise]")
movie7=movie("The Dark Knight",2008,"Christopher Nolan","PG-13","Action"," [Christian Bale, Heath Ledger, Aaron Eckhart]")
movie8=movie("Schindler's List",1993,"Steven Spielberg","R","Drama","[Liam Neeson, Ben Kingsley, Ralph Fiennes]")
movie9=movie("Fight Club",1999,"David Fincher","R","Drama","[Brad Pitt, Edward Norton, Helena Bonham Carter]")
movie10=movie("Goodfellas",1990,"Martin Scorsese","R","Crime","[Robert De Niro, Ray Liotta, Joe Pesci]")
movie11=movie("The Silence of the Lambs",1991,"Jonathan Demme","R","Thriller","[Jodie Foster, Anthony Hopkins, Scott Glenn]")
movie12=movie("Titanic",1997,"James Cameron","PG-13","Romance","[Leonardo DiCaprio, Kate Winslet, Billy Zane]")
movie13=movie("The Lord of the Rings: The Fellowship of the Ring",2001,"Peter Jackson","PG-13","Fantasy","[Elijah Wood, Ian McKellen, Orlando Bloom]")
movie14=movie("Gladiator",2000,"Ridley Scott","R","Action","[Russell Crowe, Joaquin Phoenix, Connie Nielsen]")
movie15=movie("The Green Mile",1999,"Frank Darabont","R","Drama","[Tom Hanks, Michael Clarke Duncan, David Morse]")
movie16=movie("Saving Private Ryan",1998,"Steven Spielberg","R","War","[Tom Hanks, Matt Damon, Tom Sizemore]")
movie17=movie("Jurassic Park",1993,"Steven Spielberg","PG-13","Adventure","[Sam Neill, Laura Dern, Jeff Goldblum]")
movie18=movie("The Departed",2006,"Martin Scorsese","R","Crime","[Leonardo DiCaprio, Matt Damon, Jack Nicholson]")
movie19=movie("The Lion King",1994,"Roger Allers, Rob Minkoff","G","Animation","[Matthew Broderick, Jeremy Irons, James Earl Jones]")
movie20=movie("Eternal Sunshine of the Spotless Mind",2004,"Michel Gondry","R","Romance","[Jim Carrey, Kate Winslet, Kirsten Dunst]")
tarr = [movie1.title,movie2.title,movie3.title,movie4.title,movie5.title,movie6.title,movie7.title,movie8.title,movie9.title,movie10.title,movie11.title,movie12.title,movie13.title,movie14.title,movie15.title,movie16.title,movie17.title,movie18.title,movie19.title,movie20.title]
print(tarr)