var accountSelection = [];
var accountRejection = [];
$(document).ready(function(){
    $("#audianceConfiguration").on("click", function(){
        $.ajax({
            type: "POST",
            url: "/audianceConfiguration",
            processData: true,
            contentType: false,
            success: function(data){
              $("#main-screen").html(data)
            },
            error:function(xhr, status, error){
              alert("error ajax loading:" + error)
            },
        });
    })

    $("#performanceConfiguration").on("click", function(){
        $.ajax({
            type: "POST",
            url: "/performanceConfiguration",
            processData: true,
            contentType: false,
            success: function(data){
              $("#main-screen").html(data)
            },
            error:function(xhr, status, error){
              alert("error ajax loading:" + error)
            },
        });
    })

    $("#informationRequestie").on("click", function(){
        $.ajax({
            type: "POST",
            url: "/informationRequestie",
            processData: true,
            contentType: false,
            success: function(data){
              $("#main-screen").html(data)
            },
            error:function(xhr, status, error){
              alert("error ajax loading:" + error)
            },
        });
    })

    $("#main-screen").on("click", ":button[name='audianceFileUploadButton']", function(){
      const file = $("#main-screen #audianceFileUploadInput").prop("files")[0]
      if(!file){
        alert("Please select a file.")
        return;
      }

      const audianceAccount = $("#main-screen #audianceAccountName").val()
      const formData = new FormData();
      formData.append('userfile', file);
      formData.append('audianceAccount', audianceAccount)

      $.ajax({
        type: "POST",
        url: "/audianceFileUpload",
        data: formData,
        processData: false,
        contentType:false,
        success: function(data){
          alert("file uploaded successfully")
          $("#audianceConfiguration").trigger("click")
        },
        error:function(xhr, status, error){
          alert("error uploading file:" + error)
        },
      });
    })

    $("#main-screen").on("click", ":button[name='performanceFileUploadButton']", function(){
      const file = $("#main-screen #performanceFileUploadInput").prop("files")[0]
      if(!file){
        alert("Please select a file.")
        return;
      }

      const performanceAccount = $("#main-screen #performanceAccountName").val()
      const formData = new FormData();
      formData.append('userfile', file);
      formData.append('performanceAccount', performanceAccount)

      $.ajax({
        type: "POST",
        url: "/performanceFileUpload",
        data: formData,
        processData: false,
        contentType:false,
        success: function(data){
          alert("file uploaded successfully")
          $("#performanceConfiguration").trigger("click")
        },
        error:function(xhr, status, error){
          alert("error uploading file:" + error)
        },
      });
    })

    $("#main-screen").on("change", "input:checkbox[name='performanceAccountSelection']", function(){
      if(this.checked){
        if(accountSelection.includes(this.value) == false){
          accountSelection.push(this.value)
        }
        if(accountRejection.includes(this.value) == true){
          const index = accountRejection.indexOf(this.value)
          accountRejection.splice(index, 1)
        }
      }else{
        if(accountRejection.includes(this.value) == false){
          accountRejection.push(this.value)
        }
        if(accountSelection.includes(this.value) == true){
          const index = accountSelection.indexOf(this.value)
          accountSelection.splice(index, 1)
        }
      }
    })

    $("#main-screen").on("click", ":button[name='configurationSavingButton']", function(){
      $.ajax({
        type: "POST",
        url: "/requirationSwitch",
        data: JSON.stringify({
          "accountSelection": accountSelection,
          "accountRejection": accountRejection
        }),
        processData: false,
        contentType: 'application/json',
        success: function(data){
          alert("Success")
          $("#performanceConfiguration").trigger("click")
        },
        error:function(xhr, status, error){
          alert("error:" + error)
        },
      });
    })

    $("#main-screen").on("click", ":button[name='dataLoadingButton']", function(){
      $.ajax({
        type: "POST",
        url: "/dataReceivement",
        processData: false,
        contentType: 'application/json',
        success: function(data){
          $("#informationRequestie").trigger("click")
          console.log(data)
        },
        error:function(xhr, status, error){
          alert("error:" + error)
        },
      });
    })
})