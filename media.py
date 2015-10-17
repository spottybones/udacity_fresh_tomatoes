import webbrowser

class Movie():
    """Provides Storage for Movie Information.

    This class stores information about a motion picture.

    Attributes:
        title: The movie's title
        storyline: A very brief description of the movie_title
        poster_image_url: The URL of an image of the movie's poster_image
        trailer_youtube_url: The Youtube URL of the movie's trailer
        rating: The MPAA assigned movie rating

    Returns:
        An instance of class Movie
    """

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url, rating):
        """Initialize class instance with movie metadata."""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.rating = rating

    def show_trailer(self):
        """Open a web browser window with the Movie Trailer YouTube URL"""
        webbrowser.open(self.trailer_youtube_url)
