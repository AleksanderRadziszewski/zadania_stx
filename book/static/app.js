function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function book_import(event) {
    event.preventDefault();
    var csrftoken = getCookie('csrftoken');
    var search_input = $("#id_search_input").val();
    $.post({
        url: "/book_import/",
        data: {
            csrfmiddlewaretoken: csrftoken,
            search_input: search_input,
        }
    }).done(function () {
        $("#search_list").text("Books have already imported")
    }).fail(function (e) {
        console.log(e)
    });
}
$(document).ready(function () {
    $("#search_import").click(book_import);
});

function filter_api(event) {
    event.preventDefault();
    var csrftoken = getCookie('csrftoken');
    var search_input = $("#id_search_input").val();
    var checkboxes_button = document.querySelectorAll(".my-checkbox");

    checkboxes_button.forEach(function (checkbox) {
        if (checkbox.checked) {
            var value = checkbox.value;
            $.post({
                url: "/filter/",
                data: {
                    csrfmiddlewaretoken: csrftoken,
                    value: value,
                    search_input: search_input,
                }
            })
        } else {
            $.post({
                url: "/filter/",
                data: {
                    csrfmiddlewaretoken: csrftoken,
                    search_input: search_input,
                }
            }).done(function (response) {
                $("#search_list").html(response)
            }).fail(function (e) {
                console.log(e)
            })
        }
    })
}

$(document).ready(function () {
    $("#filter").click(filter_api);
});

function search_api(event) {

    event.preventDefault();
    var csrftoken = getCookie('csrftoken');
    var search_input=$("#id_search_input").val();

    $.post({
        url: "/search_api/",
        data: {
            csrfmiddlewaretoken: csrftoken,
            search_input:search_input
        }
    }).done(function (response) {
        var $result_list = $("#search_list");
        $result_list.html(response)
    }).fail(function (e) {
        console.log(e)
    });
}

$(document).ready(function () {
    $("#search_api").click(search_api);
});
