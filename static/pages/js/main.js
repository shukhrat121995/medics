$(document).ready(function () {
    $("#birthFromDate").datepicker({
        format: 'dd/mm/yyyy',
        autoclose: 1,
        //startDate: new Date(),
        todayHighlight: false,
        //endDate: new Date()
    }).on('changeDate', function (selected) {
        var minDate = new Date(selected.date.valueOf());
        $('#birthToDate').datepicker('setStartDate', minDate);
        /* hide autocomplete for birth date*/
        //$("#birthToDate").val($("#birthFromDate").val());
        $(this).datepicker('hide');
    });

    $("#birthToDate").datepicker({
        format: 'dd/mm/yyyy',
        todayHighlight: true,
        //endDate: new Date()
    }).on('changeDate', function (selected) {
        $(this).datepicker('hide');
        ShowPersons()
    });

    $("#deathFromDate").datepicker({
        format: 'dd/mm/yyyy',
        autoclose: 1,
        //startDate: new Date(),
        todayHighlight: false,
        //endDate: new Date()
    }).on('changeDate', function (selected) {
        var minDate = new Date(selected.date.valueOf());
        $('#deathToDate').datepicker('setStartDate', minDate);
        /* hide autocomplete for death date */
        //$("#deathToDate").val($("#deathFromDate").val());
        $(this).datepicker('hide');
    });

    $("#deathToDate").datepicker({
        format: 'dd/mm/yyyy',
        todayHighlight: true,
        //endDate: new Date()
    }).on('changeDate', function (selected) {
        $(this).datepicker('hide');
        ShowPersons()
    });
    const node = document.getElementById('search_query');
    node.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            ShowPersons(document.getElementById('search_query').value);
        }
    });
    const place_of_birth = document.getElementById('place_of_birth');
    place_of_birth.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            ShowPersons();
        }
    });
    ShowPersons();
});


function ShowPersons(page_number) {
    query = document.getElementById('search_query').value

    gender = document.getElementById("gender_id");
    gender_selected = gender.options[gender.selectedIndex].value;

    social_class = document.getElementById("social_class");
    social_class_selected = social_class.options[social_class.selectedIndex].value;

    place_of_birth = document.getElementById('place_of_birth').value

    language = document.getElementById("language_id");
    language_selected = language.options[language.selectedIndex].value;

    birth_from_date = document.getElementById('birthFromDate').value
    birth_to_date = document.getElementById('birthToDate').value
    death_from_date = document.getElementById('deathFromDate').value
    death_to_date = document.getElementById('deathToDate').value

    $.ajax({
        url: "../getpersons",
        type: "GET",
        data: {
            "query": query,
            "page": page_number,
            "gender": gender_selected,
            "language": language_selected,
            "social_class": social_class_selected,
            "place_of_birth": place_of_birth,
            "birth_from_date": birth_from_date,
            "birth_to_date": birth_to_date,
            "death_from_date": death_from_date,
            "death_to_date": death_to_date,
        },
        success: function (data) {
            $("#persons_list").html(data);
            let table = $("table tr");
            table.hide();
            table.each(function (index) {
                $(this).delay(index * 25).show(10);
            });
        }
    });
}


