// document.addEventListener("DOMContentLoaded",function() {
//     function getCookie(name) {
//         var cookieValue = null;
//         if (document.cookie && document.cookie !== '') {
//             var cookies = document.cookie.split(';');
//             for (var i = 0; i < cookies.length; i++) {
//                 var cookie = cookies[i].trim();
//                 // Does this cookie string begin with the name we want?
//                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }
//
//     var csrftoken = getCookie("csrftoken");
//     var $title = $("#id_title");
//     var $save=$("#button");
//     console.log($title);
//
//     $title.one("keyup", function (event) {
//         event.preventDefault();
//         var typingTimer;
//         var doneTypingInterval = 50;
//         clearTimeout(typingTimer);
//         if ($('#id_title').val()) {
//             typingTimer = setTimeout(input_send, doneTypingInterval);
//         }
//
//         function input_send() {
//
//             var $title_input = $title.val();
//             console.log($title_input);
//             $.post({
//                 url: "/add_update/",
//                 data: {
//                     csrfmiddlewaretoken: csrftoken,
//                     title_input: $title_input
//                 }
//             }).done(function (responce) {
//                 var $form = $("#form");
//                 console.log($form);
//                 $form.html(response
//
//             })
//                 .fail(function (e) {
//                     alert("nie poszlo");
//                     console.log(e)
//
//                 });
//         }
//     });
//
//
//             $save.one("click", function (event) {
//             $.post({
//                 url: "/add_update/",
//                 data: {
//                     button:button,
//                     csrfmiddlewaretoken: csrftoken,
//                 }
//             }).done(function (repsonse) {
//
//             })
//                 .fail(function (e) {
//                     alert("nie poszlo");
//                     console.log(e)
//
//                 });
//         })
//
// });