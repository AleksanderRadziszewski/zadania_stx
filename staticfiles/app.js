function search(event) {
        event.preventDefault();
    var csrftoken = getCookie('csrftoken');
    $.post({
        url: "/search_api/",
        data: {
            csrfmiddlewaretoken: csrftoken,
        }
    }).done(function (repsonse) {
        var $result_list = $("#search_list");
        $result_list.html(repsonse)

    })
        .fail(function (e) {
            alert("nie poszlo");
            console.log(e)

        });


}

$(document).ready(function () {
    $("#search_api").click(search);

});

function filter(event) {
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
                    value: value,
                    search_input: search_input,
                }
            })
                .done(function (response) {
                    console.log("poszlo");
                    $("#search_list").html(response)

                })
                .fail(function (e) {
                    alert("nie poszlo");
                    console.log(e)
                })


        }
    })
}

$(document).ready(function () {
    $("#filter").click(filter);
});

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
        console.log("poszlo");
        $("#search_list").text("Books have already imported")

    })
        .fail(function (e) {
            alert("nie poszlo");
            console.log(e)

        });
}

$(document).ready(function () {
    $("#search_import").click(book_import);
});
