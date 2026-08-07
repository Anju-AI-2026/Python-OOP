# Movie Rating Class using Computed Property

class MovieRating:
    # Constructor to initialize movie details
    def __init__(self, movie_name, story, acting, music):
        self.movie_name = movie_name
        self.story = story
        self.acting = acting
        self.music = music

    # Computed property to calculate average rating
    @property
    def average_rating(self):
        return (self.story + self.acting + self.music) / 3

    # Computed property to decide movie result
    @property
    def result(self):
        if self.average_rating >= 8:
            return "Blockbuster"
        elif self.average_rating >= 6:
            return "Hit"
        else:
            return "Average"

    # Display movie details
    def show_details(self):
        print(f"Movie : {self.movie_name}")
        print(f"Story Rating : {self.story}")
        print(f"Acting Rating : {self.acting}")
        print(f"Music Rating : {self.music}")
        print(f"Average Rating : {self.average_rating:.2f}")
        print(f"Result : {self.result}")


# Creating object
movie = MovieRating("Galactic Adventure", 9, 8, 7)

# Display movie details
movie.show_details()
