function ShowPersons(query) {
    $.ajax({
        url: "../getpersons",
        type: "GET",
        data: {"query": query},
        success: function (data) {
            $("#persons_list").html(data);
        }
    });
}
