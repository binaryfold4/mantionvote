$(document).ready(function() {

    $.fn.dataTable.ext.errMode = 'throw';

    var votetable = $('#votetracks').dataTable( {
        "bPaginate": false,
        "bFilter": false, 
        "ajax": {
            "url": "/api/vote/?format=json",
            "dataSrc": ""
        },
        "oLanguage": {
            "sEmptyTable":     "No tracks selected"
        },
        "columnDefs": [
            { "targets": 0, "data": "track.sc_id", "visible": false },
            { "targets": 1, "data": "track.title" }
        ]
    } );   
      
    var tracktable = $('#tracks').dataTable( {
        "aaSorting": [[0,'created_at']],
        "iDisplayLength": -1,
        "lengthMenu": [[25, 50, 100, -1], [25, 50, 100, "All"]],
        "ajax": {
            "url": "/api/tracks/?format=json",
            "dataSrc": ""
        },
        "fnDrawCallback": function() {
           var votes = getTableId(votetable);
           markSelected(tracktable,votes);    // send this to server

            var api = this.api();
            var rows = api.rows( {page:'current'} ).nodes();
            var last=null;

            api.column(0, {page:'current'} ).data().each( function ( sc_id, i ) {
                $(rows).eq( i ).after(
                    '<tr class="trackWidgetRow">'
                    +'<td colspan="6">'
                    +'<div class="waveformContainer"></div>'
                    +'<div class="trackArt"></div>'
                    +'</td>'
                    +'</tr>'
                );
            });
        },
        "columnDefs": [
            { "targets": 0, "data": "sc_id", "visible": false },
            { "targets": 1, "className": "title", "data": "title" },
            { "targets": 2, "data": "duration", "render": calc_sc_duration },
            { "targets": 3, "data": "uploaded_at", "render": calc_created_at },
            { "targets": 4, "data": "playback_count", "render": nullify },
            { "targets": 5, "data": "comment_count", "render": nullify },
            { "targets": 6, "data": "favoritings_count", "render": nullify },
            { "targets": 7, "data": null, "orderable": false, defaultContent: '' }
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

    function nullify(number) {
        if (number == 0) {
            return "";
        } else {
            return number;
        }
    }
    
    function getTableId(table) {
        var votes = {};
        var i=0;
        var data = table.api().column(0).data().each(function(value, index) {
            i++;
            votes["vote" + i] = value;
        });
        return votes;
    };  
    
    function markSelected(table,votes) {
        for (var i=0; i < votes.length; i++) {
            alert(votes[i]);
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
        var trackWaveform = tracktable.fnGetData(this).waveform_url;

        var waveFormRow = $(this).next('tr');

        $('.trackWidgetRow').not(this).removeClass('playing');
        $(waveFormRow).addClass('playing');

        var totalVotes = 20
        
        if ( !$(this).hasClass('selected') ) {
            totalvote = votetable.fnSettings().fnRecordsTotal();
            
            if (totalvote > totalVotes-1) {
                alert(totalVotes + " votes already reached!");
            } else {
                $(this).addClass('selected'); 
                votetable.fnAddData( { track: { 'sc_id': trackId, 'title': trackTitle } } );
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
                var track = {
                    waveform_url: trackWaveform,
                    uri : '/tracks/'+trackId
                };

                var waveform = new Waveform({
                    container: $(waveFormRow).find('div.waveformContainer')[0],
                    innerColor: '#fff',
                    outerColor: '#310520',
                    playedColor: '#f50'
                });

                waveform.dataFromSoundCloudTrack(track);
                var streamOptions = waveform.optionsForSyncedStream({
                    loadedColor: '#fff',
                    playedColor: '#f50'
                });

//                    streamOptions.ontimedcomments = function(comments){
////                            console.log(comments);
//                    };

                SC.stream(track.uri, streamOptions, function(stream){
                    if(currentStream){
                        currentStream.destruct();
                    }
                    stream.play();
                    currentStream = stream;
                    currentTrack = trackId;
                });

            }
        }
    
    } );
    
    $('#votetracks tbody').on( 'click', 'tr', function () {  
          votetable.fnDeleteRow(this);
          // MATCHING SC_ID IN MAIN TABLE  -Class('selected');
    } );    

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    $('#vote').click( function () {

        var minVotes = 5;

        totalvote = votetable.fnSettings().fnRecordsTotal();
        if (totalvote < minVotes) {
            alert("At least " + minVotes + " votes are required");
        } else {
            var votes = getTableId(votetable);
            console.log(votes);

            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            $.ajax({

                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                },

                url : "/myvote/",
                type: "POST",
                data: votes,

                success: function(json) {
                    console.log("success");
                    $("#status").text(json);
                },

                error: function(xhr,errmsg,err) {
                    console.log("failure");
                    console.log(xhr.status + ": " + xhr.responseText);
                    $("#status").text(err);
                }
            })


        };

    } );
        
} );
