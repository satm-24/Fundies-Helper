$(document).ready(function() {
    $.ajax({
        type: "GET",
        // ../src/scraper/piazza_scrape.csv
        url: "piazza_scrape.csv",
        dataType: "text",
        success: function(data) {processData(data);}
     });
});

function processData(allText) {
    var allTextLines = allText.split(/\r\n|\n/);
    var headers = allTextLines[0].split();
    var lines = [];

    for (var i=1; i<allTextLines.length; i++) {
        var data = allTextLines[i].split();

        if (data.length == headers.length) {
            var row = [];
            for (var j=0; j<headers.length; j++) {
                // row.push(headers[j]+":"+data[j]);
                row.push(data[j]);
            }
            lines.push(row);
        }
    }
    document.getElementsByClassName("piazza-one")[0].innerHTML = lines[0];
    document.getElementsByClassName("piazza-two")[0].innerHTML = lines[1];
    document.getElementsByClassName("piazza-three")[0].innerHTML = lines[2];
    document.getElementsByClassName("piazza-four")[0].innerHTML = lines[3];
    document.getElementsByClassName("piazza-five")[0].innerHTML = lines[4];
}
