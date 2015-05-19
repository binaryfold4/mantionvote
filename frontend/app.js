$(document).ready(function() {
    
    var votetable = $('#votetracks').dataTable( {
        "bPaginate": false,
        "bFilter": false, 
        "ajax": {
            "url": "vote.json",
            "dataSrc": "vote"
        },
        "columns": [
            { "data": "id", "visible": false },
            { "data": "title" }
        ]
    } );  
      
    var tracktable = $('#tracks').dataTable( {
        "aaSorting": [[0,'created_at']],
        "iDisplayLength": -1,
        "lengthMenu": [[25, 50, 100, -1], [25, 50, 100, "All"]],
        "ajax": {
            "url": "user18081971.json",
            "dataSrc": "tracks"
        },
        "fnDrawCallback": function() {
           var votes = getTableId(votetable);
           markSelected(tracktable,votes);    // send this to server
        },
        "columns": [
            { "data": "id", "visible": false },
            { "data": "created_at" },  // should be reofrmatted
            { "data": "title" },
            { "data": "comment_count" },
            { "data": "download_count" },
            { "data": "playback_count" },
            { "data": "favoritings_count" },
            { "data": null, "defaultContent": "<a class='btn btn-warning btn-sm'>vote</a>" }         
        ]
    } );
    
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
        
    $('#tracks tbody').on( 'click', 'tr', function () {
       
        var trackTitle = tracktable.fnGetData(this).title;
        var trackId = tracktable.fnGetData(this).id;
        
        var totalVotes = 20
        
        if ( !$(this).hasClass('selected') ) {
            totalvote = votetable.fnSettings().fnRecordsTotal();
            
            if (totalvote > 20-1) {
                alert(totalVotes + " votes already reached!");
            } else {
                $(this).addClass('selected'); 
                votetable.fnAddData( { 'id': trackId, 'title': trackTitle } );   
            };
            
        };
    
    } );
    
    $('#votetracks tbody').on( 'click', 'tr', function () {  
          votetable.fnDeleteRow(this);
    } );    
    
    $('#vote').click( function () {
        var votes = getTableId(votetable);
        console.log(votes);    // send this to server
    } );
        
} );
