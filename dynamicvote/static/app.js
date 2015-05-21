$(document).ready(function() {
    
    var votetable = $('#votetracks').dataTable( {
        "bPaginate": false,
        "bFilter": false, 
        "ajax": {
            "url": "", ///rest/votes/?format=json"
            "dataSrc": ""
        },
        "columnDefs": [
            { "targets": 0, "data": "sc_id", "visible": false },
            { "targets": 1, "data": "title" }
        ]
    } );   
      
    var tracktable = $('#tracks').dataTable( {
        "aaSorting": [[0,'created_at']],
        "iDisplayLength": -1,
        "lengthMenu": [[25, 50, 100, -1], [25, 50, 100, "All"]],
        "ajax": {
            "url": "/rest/tracks/?format=json",
            "dataSrc": ""
        },
        "fnDrawCallback": function() {
           var votes = getTableId(votetable);
           markSelected(tracktable,votes);    // send this to server
        },
        "columnDefs": [
            { "targets": 0, "data": "sc_id", "visible": false },
            { "targets": 1, "data": "created_at", "render": calc_created_at },
            { "targets": 2, "data": "title" },
            { "targets": 3, "data": "duration", "render": calc_sc_duration },
            { "targets": 4, "data": "comment_count" },
            { "targets": 5, "data": "download_count" },
            { "targets": 6, "data": "playback_count" },
            { "targets": 7, "data": "favoritings_count" }
        ]
    } );
    
    function calc_created_at(data) {
        date = new Date(data);
        return date.toISOString().substring(0, 10);
    };
    
    function padDigits(number, digits) {
        return Array(Math.max(digits - String(number).length + 1, 0)).join(0) + number;
    }

    function calc_sc_duration(millis) {
        var minutes = padDigits(Math.floor(millis / 60000), 2);
        var seconds = ((millis % 60000) / 1000).toFixed(0);
        return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
    }
    
    function getTableId(table) {
        var votes = [];
        var data = table.api().column(0).data().each(function(value, index) {
            votes.push(value);
        });
        return votes;
    };  
    
    function markSelected(table,votes) {
        for (var i=0; i < votes.length; i++) {
            // iterate through main table, mark matching's id as selected        
        };   
        //console.log(table);
        //console.log(votes);
    };

    var currentStream;
    var currentTrack;
        
    $('#tracks tbody').on( 'click', 'tr', function () {
       
        var trackTitle = tracktable.fnGetData(this).title;
        var trackId = tracktable.fnGetData(this).sc_id;

        var totalVotes = 20
        
        if ( !$(this).hasClass('selected') ) {
            totalvote = votetable.fnSettings().fnRecordsTotal();
            
            if (totalvote > 20-1) {
                alert(totalVotes + " votes already reached!");
            } else {
                $(this).addClass('selected'); 
                votetable.fnAddData( { 'sc_id': trackId, 'title': trackTitle } );
                //votetable.fnAddData( [ trackId, trackTitle ]);
            };
            
        };

        if(trackId){
            if(currentTrack == trackId){
                if(currentStream.paused)
                    currentStream.resume();
                else
                    currentStream.pause();
            }
            else{
                SC.stream("/tracks/" + trackId, {
                    ontimedcomments :function(comments){
                        console.log(comments[0].body);
                  }},

                function(sound){

                    if(currentStream){
                        currentStream.destruct();
                    }
                    sound.play();
                    currentStream = sound;
                    currentTrack = trackId;
                });
            }
        }
    
    } );
    
    $('#votetracks tbody').on( 'click', 'tr', function () {  
          votetable.fnDeleteRow(this);
          // MATCHING SC_ID IN MAIN TABLE  -Class('selected');
    } );    
    
    $('#vote').click( function () {
        var votes = getTableId(votetable);
        alert(votes);    // send this to server
    } );
        
} );
