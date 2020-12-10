$(document).ready(function() {


    $("#submit").click(function() {
        var cl = document.getElementsByClassName("course-item");
        var classes = [];
        var i;
        console.log(cl.length)
        for (i = 0; i < cl.length; i++) {
            var count = i;
            classes.push({
                [count]: cl[i].innerText.split('\n')[0].split(' ')[0]
            })
        }
        console.log(classes);
        $.ajax({
            type: 'GET',
            url: "/CourseReg/register/",
            data: {
                classes
            },
            success: function(data) {
                alert("registered")
                console.log("shits done");
            },
            failure: function(data) {
                alert("shits fucked");
            },
        });
    });


    function ac() {
        var rep = [];
        $.ajax({
            type: 'GET',
            url: "/CourseReg/ajax/",
            async: false,
            success: function(data) {
                console.log(data)
                items = data
            },
            failure: function(data) {
                console.log(data)
                alert("shits fucked");
            },
        });
        rep = items
        return rep;
    }
    var existing_elements = [];

    function exists(el) {
        return existing_elements.includes(el);
    }

    new autoComplete({
        data: {
            src: ac(),
            cache: false
        },
        placeHolder: "Course Number",
        highlight: true,
        searchEngine: "loose",
        onSelection: feedback => {
            if (!exists(feedback.selection.value)) {
                var new_div = document.createElement("div")
                new_div.className = "course-item"
                    // add buttons and inner div
                new_div.innerHTML = feedback.selection.value + " : <div class='course-list-options'><button class='ui grey tiny button' role='button'>Sections</button><button class='ui pink tiny icon button' role='button'><i aria-hidden='true' class='fa fa-times'></i></button></div>"
                document.getElementById("selclasses").appendChild(new_div)
                existing_elements.push(feedback.selection.value);
            } else {
                alert("already added")
            }

        }
    });
});