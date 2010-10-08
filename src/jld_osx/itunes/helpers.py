"""
    iTunes helpers
        
    Created on 2010-10-07
    @author: jldupont
"""
import appscript

class itunes(object):
    """
    Helper class for itunes
    """
    def __init__(self):
        self.it=appscript.app("itunes")
        self.lib=self.it.playlists["Library"]

    def findByArtist(self, artist):
        list=self.it.search(self.lib, for_=artist, only=appscript.k.artists)
        return list
    
    def findBySong(self, song):
        list=self.it.search(self.lib, for_=song, only=appscript.k.songs)
        return list
        
    ############################################################################ SONG RELATED
        
    def setSongPlaycount(self, item, playcount):
        item.set(item.play_count, to=playcount)
        
    def getSongName(self, item):
        return item.name()
    
    def getSongArtist(self, item):
        return item.artist()
    
    def getSongPlaycount(self, item):
        return item.played_count()
    
if __name__=="__main__":
    i=itunes()
    list=i.findByArtist("Xandria")
    for item in list:
        print i.getSongName(item)
        
    
    