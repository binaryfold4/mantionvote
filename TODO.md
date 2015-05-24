## TODO

## bugs/immediate
 
  * implement sentry
  * tracks JSON should be cached and only generated every X minutes

## backend

  * improve database storage logic + submission code/throttling
    
## scraper

  * should auto run from django-cron or similar
  * don't remove data if removed from SC
  * ensure exits once all tracks processed
  * config + reports be integrated into Django admin 
   
## frontend bugs

  * optimise Datatables responsive stuff
  * fix datatables responsiveness on vote table (should see vote button on mobile)
  * workaround: fix page 'jumping' down when clicking vote on a track on mobile
  * responsiveness improved on mobile devices (esp sidebar)
  * when removing tracks, deselect from main track listing


## frontend features (suggestions, not approved)
  
  * order voted tracks by date
  * make harder to remove tracks from list, by only pushing subtract
  * (related to above) make behaviour between lists consistent; either pushing anywhere on main track except play button adds it, or do above
  * play button on voted tracks
  
  * replace alert() with nice modal
  * increment votes in main table when hitting 'save'
  * improved styling on secondary pages (profile, etc)
  * ensure still works (degrades) with JS turned off
  * improve accessibility
  * ensure design CSS is Bootstrap-ified (easier templates for other pages)

## playlists

  * implement playlist sharing + voting on playlists
  
## vote reporting
  
  * implement more interesting reports on vote/votesets
  

  
  