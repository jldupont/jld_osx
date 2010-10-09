'''
    itunes_update_playcount
    
    Reads a file with format following:
        
        # comment
        # note the 2 spaces between the fields
        $artist  $track  $playcount
        $artist  $track  $playcount
        ...
        
    Updates matching iTunes track found in library
    Outputs missing track(s) on 'stdout' following same format as above 

    Created on Oct 7, 2010

    @author: jldupont
'''
import os
import sys
import optparse

from jld_scripts.system.oparser import OParser
from jld_scripts.system.messaging import UserMessaging

from jld_osx.itunes.helpers import itunes

TIMEOUT = 30
LIBRARY_GETTRACKS_URL="http://ws.audioscrobbler.com/2.0/?method=library.gettracks&user=%s&page=%s&api_key=%s"
API_KEY="50fa3794354dd9d42fc251416f523388"

webhelp_url="http://www.systemical.com/doc/opensource/itunes_update_playcount"
sname="itunes_update_playcount"
susage="""Usage: %s [options] filepath

Updates the local iTunes library track information playcount
Updating will only occur upon specifying the '-e' option
""" % sname
soptions=[
           (["-v", "--verbose"],  {"dest":"verbose", "help":"More information to stdout",   "action":"store_true", "default":False})
           ,(["-e",  "--exec"],   {"dest":"execute", "help":"Performs the update(s)",       "action":"store_true", "default":False})         
          ,(["-w",  "--webhelp"], {"dest":"webhelp", "help":"Opens a online documentation", "action":"store_true", "default":False})
         ]

messages={ "args":        "Invalid argument(s)"
          ,"error_path":  "Invalid path specified"
          ,"error_proc":  "Processing Error: %s"
          }


def main():

    try:
        o=OParser(susage, soptions)
    except optparse.OptionError, e:
        print "# invalid option: %s" % e
        sys.exit(1)
        
    options, args=o.parse()
    um=UserMessaging(sname, False, prepend="#")
    
    if len(args) != 1:
        um.error(messages["args"])
        sys.exit(1)

    try:
        path=os.path.expanduser(args[0])
        is_file=os.path.isfile(path)
    except:
        um.error(messages["error_path"])
        sys.exit(1)

    if not is_file:
        um.error(messages["error_path"])
        sys.exit(1)

    if options.verbose:
        print "## input filepath: %s" % path
        if options.execute:
            print "## SIMULATION ONLY"

    try:
        process(path, options.execute, options.verbose)
    except Exception,e:
        um.error(messages["error_proc"] % e)
        sys.exit(1)
    
    sys.exit(0)
    
def read_input_file(path):
    try:
        file=open(path, "r")
        contents=file.read()
    except Exception,e:
        raise Exception("Access to input file failed: %s" % e)
    finally:
        try:    file.close()
        except: pass
    return contents
    
def get_fields(line):
    try:
        fields=line.split("  ")
    except:
        raise Exception("invalid line format")
    return fields
    
def validate_fields(fields):
    """
    Must have 3 fields, 2 strings and 1 integer
    """
    if len(fields) != 3:
        raise Exception("invalid line format: missing fields")
    
    try:
        _pc=int(fields[2])
    except:
        raise Exception("field 'playcount' must be an integer")
    
def findSongsByArtist(it, artist):
    songs=it.findByArtist(artist)
    return songs

def findSongsByTrackName(it, name):
    return it.findBySong(name)

def findMatch(it, songs_by_artist, songs_by_track_name):
    """
    Just need to check which song database ID matches
    in both lists
    """
    for asong in songs_by_artist:
        for tsong in songs_by_track_name:
            aid=it.getSongId(asong)
            tid=it.getSongId(tsong)
            if aid==tid:
                return asong
    return None
             
    
def process(path, execute, verbose):
    try:
        it=itunes()
    except Exception,e:
        raise Exception("Can't access iTunes: %s" % e)
            
    c=read_input_file(path)
    
    try:
        lines=c.split("\r")
    except:
        raise Exception("invalid input file format")
    
    total=0
    found=0
    
    for line in lines:
        l=line.strip(" \r\n")
        if l.startswith("#") or l=="":
            continue
        
        #if verbose:
        #    print "# processing line: %s" % l
        fields=get_fields(l)
        validate_fields(fields)
        
        artist, track, playcount=fields        
        list1=findSongsByArtist(it, unicode(artist.lower(), "utf-8"))
        list2=findSongsByTrackName(it, unicode(track.lower(), "utf-8"))
        
        total+=1
        match=findMatch(it, list1, list2)
        if match is None:
            print "%s  %s  %s" % (artist, track, playcount)
        else:
            found+=1
            if verbose:
                print "# FOUND: %s  %s  %s" % (artist, track, playcount)
 
    print "# total: %s, found: %s" % (total, found)



