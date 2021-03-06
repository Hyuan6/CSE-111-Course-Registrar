$(document).ready(function() {
    setTimeout(function() {
        $("#cookieConsent").fadeIn(200);
    }, 1000);
    $("#closeCookieConsent, .cookieConsentOK").click(function() {
        $("#cookieConsent").fadeOut(200);
    });
    updatePage();
});

function updatePage() {
    var cookie = getcookie("student_id");
    if (cookie == undefined) { //unsuccessful login
        document.getElementById("Main Banner").style = "display: block;";
        document.getElementById("User Profile").style = "display: none;";
    } else {
        document.getElementById("Main Banner").style = "display: none;";
        document.getElementById("User Profile").style = "display: block;";
        populateUserProfile(student_id = cookie);
    }
}

function populateUserProfile(student_id = '') {

    $.ajax({
        type: 'GET',
        url: "/CourseReg/student_profile/",
        data: { student_id },
        success: function(data) {
            var username = data[0];
            var class_standing = data[1];
            var phone_number = data[2];
            if (data[3] == 1) {
                var academic_probation = "Yes"
            } else {
                var academic_probation = "None";
            }

            document.getElementById("welcome-user").innerText = "Welcome " + username;
            document.getElementById("username-profile-panel").innerText = username;
            document.getElementById("input-username").value = username

            document.getElementById("input-class-standing").value = class_standing;
            document.getElementById("input-phone-number").value = phone_number;
            document.getElementById("input-academic-probation").value = academic_probation;
            document.getElementById("input-holds").value = academic_probation;
        },
        failure: function(data) {
            console.log(data)

        },
    });
}

function getcookie(name = '') {
    let cookies = document.cookie;
    let cookiestore = {};

    cookies = cookies.split(";");

    if (cookies[0] == "" && cookies[0][0] == undefined) {
        return undefined;
    }

    cookies.forEach(function(cookie) {
        cookie = cookie.split(/=(.+)/);
        if (cookie[0].substr(0, 1) == ' ') {
            cookie[0] = cookie[0].substr(1);
        }
        cookiestore[cookie[0]] = cookie[1];
    });

    return (name !== '' ? cookiestore[name] : cookiestore);
}