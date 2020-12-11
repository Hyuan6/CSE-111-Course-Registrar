var existing_elements = [];
$(document).ready(function() {

    var sid = getcookie("student_id")
    console.log(sid)

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

    $("#submit").click(function() {
        var cl = document.getElementsByClassName("course-item");
        var classes = [];
        var i;
        console.log(classes)
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
                classes,
                sid
            },
            success: function(data) {
                if (data === "Login") {
                    alert("Please log in before registering.")
                } else if (data === "Success") {
                    alert("Successfully Registered")
                }
            },
            failure: function(data) {
                alert("shits fucked");
            },
        });
    });

    $("#gen").click(function(){
        var cl = document.getElementsByClassName("course-item");
        var classes = [];
        var i;
        console.log(classes)
        for (i = 0; i < cl.length; i++) {
            var count = i;
            classes.push({
                [count]: cl[i].innerText.split('\n')[0].split(' ')[0]
            })
        }
        
        console.log(classes);
        $.ajax({
            type: "GET",
            url: "/CourseReg/pref/",
            data:{
                classes,
                sid
            },
            success: function(data){
                alert("generating")
            },
            failure: function(data){
                alert("it didn't work")
            },
        });

        placeOnTable('ANTH-003-01', 16.5, 17.75, 'MW', "rgb(255,255,0)");
        placeOnTable('CSE-015-01', 9.5, 10.25, 'MW', "rgb(255,0,255)" )
        placeOnTable('PHYS-008-01', 13.5, 14.75, 'TR', "rgb(0,255,255)")
    });

    var modal = document.getElementById("myModal");
    $("#pref").click(function(){
        modal.style.display = "block";
    });
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function(){
        modal.style.display = "none";
    }
    window.onclick = function(event) {
        if (event.target == modal) {
          modal.style.display = "none";
        }
      }

    function ac(){
        var rep = [];
        var bool_ics = document.getElementById("fc").checked
        var earl = document.getElementById("early")
        var late = document.getElementById("late")
        $.ajax({
            type: 'GET',
            url: "/CourseReg/ajax/",
            async: false,
            success: function(data) {
                items = data[0]
                others = data[1]
            },
            failure: function(data) {
                console.log(data)
                
            },
        });
        if(bool_ics){
            rep=others;
        }
        else{
            rep=items;
        }
        return rep;
    }
    

    function exists(el) {
        return existing_elements.includes(el);
    }

   

    $(".chb").change(function() {
        $(".chb").prop('checked', false);
        $(this).prop('checked', true);
      });

    $(".bhc").change(function() {
        $(".bhc").prop('checked', false);
        $(this).prop('checked', true);
    });

    
    var counter = 1;
    var button_ids = [];
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
                var new_div = document.createElement("div");
                new_div.id = counter + "i";
                new_div.className = "course-item";
                    // add buttons and inner div
                new_div.innerHTML = feedback.selection.value + " :<div class='course-list-options'><button class='ui grey tiny button' role='button'>Sections</button><button class='ui pink tiny icon button' role='button'><i id = "+ counter +" onclick='something(this.id)' aria-hidden='true' class='fa fa-times'></i></button></div>";
                button_ids.push(counter);
                counter++;
                document.getElementById("selclasses").appendChild(new_div);
                existing_elements.push(feedback.selection.value);
            } else {
                alert("already added");
            }

        }
    });

    /*
    Example Parameter:
    (string) cnum = CSE-185-02L
    (float) start = 11.5
    (float) end = 13.5
    (string) day = MWF
    (any valid css color selection) color = rgb(255,255,255)
    */
    function placeOnTable(cnum, start, end, days, color) {
        var dayMapping = {
            "M": 0,
            "T": 1,
            "W": 2,
            "R": 3,
            "F": 4,
        };

        var spacingPer30Min = 22.25;
        var topMultiplier = (start - 7) * 2;
        var heightMultiplier = (end - start + 1) * 2;
        var rgba = [color.slice(0, 3), 'a', color.slice(3)].join('');
        rgba = [rgba.slice(0, -1), ', 0.5', rgba.slice(-1)].join('');

        var dayList = days.split("");
        dayList.forEach(function(day) {
            var col = document.getElementsByClassName("days-col")[dayMapping[day]];

            var new_div = document.createElement("div");
            new_div.className = "hour-slot";
            new_div.style = `width: 100%; 
                             position: absolute; 
                             z-index: 1; 
                             top: ${spacingPer30Min*topMultiplier}px; 
                             height: ${spacingPer30Min*heightMultiplier}px; 
                             display: block; 
                             border-radius: 5px; 
                             cursor: pointer; 
                             color: rgb(91, 91, 91); 
                             border-left: 3px solid ${color}; 
                             background: ${rgba};`;
            new_div.innerHTML = `<div class="title" style="font-size: 14px;">${cnum}</div>`;
            col.appendChild(new_div);
        });
    }
    
});

function something(id) {
    console.log("this is running")
    var elem = document.getElementById(id + "i");
    var todel = elem.innerText.split(' ')[0];
    var i;
    for(i=0; existing_elements.length; i++){
        if(existing_elements[i] == todel){
            existing_elements.splice(i, 1);
        }
    }
    console.log(todel);
    elem.parentNode.removeChild(elem);
    console.log(existing_elements);
}