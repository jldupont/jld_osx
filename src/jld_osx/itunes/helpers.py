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
        item.set(item.played_count, to=playcount)
        
    def getSongName(self, item):
        return item.name()
    
    def getSongArtist(self, item):
        return item.artist()
    
    def getSongPlaycount(self, item):
        return item.played_count()
    
    def getSongId(self, item):
        return item.database_ID()
        
if __name__=="__main__":
    i=itunes()
    list=i.findByArtist("Xandria")
    for item in list:
        a=i.getSongArtist(item)
        id=i.getSongId(item)
        t=i.getSongName(item)
        print "id(%s) artist: %s, track: %s" % (id, a, t)
        
    
    