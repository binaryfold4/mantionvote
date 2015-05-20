from django.core.management.base import BaseCommand, CommandError
from dynamicvote.models import Track
import soundcloud

# TODO:
#  * ensure exists upon no extra data (currently need to ctrl-c)
#  * grab extra data (stream URL, etc) 

TRACKCOUNT = 0

class Command(BaseCommand):
    args = ''
    help = 'Grabs latest data from SoundCloud'

    def handle(self, *args, **options):

        SC_USERNAME="user18081971"
        LIMIT = 50
        OFFSET = 1

        clientID="1d64d5728db6fd2bf52b77c57a47fc91"
        URL="http://soundcloud.com/" + SC_USERNAME
        FILE="../frontend-old/" + SC_USERNAME + ".json"

        alltracks = []


        client = soundcloud.Client(client_id=clientID)

        #user = client.get('/resolve', url=URL)
        userid = 122922135 # or user.id - locking this down as rdj keeps changing username

        def AppendTrack(alltracks, track, Track):
            global TRACKCOUNT
            TRACKCOUNT = TRACKCOUNT + 1

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
            try:
                downloadurl = track.download_url
            except:
                downloadurl = None

            t, created = Track.objects.get_or_create(sc_id = track.id)
            print("%s: (NEW: %s) %s %s" % (TRACKCOUNT, created, track.id, track.title))

            t.sc_id = track.id
            t.uploaded_at = track.created_at
            t.title = track.title
            t.description = track.description
            t.tag_list = track.tag_list
            t.duration = track.duration
            t.comment_count = commentcount
            t.download_count = downloadcount
            t.playback_count = playbackcount
            t.favoritings_count = favoritingscount
            t.stream_url = track.stream_url
            t.download_url = downloadurl
            t.permalink_url = track.permalink_url

            t.save()

        tracks = client.get('/users/%d/tracks' %userid, order='created_at', limit=LIMIT)

        while True:
            tracks = client.get('/users/%d/tracks' %userid, order='created_at', limit=LIMIT, offset=OFFSET*LIMIT-LIMIT)   #linked_partitioning=1)
            OFFSET=OFFSET+1
            for track in tracks:
                AppendTrack(alltracks, track, Track)
            #except:
            #    print("ERROR with %s" % (track.id))
            #    break

        #pprint.pprint(alltracks)
        #finalfile = {'tracks':alltracks}

        #with open(FILE, 'w') as outfile:
        #    json.dump(finalfile, outfile)
        #    print("written out %s" % (FILE))




