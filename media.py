class Movie():
  
  def __init__(self, movie_title, poster_image, trailer_youtube):
    '''This class contains the movie-relate information.

      Atributes:
      title (str): Name of the Movie
      poster_image_url(str): URL of the image to be displayed with each movie
      trailer_youtube_url(str): URL of the video to be played 
    '''
    self.title = movie_title
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube