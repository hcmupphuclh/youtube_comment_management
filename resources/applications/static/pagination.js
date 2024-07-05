var current_page = 1;
var records_per_page = 50;

function prevPage(){
    if(current_page > 1){
        current_page--;
        changePage(current_page);
    }
}

function nextPage(){
    if(current_page < numPages()){
        current_page++;
        changePage(current_page);
    }
}

function changePage(page){
    var btn_next = $("#btn_next")
    var btn_prev = $("#btn_prev")
    var gridview = $("#gridview")
    var page_span = $("#page")

    if (page < 1) page = 1;
    if (page > numPages()) page = numPages();

    gridview.html("");
    for (var i = (page - 1) * records_per_page; i < (page * records_per_page); i++){
        gridview.append("<div class='row'>" +
        "<div class='col-2'>" + 
           "<div class='input-group mb-3'>"
          + "<div class='input-group-prepend'>"
            + "<div class='input-group-text'>"
             + "<input type='checkbox' name='videoSelection' value='"+ objJson[i]['contentDetails']['videoId'] +"'>"
          +   "</div>" 
          + "</div>" +
        "</div>" + "</div>" +                                      
        "<div class='col-6'>" + objJson[i]['snippet']['title'] + "</div>" +
        "<div class='col-2'>" + '<button class="btn btn-primary" type="button" value="'+ objJson[i]['contentDetails']['videoId'] +'" name="fbShareActivator">Open Link</button>' + "</div>" +
        "<div class='col-2'>" + objJson[i]['snippet']['publishedAt'] + "</div>"+
      "</div>") 
    }
    page_span.html(page);

    if (page == 1) {
        btn_prev.css("visibility", "hidden");
    } else {
        btn_prev.css("visibility", "visible");
    }

    if (page == numPages()) {
        btn_next.css("visibility", "hidden");
    } else {
        btn_next.css("visibility", "visible");
    }
}

function numPages(){
    return Math.ceil(objJson.length / records_per_page);
}
