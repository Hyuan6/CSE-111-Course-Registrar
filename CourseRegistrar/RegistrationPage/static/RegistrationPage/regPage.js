$(document).ready(function(){
    
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
    
    $("#submit").click(function(){
        var cl = document.getElementsByClassName("course-item");
        var classes = [];
        var i;
        console.log(cl.length)
        for(i = 0; i < cl.length;i++){
            var count = i;
            classes.push({[count]:cl[i].innerText.split('\n')[0].split(' ')[0]})
        }
        console.log(classes);
        $.ajax({
            type: 'GET',
            url:"/CourseReg/register/", 
            data:{
                classes, sid
            },
            success: function(data){
                alert("registered")
                console.log("shits done");
            },
            failure: function(data){
                alert("shits fucked");
            },
        });
    });

    $("#gen").click(function(){
        
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
        $.ajax({
            type: 'GET',
            url:"/CourseReg/ajax/",
            async: false,
            success: function(data){
                items = data
            },
            failure: function(data){
                console.log(data)
                
            },
        });
        rep = items
        return rep;
    }
    var existing_elements = [];
    function exists(el){
        return existing_elements.includes(el);
    }

    function something(){
        console.log("test passed");
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
    var button_ids =[];
    new autoComplete({
        data:{
            src: ac(),
            cache: false
        },
        placeHolder:"Course Number",
        highlight:true,
        searchEngine: "loose",
        onSelection: feedback =>{
            if(!exists(feedback.selection.value)){
                var new_div = document.createElement("div")
                new_div.className = "course-item"
                // add buttons and inner div
                new_div.innerHTML = feedback.selection.value + " :<div class='course-list-options'><button class='ui grey tiny button' role='button'>Sections</button><button class='ui pink tiny icon button' role='button'><i onclick='something()' aria-hidden='true' class='fa fa-times'></i></button></div>"
                button_ids.push(counter);
                counter++
                // $(i).attr('id', 'id' + counter++)
                document.getElementById("selclasses").appendChild(new_div)
                existing_elements.push(feedback.selection.value);
            }
            else{
                alert("already added")
            }
            
        }
    });

   

    $("i").click(function(){
        console.log("we here")
        if(button_ids.includes(this.id)){
            console.log("button: " + this.id)
            var elem = document.getElementById(this.id);
            elem.parentNode.removeChild(elem);
        }
    })
    
});