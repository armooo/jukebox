class Song(object):
    def __init__(self, title, album, artist, path):
        self.pk = None
        self.title = title
        self.album = album
        self.artist = artist
        self.path = path