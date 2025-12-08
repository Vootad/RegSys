// SLIDER
const slides = document.querySelectorAll(".slide");
const slideText = document.getElementById("slide-text");
const texts = [
    "Effortless Enrollment Experience — A clean platform.",
    "Intelligent Prerequisite Checking — Automatic validation.",
    "Secure & Unified Access — One gateway for everyone."
];
let currentSlide = 0;

function showSlide(index){
    slides.forEach((s,i)=>{
        s.classList.remove("active");
        if(i===index) s.classList.add("active");
    });
    slideText.textContent = texts[index];
}

function nextSlide(){ 
    currentSlide = (currentSlide+1)%slides.length; 
    showSlide(currentSlide); 
}

function prevSlide(){ 
    currentSlide = (currentSlide-1+slides.length)%slides.length; 
    showSlide(currentSlide); 
}

setInterval(nextSlide, 4000);


// LOGIN VALIDATION
document.getElementById("loginBtn").addEventListener("click", function () {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const errorMsg = document.getElementById("errorMsg");

    errorMsg.style.display = "none";

    if (username === "") {
        errorMsg.textContent = "Username cannot be empty!";
        errorMsg.style.display = "block";
        return;
    }

    if (password === "") {
        errorMsg.textContent = "Password cannot be empty!";
        errorMsg.style.display = "block";
        return;
    }

    errorMsg.style.color = "green";
    errorMsg.textContent = "Validation OK.";
    errorMsg.style.display = "block";
});
