function ShowPersons() {
    query = document.getElementById('search_query').value
    gender = document.getElementById("gender_id");
    gender_selected = gender.options[gender.selectedIndex].value;
    // console.log(gender_selected)
    // console.log(query)
    $.ajax({
        url: "../getpersons",
        type: "GET",
        data: {
            "query": query,
            "gender": gender_selected
        },
        success: function (data) {
            $("#persons_list").html(data);
        }
    });
}
