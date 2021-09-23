function ShowPersons(query) {
    $.ajax({
        url: "../getpersons",
        type: "GET",
        data: {"query": query},
        success: function (data) {
            console.log(data)
            $("#persons_list").html(data);
        }
    });
}
