$(function () {
    $("[name='username']").keyup(function () {
        let form_data = $("#reg").serialize()
        $.ajax({
            url: "/username",
            method: "POST",
            data: form_data,
        }).done(function (res) {
            $("#username-availability").html(res)
        })
    })
})
