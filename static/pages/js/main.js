$(document).ready(function () {
    ShowPersons();
    $("#birthFromDate").datepicker({
        format: 'dd/mm/yyyy',
        autoclose: 1,
        //startDate: new Date(),
        todayHighlight: false,
        //endDate: new Date()
    }).on('changeDate', function (selected) {
        var minDate = new Date(selected.date.valueOf());
        $('#birthToDate').datepicker('setStartDate', minDate);
        $("#birthToDate").val($("#birthFromDate").val());
        $(this).datepicker('hide');
    });

    $("#birthToDate").datepicker({
        format: 'dd/mm/yyyy',
        todayHighlight: true,
        //endDate: new Date()
    }).on('changeDate', function (selected) {
        $(this).datepicker('hide');
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
        $("#deathToDate").val($("#deathFromDate").val());
        $(this).datepicker('hide');
    });

    $("#deathToDate").datepicker({
        format: 'dd/mm/yyyy',
        todayHighlight: true,
        //endDate: new Date()
    }).on('changeDate', function (selected) {
        $(this).datepicker('hide');
    });
    const node = document.getElementById('search_query');
    node.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            ShowPersons(document.getElementById('search_query').value);
        }
    });
});


function ShowPersons(page_number) {
    query = document.getElementById('search_query').value
    gender = document.getElementById("gender_id");
    gender_selected = gender.options[gender.selectedIndex].value;
    birth_from_date = document.getElementById('birthFromDate').value
    birth_to_date = document.getElementById('birthToDate').value

    $.ajax({
        url: "../getpersons",
        type: "GET",
        data: {
            "query": query,
            "page": page_number,
            "gender": gender_selected,
            "birth_from_date": birth_from_date,
            "birth_to_date": birth_to_date
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


