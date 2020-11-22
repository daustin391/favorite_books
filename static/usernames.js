$(function () {
    $("[name='username']").on("keyup", function () {
        let form_data = $("#reg").serialize()
        $.ajax({
            url: "/username",
            method: "POST",
            data: form_data,
        }).done(function (res) {
            $("#username-availability").html(res)
        })
    })

    $("#search").on("keyup", function () {
        let form_data = $("[name='usersearch']").serialize()
        console.log(form_data)
        $.ajax({
            url: "/usersearch",
            method: "POST",
            data: form_data,
        }).done(function (res) {
            $("#usernames").html(res)
        })
    })
    return false
})
