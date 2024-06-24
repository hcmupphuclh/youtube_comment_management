var videoIDArray = []
var objJson = []
$(document).ready(function(){

    $('#audianceAccountSelection').on('click', 'li', function(){
      $('#audianceSelectionPresent').text($(this).text());
    });
  
    $('#performanceAccountSelection').on('click', 'li',function(){
        $('#performanceSelectionPresent').text($(this).text());
    });

    $('#performanceFileUpload').on('click', function(){
      $("#busniessfileUploadInput").trigger("click");
    });
  
    $('#performanceChosenAccountSubmit').on('click', function(){
      array = []
      performanceChosenAccount = $('#performanceSelectionPresent').text()
        $.ajax({ 
            url: '/dataReceivement', 
            type: 'POST', 
            contentType: 'application/json',
            data: JSON.stringify({
              "performanceChosenAccount": performanceChosenAccount,
            }),
            success: function(response){
              objJson = response
              changePage(1)
              // for(var i = 0; i < response.length; i++){
              //   $("#gridview").append("<div class='row'>" +
              //                           "<div class='col-2'>" + 
              //                              "<div class='input-group mb-3'>"
              //                             + "<div class='input-group-prepend'>"
              //                               + "<div class='input-group-text'>"
              //                                + "<input type='checkbox' name='videoSelection' value='"+ response[i]['contentDetails']['videoId'] +"'>"
              //                             +   "</div>" 
              //                             + "</div>" +
              //                           "</div>" + "</div>" +                                      
              //                           "<div class='col-6'>" + response[i]['snippet']['title'] + "</div>" +
              //                           "<div class='col-2'>" + '<button class="btn btn-primary" type="button" value="'+ response[i]['contentDetails']['videoId'] +'" name="fbShareActivator">Open Link</button>' + "</div>" +
              //                           "<div class='col-2'>" + response[i]['snippet']['publishedAt'] + "</div>"+
              //                         "</div>"
              //   )
              // }
            },
            error: function(xhr){
              console.log("Failure")
            }
        });
    });

    // $("input:checkbox[name='videoSelection']").on("change", function() {
    //   if(this.checked){
    //     videoIDArray.push(this.value)
    //   }else{
    //     const index = videoIDArray.indexOf(this.value)
    //     videoIDArray.splice(index, 1)
    //   } 
    // });

    $("#gridview").on("change", "input:checkbox[name='videoSelection']", function(e){
      if(this.checked){
        videoIDArray.push(this.value)
      }else{
        const index = videoIDArray.indexOf(this.value)
        videoIDArray.splice(index, 1)
      }
    });

    $("#gridview").on("click", ":button[name='fbShareActivator']", function(e){
      link = "https://www.youtube.com/watch?v=" + $(this).attr("value")
      console.log(link)
      window.open(link)
    });

    $("#selectAll").on('click', function(){
      if(this.checked){
        $(":checkbox").each(function(){
          this.checked = true;
          videoIDArray.push(this.value)
        });
      }else{
        $(":checkbox").each(function(){
          this.checked = false;
          const index = videoIDArray.indexOf(this.value)
          videoIDArray.splice(index, 1);
        });
      }
    });

    $("#audianceFileChoosing").on("click", function(){
      $("#audianceFileUploadInput").trigger("click")
    });

    $("#audianceFileUpload").on("click", function(){
      const file = $("#audianceFileUploadInput").prop("files")[0]
      if(!file){
        alert("Please select a file.")
        return;
      }

      const formData = new FormData();
      formData.append('userfile', file);

      $.ajax({
        type: "POST",
        url: "/audianceFileUpload",
        data: formData,
        processData: false,
        contentType: false,
        success: function(data){
          alert("file uploaded successfully")
        },
        error:function(xhr, status, error){
          alert("error uploading file:" + error)
        },
      });
    });

    $("#performanceFileChoosing").on("click", function(){
      $("#performanceFileUploadInput").trigger("click")
    });

    $("#performanceFileUpload").on("click", function(){
      const file = $("#performanceFileUploadInput").prop("files")[0]
      if(!file){
        alert("Please select a file.")
        return;
      }

      const formData = new FormData();
      formData.append('userfile', file);

      $.ajax({
        type: "POST",
        url: "/performanceFileUpload",
        data: formData,
        processData: false,
        contentType: false,
        success: function(data){
          alert("file uploaded successfully")
        },
        error:function(xhr, status, error){
          alert("error uploading file:" + error)
        },
      });
    });
  
    $("#audianceButton").on("click", function(){
          comment = $("#audianceTextArea").val()
          audianceChosenAccount = $('#audianceSelectionPresent').text()
          $.ajax({ 
              url: '/commentExecution', 
              type: 'POST', 
              contentType: 'application/json',
              data: JSON.stringify({
                "audianceChosenAccount": audianceChosenAccount,
                "videoIDs": videoIDArray,
                "comment": comment
              }),
              success: function(response){
                console.log("success")
                
              },
              error: function(xhr){
                console.log("Failure")
              }
          });
    });    
});

