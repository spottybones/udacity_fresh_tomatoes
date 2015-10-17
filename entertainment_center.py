import fresh_tomatoes
import media

monty_python_and_the_holy_grail = media.Movie(
        "Monty Python and the Holy Grail",
        "The story of King Arthur and the Knights of Camelot",
        "https://upload.wikimedia.org/wikipedia/en/4/49/Monty_python_and_the_holy_grail_2001_release_movie_poster.jpg",
        "https://www.youtube.com/watch?t=1&v=zIbx7jU35X0",
        "PG"
    )

godfather = media.Movie(
        "The Godfather",
        "This mob drama focuses on the powerful Italian-American crime family of Don Vito Corleone",
        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
        "https://www.youtube.com/watch?t=3&v=8V2k2YQEQJ4",
        "R"
    )

accidental_tourist = media.Movie(
        "The Accidental Tourist",
        "The story of a writer of travel guides for reluctant business travelers",
        "https://upload.wikimedia.org/wikipedia/en/8/8c/The_accidental_tourist.jpg",
        "https://www.youtube.com/watch?v=bQPonAjdU8g",
        "PG"
    )

mad_max_fury_road = media.Movie(
        "Mad Max: Fury Road",
        "Life in post-apocolyptic Australia",
        "https://upload.wikimedia.org/wikipedia/en/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg",
        "https://www.youtube.com/watch?t=47&v=jOZQZOVToDI",
        "R"
    )

star_wars = media.Movie(
        "Star Wars",
        "An American epic space opera",
        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
        "https://www.youtube.com/watch?t=2&v=H38MpZtujJc",
        "PG"
    )

lord_of_the_rings = media.Movie(
        "The Lord of the Rings: The Return of the King",
        "The final confrontation between the forces of good and evil fighting for control of the future of Middle-earth",
        "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
        "https://www.youtube.com/watch?t=1&v=Wmm5SNcjLvo",
        "PG-13"
)

movies = [monty_python_and_the_holy_grail, godfather, accidental_tourist,
          mad_max_fury_road, star_wars, lord_of_the_rings]
fresh_tomatoes.open_movies_page(movies)
