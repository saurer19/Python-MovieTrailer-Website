import media
import fresh_tomatoes
'''
 Instatiate 6 Movie objects with
  the names, poster URLs and trailer URLs
'''
cars_2 = media.Movie("Cars 2",
  "https://upload.wikimedia.org/wikipedia/en/7/7f/"  # NOQA
  "Cars_2_Poster.jpg",
  "https://www.youtube.com/watch?v=oFTfAdauCOo")

inside_out = media.Movie("Inside Out",
  "https://upload.wikimedia.org/wikipedia/en/0/0a/"  # NOQA
  "Inside_Out_%282015_film%29_poster.jpg",
  "https://www.youtube.com/watch?v=yRUAzGQ3nSY")

good_dinosaur = media.Movie("The Good Dinosaur",
  "https://upload.wikimedia.org/wikipedia/en/8/80/"  # NOQA
  "The_Good_Dinosaur_poster.jpg",
  "https://www.youtube.com/watch?v=O-RgquKVTPE")

monsters_uni = media.Movie("Monsters University",
  "https://upload.wikimedia.org/wikipedia/en/2/2a/"  # NOQA
  "Monsters_University_poster_3.jpg",
  "https://www.youtube.com/watch?v=xBzPioph8CI")

toy_story_3 = media.Movie("Toy Story 3",
  "https://upload.wikimedia.org/wikipedia/en/6/69/"  # NOQA
  "Toy_Story_3_poster.jpg",
  "https://www.youtube.com/watch?v=JcpWXaA2qeg")

brave = media.Movie("Brave",
"https://upload.wikimedia.org/wikipedia/en/9/96/"  # NOQA
"Brave_Poster.jpg",
"https://www.youtube.com/watch?v=TEHWDA_6e3M")

# Store the Movie objects in a list.
movies = [
  cars_2,
  inside_out,
  good_dinosaur,
  monsters_uni,
  toy_story_3,
  brave
  ]

# Open the movie trailer website in the browser
fresh_tomatoes.open_movies_page(movies)
