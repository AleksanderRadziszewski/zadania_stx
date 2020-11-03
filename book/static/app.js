function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function search() {
    var csrftoken = getCookie('csrftoken');
    $.post({
        url: "/search_api/",
        data: {
            csrfmiddlewaretoken: csrftoken,
            id_product: this.dataset.id,
        }
    }).done(function (repsonse) {
        var $result_list = $("#search_list");
        console.log($result_list);
        $result_list.html(repsonse)

    })
        .fail(function (e) {
            alert("nie poszlo");
            console.log(e)

        });

    $(document).ready(function (event) {
        event.preventDefault();
        $("#search").click(search);

    })
}