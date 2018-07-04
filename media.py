import webbrowser


class Movie():
    """The class stores information about a Movie .

        Attributes:
            title (str): Title of the Movie.
            movie_storyline (str): Story line of the movie.
            poster_image_url(obj): Url to the movie poster
            trailer_youtube_url(str): Url to movie trailer
    """

    def __init__(self, title, movie_storyline, poster_image_url, trailer_youtube_url):  # NOQA
        """ This method creates a new Movie. """
        self.title = title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """This method plays the selected movie trailer"""
        webbrowser.open(self.trailer_youtube_url)
