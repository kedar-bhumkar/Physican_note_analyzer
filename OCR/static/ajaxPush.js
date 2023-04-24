function callOCR(){
    
    $.ajax({
      url: "/",
      type: "POST",
      data: {jsdata: text},
      success: function(response) {
        $("#place_for_suggestions").html(response);
      },
      error: function(xhr) {
        //Do Something to handle error
      }
    });
};