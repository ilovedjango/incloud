$(function () {
	var nav = $('.navbar');
	var content = $('.navbar');
	$(window).scroll(function () {
		if ($(this).scrollTop() > 53) {
			nav.addClass("navbar-fixed");
			content.addClass("topmargin");
		} else {
			nav.removeClass("navbar-fixed");
			content.removeClass("topmargin");

		}
	});
});



$(document).ready(function(){
    $("#myBtn").click(function(){
        $("#myModal").modal();
    });
});



//For getting CSRF token
function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
             }
          }
      }
 return cookieValue;
}


// Subscription
$(document).ready(function(){
    var csrftoken = getCookie('csrftoken');
    $("#submit").live("click", function(e){
        e.preventDefault();
        $.post("/subscription/",{
                url : window.location.href,
                csrfmiddlewaretoken : csrftoken,
                full_name : full_name,
                email : email,
        });
    });
});




// Server request
$(document).ready(function(){
    var csrftoken = getCookie('csrftoken');
    $("#ServerRequest").live("click", function(e){
        e.preventDefault();
        $.post("/getserver/",{
                url : window.location.href,
                csrfmiddlewaretoken : csrftoken,
                full_name : full_name,
                location : location,
                time : time,
                skype_id : skype_id,
                instructions : instructions,
                order_type : order_type,
                tv_machine : tv_machine,
                quantity : quantity,
                payment_method : payment_method,
        });
    });
});


//requestpvaaccounts
$(document).ready(function(){
    var csrftoken = getCookie('csrftoken');
    $("#requestpvaaccounts").live("click", function(e){
        e.preventDefault();
        $.post("/Job/",{
                url : window.location.href,
                csrfmiddlewaretoken : csrftoken,
                email : email,
                skypeid : skypeid,
                description : description,
                quantity : quantity,
        });
    });
});


// Job
$(document).ready(function(){
    var csrftoken = getCookie('csrftoken');
    $("#post-project-submit").live("click", function(e){
        e.preventDefault();
        $.post("/Job/",{
                url : window.location.href,
                csrfmiddlewaretoken : csrftoken,
                name_project : name_project,
                project_description : project_description,
                name : name,
                email : email,
        });
    });
});