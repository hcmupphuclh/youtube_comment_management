$(document).ready(function(){
    $("#audianceConfiguration").on("click", function(){
        $("#main-screen").load("../resources/blueprints/attachments/templates/gridview.html")
        console.log(window.location.href)
    })
})