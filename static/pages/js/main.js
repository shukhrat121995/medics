function ShowPersons() {
    query = document.getElementById('search_query').value
    gender = document.getElementById("gender_id");
    gender_selected = gender.options[gender.selectedIndex].value;
    birth_from_date = document.getElementById('birthFromDate').value
    birth_to_date = document.getElementById('birthToDate').value

    // console.log(gender_selected)
    $.ajax({
        url: "../getpersons",
        type: "GET",
        data: {
            "query": query,
            "gender": gender_selected,
            "birth_from_date": birth_from_date,
            "birth_to_date": birth_to_date
        },
        success: function (data) {
            $("#persons_list").html(data);
        }
    });
}


