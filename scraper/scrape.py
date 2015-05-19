import soundcloud
import json
import pprint

# TODO:
#  * ensure exists upon no extra data (currently need to ctrl-c)
#  * grab extra data (stream URL, etc) 

clientID="1d64d5728db6fd2bf52b77c57a47fc91"
URL="http://soundcloud.com/user18081971"
FILE="user18081971.json"
LIMIT = 50
OFFSET = 1

alltracks = []
TRACKCOUNT = 0

client = soundcloud.Client(client_id=clientID)

#user = client.get('/resolve', url='http://soundcloud.com/user18081971')
userid = 122922135 #user.id

def AppendTrack(alltracks, track):
    global TRACKCOUNT
    TRACKCOUNT = TRACKCOUNT + 1
    print("%s %s" % (TRACKCOUNT, track.id))
    
    try:
        commentcount = track.comment_count
    except:
        commentcount = '0'  
    try:
        downloadcount = track.download_count 
    except:
        downloadcount = '0' 
    try:
        playbackcount = track.playback_count
    except:
        playbackcount = '0'
    try:
        favoritingscount = track.favoritings_count
    except:
        favoritingscount = '0'
    
    alltracks.append({
        'id': track.id,
        'created_at': track.created_at,
        'title': track.title,
        'comment_count': commentcount,
        'download_count': downloadcount,
        'playback_count': playbackcount,
        'favoritings_count': favoritingscount
    })

tracks = client.get('/users/%d/tracks' %userid, order='created_at', limit=LIMIT)

while True:
    try:
        tracks = client.get('/users/%d/tracks' %userid, order='created_at', limit=LIMIT, offset=OFFSET*LIMIT-LIMIT)   #linked_partitioning=1)
        OFFSET=OFFSET+1
        for track in tracks:
            AppendTrack(alltracks, track)
    except:
        print("ERROR with %s" % (track.id))
        break

#pprint.pprint(alltracks)
finalfile = {'tracks':alltracks}

with open(FILE, 'w') as outfile:
    json.dump(finalfile, outfile)
    print("written out %s" % (FILE))


