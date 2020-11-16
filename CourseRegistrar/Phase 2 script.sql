-- 1: Student registers for this service
insert into Student (Student_ID, Password, Username, Class_Standing, Phone_Number)
values ("1", " ", "Admin", "SR", "(111)111-1111")

-- 2: Semester starts and theres a new course
insert into Course (sub, crn, Instructor, Title, cnum,  Actv, Units, Days, TimeOfLec, Bldg_Rm, Start, End, Max_enrl, Act_enrl, Seats_avail)
values ("CSE", "11111", "Internet", "Database", "CSE-111-01", "Lect", "MWF", "12:00-12:01am", "REMOTE", "01-JAN", "02-JAN", 1, 0, 1)

-- 3: Student registers for said course
insert into Rolecall (course, student, sid)
values ("CSE-111-01", "Admin", "1")

-- 4: Student realizes he rather not
delete from rolecall
where student = "Admin" and course = "CSE-111-01"

-- 5: New course added
insert into Course (sub, crn, Instructor, Title, cnum,  Actv, Units, Days, TimeOfLec, Bldg_Rm, Start, End, Max_enrl, Act_enrl, Seats_avail)
values ("CSE", "11112", "Satan", "Networks", "CSE-160-01", "Lect", "MWF", "12:00-12:01am", "REMOTE", "01-JAN", "02-JAN", 1, 0, 1)

-- 6: Check if Satan has seats available
select Seats_avail
from Course
where cnum = "CSE-160-01"

-- 7: Student decides to join satan
insert into Rolecall (course, student, sid)
values ("CSE-160-01", "Admin", "1")

-- 8: Update courses to note that student has registered. Yah we forgot this for query 3
update Course
set Act_enrl = Act_enrl + 1,
    Seats_avail = Seats_avail - 1
where cnum = "CSE-160-01"

-- 9: Student deletes account
delete from Student
where Studnet_ID = 1

-- 10 / 11: Drop student from classes
update Course
set Act_enrl = Act_enrl - 1,
    Seats_avail = Seats_avail + 1
where cnum in ( select course
                from Rolecall
                where student = 1)

delete from Rolecall
where student = 1

-- 12: Get students currently in Satan's class
select Username
from Course inner join Rolecall on cnum = course
            inner join Student on student = Student_ID
where Instrutor = "Satan"

-- 13: How many units is Admin enrolled in
select sum(Units)
from Rollcall inner join Course on course = cnum
              inner join Student on student = Student_ID
where Username = "Admin"

-- 14: Simple get class query
select *
from Course
where crn = "11111"

-- 15: classes taught by satan
select * 
from Course
where Instructor = "Satan"

-- 16: all courses starting at 12pm or later
select *
from Course
where TimeOfLec like "%pm"

-- 17: all courses not on monday
select *
from Course
where Days not like "%M%"

-- 18: All discussion sections for a given course

with LectureCnum as ( select cnum
                      from Course
                      where crn = "11111")
select *
from Course
where cnum like substr(LectureCnum, 0, instr(LectureCnum,"-") + 3)

-- 19: All seniors with < 12 units
select Username
from Student inner join Rollcall on Student_ID = student
             inner join Course on course = cnum
where Class_Standing = "SR"
group by Student_ID
having sum(Units) < 12

-- 20: All courses not conflicting with Admin's schedule
select *
from Course
where not exists (select 1 
                  from (select substr(Time, 0, instr(Time,"-")-1) as startTime, substr(Time, instr(Time,"-"), length(Time)) as EndTime
                        from Rollcall inner join Course on course = cnum
                                    inner join Student on student = Student_ID
                        where username = "Admin")
                  where substr(Course.Time, 0, instr(Course.Time,"-")-1) not between startTime and EndTime)

