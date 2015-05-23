$(document).ready(function() {

    $.fn.dataTable.ext.errMode = 'throw';

    var tracktable = $('#tracks').dataTable( {
        "order": [[ 3, "desc" ]],
        //"iDisplayLength": -1,
        //"lengthMenu": [[25, 50, 100, -1], [25, 50, 100, "All"]],
        "bPaginate": false,
        "ajax": {
            "url": "/api/tracks/?format=json",
            "dataSrc": ""
        },
        "language": {
            search: "_INPUT_",
            searchPlaceholder: "Type here to search tracks"
        },
        "infoCallback": function( settings, start, end, max, total, pre ) {
            if(max)
                $('p.numTracks').html(max + ' tracks');

            var length = 0;
            this.api().column(2).data().each( function(duration, i){
                length += duration;
            });

            var seconds = ((length / 1000) % 60).toFixed();
            var minutes = ((length / (1000 * 60)) % 60).toFixed();
            var hours = ((length / (1000 * 60 * 60)) % 24).toFixed();

            var durationString = hours + ':' + minutes + ':' + seconds;

            $('p.totalTime').html(durationString);
        },
        "fnDrawCallback": function() {

//           var votes = getTableId(votetable);
//           markSelected(tracktable,votes);    // send this to server

            var api = this.api();
            var rows = api.rows( {page:'current'} ).nodes();
            var last=null;

            api.column(0, {page:'current'} ).data().each( function ( sc_id, i ) {
                $(rows).eq( i ).after(
                    '<tr class="trackWidgetRow">'
                    +'<td colspan="7">'
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
            { "targets": 3, "data": "uploaded_at", "render": { "display": calc_created_at } },
            { "targets": 4, "data": "playback_count", "render": nullify },
            { "targets": 5, "data": "comment_count", "render": nullify },
            { "targets": 6, "data": "favoritings_count", "render": nullify },
            { "targets": 7, "className": "vote", "data": null, "orderable": false, defaultContent: '' }
        ]
    } );

    var votetable = $('#votetracks').dataTable( {
        "bPaginate": false,
        "bFilter": false,
        "ajax": {
            "url": "/api/vote/?format=json",
            "dataSrc": ""
        },
        "fnRowCallback": function( nRow, aData, iDisplayIndex, iDisplayIndexFull ) {
//          console.log(aData);
        },
        "oLanguage": {
            "sEmptyTable":     "No tracks selected"
        },
        "infoCallback": function( settings, start, end, max, total, pre ) {
            if(max)
                $('p.numTracks').html(max + ' tracks');

            $('.slekshun .selected').html(max + ' selected');
            $('.slekshun .remaining').html((20-max) + ' remaining');
        },
        "columnDefs": [
            { "targets": 0, "data": "track.sc_id", "visible": false },
            { "targets": 1, "data": "track.title", "orderable": false }
        ]
    } );

    function calc_created_at(data) {
        date = new Date(data);
        return moment(date).fromNow(); // 4 years ago; //date.toISOString().substring(0, 10);
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

    $('#tracks tbody').on( 'click', 'td.title', function () {

        var trackRow = $(this).closest('tr');
        var trackData = tracktable.fnGetData(trackRow);
        var trackTitle = trackData.title;
        var trackId = trackData.sc_id;
        var trackWaveform = trackData.waveform_url;
        var trackArt = trackData.artwork_url;

        var waveFormRow = $(trackRow).next('tr');

        $('.trackWidgetRow').not(trackRow).removeClass('open');
        $('#tracks tbody tr').removeClass('playing');
        $(waveFormRow).addClass('open');

        if(trackId){
            if(currentTrack == trackId){
                if(currentStream.paused){
                    currentStream.resume();
                    $(trackRow).addClass('playing');
                }
                else{
                    currentStream.pause();
                    $(trackRow).removeClass('playing');
                }
            }
            else{

                var waveformContainer = $(waveFormRow).find('div.waveformContainer')[0];
                $(waveformContainer).empty();

                var track = {
                    waveform_url: trackWaveform,
                    uri : '/tracks/'+trackId
                };

                $(waveFormRow).find('div.trackArt:eq(0)').html( trackArt ? '<img src="' + trackArt + '" />' : '');

                var waveform = new Waveform({
                    container: $(waveFormRow).find('div.waveformContainer')[0],
                    innerColor: 'transparent',
                    outerColor: '#310520',
                    playedColor: '#f50',
                    defaultColor: 'transparent'
                });

                waveform.dataFromSoundCloudTrack(track);
                var streamOptions = waveform.optionsForSyncedStream({
                    loadedColor: '#fff',
                    playedColor: '#f50',
                    innerColor: 'transparent',
                    defaultColor: 'transparent'
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

                $(trackRow).addClass('playing');
            }
        }
    
    } );

    $('#tracks tbody').on( 'click', 'td.vote', function (e) {

        e.stopPropagation();

        var trackRow = $(this).closest('tr');
        var trackData = tracktable.fnGetData(trackRow);
        var trackId = trackData.sc_id;
        var trackTitle = trackData.title;

        var totalVotes = 20

        if ( !$(trackRow).hasClass('voted') ) {
            totalvote = votetable.fnSettings().fnRecordsTotal();

            if (totalvote > totalVotes-1) {
                alert(totalVotes + " votes already reached!");
            } else {
                $(trackRow).addClass('voted');
                votetable.fnAddData( { track: { 'sc_id': trackId, 'title': trackTitle } } );
            };
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

                url : "/vote/tracks/all/",
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

    var logo = $('.logo');
    var logoTop = $(logo).offset().top;
    var logoLeft = $(logo).offset().left;

    var mainTable = $('.main');

    $(window).scroll(function(){
        var scrollTop = $(this).scrollTop();
        var sinVal = Math.abs(Math.sin(scrollTop+90/3));

        var boundsX = $(this).width();
        var boundsY = $(this).height();

        var offset = 54 + (scrollTop / 2);
        var rotation = scrollTop/5;
        var rotate, top, left;
        if(scrollTop<50){
            rotate = 'rotate3d(0,0,0,0)';
            left =  logoLeft+'px';
            top = logoTop+'px';
            $(logo).css({ left: left, top: top});
        }
        else{
            rotate = 'rotateZ('+ rotation + 'deg)';
            left = Math.random()*boundsX + 'px';
            top = offset + 'px';
            if(sinVal<0.2){
                $(logo).css({ left: left, top: top});
            }
        }

        $(logo).css({top: offset + 'px', transform: rotate, opacity: sinVal});

        $('#tracks').on('mouseover', 'tr', function(){
            $(this).next().next().addClass('obscured');
        }).on('mouseout', 'tr', function(){
            $(this).next().next().removeClass('obscured');
        });
    });

    $('.navlinks .info').bind("click", function()
    {
        console.log('clicked');
        $(this).toggleClass('open');
        $('.infoText').toggleClass('open');
    });

} );
