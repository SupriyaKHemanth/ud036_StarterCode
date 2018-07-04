import fresh_tomatoes
import media

# Create instances of movie Class
karwaan = media.Movie("Karwaan", "A crazy journey of 3 lost souls", "https://s3.ap-southeast-1.amazonaws.com/images.deccanchronicle.com/dc-Cover-dc75ho6r318bokao0re6v3tu55-20180514181104.Medi.jpeg", "https://www.youtube.com/watch?v=IUCeN7kelXs")  # NOQA

ratatouille = media.Movie("Ratatouille", "A story of rat", "https://vignette.wikia.nocookie.net/disney/images/1/1d/Ratatouille_Pixar.jpg/revision/latest?cb=20120626221759", "https://www.youtube.com/watch?v=ALUmKa_mpik")  # NOQA

insideout = media.Movie("Inside Out", "A story of a girl", "https://en.wikipedia.org/wiki/File:Inside_Out_(2015_film)_poster.jpg", "https://www.youtube.com/watch?v=seMwpP0yeu4")  # NOQA

howtotrainyourdragon3 = media.Movie("HOW TO TRAIN YOUR DRAGON 3", "A story of a boy and dragon", "http://cdn-static.denofgeek.com/sites/denofgeek/files/styles/main_wide/public/how-to-train-your-dragon-2-2014_27.jpeg", "https://www.youtube.com/watch?v=naW9U8MiUY0")  # NOQA

movies = [karwaan, ratatouille, insideout, howtotrainyourdragon3]

# Takes list of movie objects and creates a template and loads into browser page # NOQA
fresh_tomatoes.open_movies_page(movies)
