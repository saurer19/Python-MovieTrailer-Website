import media
import fresh_tomatoes

cars_2 = media.Movie("Cars 2", 
"https://upload.wikimedia.org/wikipedia/en/7/7f/Cars_2_Poster.jpg",
"https://www.youtube.com/watch?v=oFTfAdauCOo")

inside_out = media.Movie("Inside Out", 
"https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
"https://www.youtube.com/watch?v=yRUAzGQ3nSY")

good_dinosaur = media.Movie("The Good Dinosaur",
"https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg",
"https://www.youtube.com/watch?v=O-RgquKVTPE")

monsters_university = media.Movie("Monsters University",
"https://upload.wikimedia.org/wikipedia/en/2/2a/Monsters_University_poster_3.jpg",
"https://www.youtube.com/watch?v=xBzPioph8CI")

toy_story_3 = media.Movie("Toy Story 3",
"https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
"https://www.youtube.com/watch?v=JcpWXaA2qeg")

brave = media.Movie("Brave", 
"https://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg",
"https://www.youtube.com/watch?v=TEHWDA_6e3M")

movies = [cars_2, inside_out, good_dinosaur, monsters_university, toy_story_3, brave]
fresh_tomatoes.open_movies_page(movies)