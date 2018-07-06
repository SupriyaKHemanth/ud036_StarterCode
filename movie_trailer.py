import fresh_tomatoes
import media

# Create instances of movie Class
karwaan = media.Movie("Karwaan",
                      "A crazy journey of 3 lost souls",
                      "https://bit.ly/2lYA2P1",
                      "https://www.youtube.com/watch?v=IUCeN7kelXs")

ratatouille = media.Movie("Ratatouille",
                          "A story of rat",
                          "https://bit.ly/2NuRZkE",
                          "https://www.youtube.com/watch?v=ALUmKa_mpik")

insideout = media.Movie("Inside Out",
                        "A story of a girl",
                        "https://bit.ly/2KRr6sD",
                        "https://www.youtube.com/watch?v=seMwpP0yeu4")

howtotrainyourdragon3 = media.Movie("HOW TO TRAIN YOUR DRAGON 3",
                                    "A story of a boy and dragon",
                                    "https://bit.ly/2KSplbs",
                                    "https://www.youtube.com/watch?v=naW9U8MiUY0")  # NOQA

movies = [karwaan, ratatouille, insideout, howtotrainyourdragon3]

# Takes list of movie objects and creates a template and loads into browser page # NOQA
fresh_tomatoes.open_movies_page(movies)
