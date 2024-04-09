const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");

// change starts form here

document.addEventListener("DOMContentLoaded", function() {
  const studentRadio = document.getElementById("student");
  const teacherRadio = document.getElementById("teacher");
  const studentForm = document.querySelector(".student-signup");
  const teacherForm = document.querySelector(".teacher-signup");

// change ends form here

signupBtn.onclick = (()=>{
  loginForm.style.marginLeft = "-50%";
  loginText.style.marginLeft = "-50%";
});
loginBtn.onclick = (()=>{
  loginForm.style.marginLeft = "0%";
  loginText.style.marginLeft = "0%";

  teacherForm.style.display = "none";
  studentForm.style.display = "none";

});
signupLink.onclick = (()=>{
  signupBtn.click();
  return false;
});



    const studentDiv = document.querySelector(".a");
    const teacherDiv = document.querySelector(".b");


    // Initially hide the teacher signup form
    teacherForm.style.display = "none";
    studentForm.style.display = "none";
    teacherDiv.style.display = "none";

    // Add event listeners to radio buttons
    studentRadio.addEventListener("click", function() {
      if (studentRadio.checked) {
        studentForm.style.display = "block";
        teacherForm.style.display = "none";
        studentDiv.style.display = "block";
        teacherDiv.style.display = "none";
      }
    });

    teacherRadio.addEventListener("click", function() {
      if (teacherRadio.checked) {
        teacherForm.style.display = "block";
        studentForm.style.display = "none";
        studentDiv.style.display = "none";
        teacherDiv.style.display = "block";
      }
    });
  });

  
