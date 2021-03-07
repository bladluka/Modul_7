library_list = []

class Movies:


    def __init__(self, title, year, type):
        self.title = title
        self.year = year
        self.type = type
        self.no_plays = 0
        library_list.append(self)

    def play(self, step=1):
        no_plays += step

    def __str__(self):
        return f"{self.title} {self.year}"

    def __repr__(self):
        return f"{self.title} {self.year}"



movie1 = Movies(title="The Producers", year="1968", type="comedy")
movie2 = Movies(title="The Bourne Identity", year="2002", type="thriller")
movie3 = Movies(title="The Duck Soup", year="1933", type="comedy")
movie4 = Movies(title="M.A.S.H", year="1970", type="comedy")
movie5 = Movies(title="Harry Potter and the Order of the Phoenix", year="2007", type="Fantasy")
movie6 = Movies(title="Life of Brian", year="1979", type="comedy")
movie7 = Movies(title="The Terminator", year="1984", type="Sci-Fi")
movie8 = Movies(title="Stargate ", year="1994", type="Sci-Fi")
movie9 = Movies(title="Flatliners", year="1990", type="Sci-fi")
movie10 = Movies(title="Die Hard", year="1988", type="thriller")


class Series(Movies):

    def __init__(self, no_episode, no_season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.no_episode = no_episode
        self.no_season = no_season

    def play(self, step=1):
        no_plays += step

    def __str__(self):
        return f"{self.title} S{self.no_season}E{self.no_episode}"

    def __repr__(self):
        return f"{self.title} S{self.no_season}E{self.no_episode}"


series1 = Series(title="House M.D.", year="2004 - 2007", type="drama", no_episode=1, no_season=1)
series2 = Series(title="Doctor Who", year="1963 - 2020 ", type="Sci-Fi", no_episode=1, no_season=1)
series3 = Series(title="The Big Bang Theory ", year="2007 - 2019 ", type="comedy", no_episode=1, no_season=1)
series4 = Series(title="M.A.S.H.", year="1972 - 1983", type="comedy", no_episode=1, no_season=1)
series5 = Series(title="Stargate SG-1", year="1997 - 2007 ", type="sci-Fi", no_episode=1, no_season=1)
series6 = Series(title="Buffy the Vampire Slayer", year="1997 - 2003", type="fantasy", no_episode=1, no_season=1)
series7 = Series(title="Scrubs", year="2001 - 2010", type="comedy", no_episode=1, no_season=1)
series8 = Series(title="Fawlty Towers", year="1979", type="comedy", no_episode=1, no_season=1)
series9 = Series(title="McGyver", year="1985 - 1992", type="thriller", no_episode=1, no_season=1)
series10 = Series(title="Miami Vice", year="1984 - 1990", type="criminal", no_episode=1, no_season=1)





def movies_list():
    movies = []
    for position in library_list:
        if type(position) == Movies:
            movies.append(position)
    return movies

def search(title):
    movies = []
    for position in library_list:
        if title == position.title:
            return position

#movies_list = get_movies()
#print(movies_list)

movies = movies_list()
#for number in movies_list():
 #   print(number)

titles = search('Scrubs')
print(titles)

