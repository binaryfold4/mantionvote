## TODO

  * [1] immmediate
  * [2] asap
  * [3] later
  * [W] wishlist

## bugs/immediate
 
  * [1] SC accounts with non-alphanumberic unicode characters are causing error: fix
  * [1] implement sentry / new relic (to measure)
  * [3] tracks JSON should be cached and only generated every X minutes (measure, improve, repeat)


## backend

  * [2] order voted tracks by date voted
  * [2] add FAQ page, move some information in Profile there, cover all common questions
  * [2] ensure Profile page displays existing email if it's already filled out
  * [2] redirect to Profile page only for new user
  * [3] improve database storage logic + submission code/throttling (measure, improve, repeat)

    
## scraper

  * [2] should auto run from django-cron or similar
  * [2] don't remove data if removed from SC
  * [2] ensure exits once all tracks processed
  * [W] config + reports be integrated into Django admin 
   
   
## frontend bugs

  * [1] fix favicons
  * [1] fix datatables responsiveness on vote table (should see vote button on mobile)
  * [2] responsiveness improved on mobile devices (esp sidebar)
  * [2] workaround: fix page 'jumping' down when clicking vote on a track on mobile
  * [3] optimise Datatables; slowed down after adding responsiveness



## frontend features (suggestions, not approved)
  
  * [2] improved styling on secondary pages (profile, etc)

  * [W] make harder to remove tracks from list, by only pushing subtract
  * [W] (related to above) make behaviour between lists consistent; either pushing anywhere on main track except play button adds it, or do above
  * [W] play button on voted tracks - perhaps play all of these in a loop
  
  * [W] ability to seek soundcloud tracks   
  * [W] replace alert() with nice modal
  * [W] increment votes in main table when hitting 'save'
  * [W] ensure still works (degrades) with JS turned off
  * [W] improve accessibility
  * [W] ensure design CSS is Bootstrap-ified (easier templates for other pages)


## playlists

  * [2] implement playlist sharing + voting on playlists
  * [W] extend above, allow for comments on playlists, grouping of playlists, stats showing coverage of full tracks, etc

  
## vote reporting
  
  * [W] implement more interesting reports on vote/votesets
  

  
  