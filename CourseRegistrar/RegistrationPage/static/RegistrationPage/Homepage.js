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
    if (cookie == undefined) {
        document.getElementById("Main Banner").style = "display: block;";
        document.getElementById("User Profile").style = "display: none;";
    } else {
        document.getElementById("Main Banner").style = "display: none;";
        document.getElementById("User Profile").style = "display: block;";
        populateUserProfile(student_id = cookie);
    }
}

function populateUserProfile(student_id = '') {}

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