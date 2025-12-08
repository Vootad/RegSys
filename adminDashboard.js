let courses = [];
let editIndex = -1;

/* اجرای همه بعد از بارگذاری DOM */
document.addEventListener('DOMContentLoaded', () => {
    showHome();
});

/* Home */
function showHome() {
    const content = document.getElementById("content");
    content.innerHTML = `
        <div id="homePage">
            <h1>Welcome Admin!</h1>
            <img src="admin.png" class="home-image">
        </div>
    `;
}

/* فرم اضافه/ویرایش درس */
function showAddCourseForm(isEdit = false) {
    const content = document.getElementById("content");
    let course = {name:"", code:"", teacher:"", capacity:"", room:"", time:"", day:"", prereq:""};
    if(isEdit && editIndex >= 0) course = courses[editIndex];

    content.innerHTML = `
        <h2>${isEdit ? "Edit Course" : "Add New Course"}</h2>
        <div class="form-container">
            <div id="errorMsg"></div>
            <input class="input-field" id="name" placeholder="Course Name" value="${course.name}">
            <input class="input-field" id="code" placeholder="Course Code" value="${course.code}">
            <input class="input-field" id="teacher" placeholder="Instructor Name" value="${course.teacher}">
            <input class="input-field" id="capacity" type="number" placeholder="Capacity" value="${course.capacity}">
            <input class="input-field" id="room" placeholder="Classroom" value="${course.room}">
            <select id="day" class="input-field">
                <option value="">Select Day</option>
                <option value="Saturday" ${course.day=="Saturday"?"selected":""}>Saturday</option>
                <option value="Sunday" ${course.day=="Sunday"?"selected":""}>Sunday</option>
                <option value="Monday" ${course.day=="Monday"?"selected":""}>Monday</option>
                <option value="Tuesday" ${course.day=="Tuesday"?"selected":""}>Tuesday</option>
                <option value="Wednesday" ${course.day=="Wednesday"?"selected":""}>Wednesday</option>
            </select>
            <select id="time" class="input-field">
                <option value="">Select Time</option>
                <option ${course.time=="8-10"?"selected":""}>8-10</option>
                <option ${course.time=="10-12"?"selected":""}>10-12</option>
                <option ${course.time=="14-16"?"selected":""}>14-16</option>
                <option ${course.time=="16-18"?"selected":""}>16-18</option>
            </select>
            <input class="input-field" id="prereq" placeholder="Prerequisite Course Code" value="${course.prereq}">
            <button class="btn-add" id="saveBtn">${isEdit ? "Update Course" : "Add Course"}</button>
        </div>
    `;

    document.getElementById("saveBtn").addEventListener('click', () => {
        if(isEdit) updateCourse();
        else addCourse();
    });
}

/* خواندن فرم */
function readCourseForm() {
    return {
        name: document.getElementById("name").value.trim(),
        code: document.getElementById("code").value.trim(),
        teacher: document.getElementById("teacher").value.trim(),
        capacity: document.getElementById("capacity").value.trim(),
        room: document.getElementById("room").value.trim(),
        day: document.getElementById("day").value,
        time: document.getElementById("time").value,
        prereq: document.getElementById("prereq").value.trim()
    };
}

/* اعتبارسنجی فرم */
function validateCourse(course) {
    const errorMsg = document.getElementById("errorMsg");
    errorMsg.style.display = "none";

    if(!course.name || course.name.length > 50) { errorMsg.innerText="Invalid course name"; errorMsg.style.display="block"; return false; }
    if(!course.code || isNaN(course.code)) { errorMsg.innerText="Course code must be a number"; errorMsg.style.display="block"; return false; }
    if(!course.teacher || /[^a-zA-Z\s]/.test(course.teacher)) { errorMsg.innerText="Instructor name invalid"; errorMsg.style.display="block"; return false; }
    if(!course.capacity || isNaN(course.capacity) || Number(course.capacity) <= 0) { errorMsg.innerText="Capacity must be a positive number"; errorMsg.style.display="block"; return false; }
    if(!course.room) { errorMsg.innerText="Room cannot be empty"; errorMsg.style.display="block"; return false; }
    if(!course.day) { errorMsg.innerText="Day must be selected"; errorMsg.style.display="block"; return false; }
    if(!course.time) { errorMsg.innerText="Time must be selected"; errorMsg.style.display="block"; return false; }

    return true;
}

/* افزودن درس */
function addCourse() {
    const course = readCourseForm();
    if(!validateCourse(course)) return;

    courses.push(course);
    alert("Course added successfully!");
    showCourses();
}

/* بروزرسانی درس */
function updateCourse() {
    const course = readCourseForm();
    if(!validateCourse(course)) return;

    courses[editIndex] = course;
    alert("Course updated!");
    showCourses();
}

/* نمایش لیست دروس */
function showCourses() {
    const content = document.getElementById("content");
    if(courses.length === 0){ content.innerHTML = "<h2>No courses found.</h2>"; return; }

    let rows = "";
    courses.forEach((c,index)=>{
        rows += `<tr>
            <td>${c.name}</td>
            <td>${c.code}</td>
            <td>${c.teacher}</td>
            <td>${c.capacity}</td>
            <td>${c.room}</td>
            <td>${c.day} ${c.time}</td>
            <td>${c.prereq}</td>
            <td>
                <i class="fa-solid fa-pen-to-square icons edit" onclick="editCourse(${index})"></i>
                <i class="fa-solid fa-trash icons trash" onclick="deleteCourse(${index})"></i>
            </td>
        </tr>`;
    });

    content.innerHTML = `
        <h2>Courses List</h2>
        <div class="table-container">
            <table>
                <tr>
                    <th>Name</th>
                    <th>Code</th>
                    <th>Teacher</th>
                    <th>Capacity</th>
                    <th>Room</th>
                    <th>Day & Time</th>
                    <th>Prerequisite</th>
                    <th>Actions</th>
                </tr>
                ${rows}
            </table>
        </div>
    `;
}

/* ویرایش درس */
function editCourse(index) {
    editIndex = index;
    showAddCourseForm(true);
}

/* حذف درس */
function deleteCourse(index) {
    if(!confirm("Are you sure you want to delete this course?")) return;
    courses.splice(index,1);
    alert("Course deleted!");
    showCourses();
}
