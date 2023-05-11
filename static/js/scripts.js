var exampleTwoElement = document.getElementById("example-three"); // Get the element by ID
exampleTwoElement.style.backgroundColor = "pink"; // Change the background color to pink

function exampleOne () {

  var exampleTwoElement = document.getElementById("example-seven"); // Get the element by ID
  exampleTwoElement.style.backgroundColor = "pink"; // Change the background color to pink

}

var exampleTwoElement = document.getElementById("example-seven"); // Get the element by ID
exampleTwoElement.style.backgroundColor = "pink"; // Change the background color to pink

// Dismissal triggers:

var alertList = document.querySelectorAll('.alert')
alertList.forEach(function (alert) {
  new bootstrap.Alert(alert)
})

/* <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button> */


var myAlert = document.getElementById('myAlert')
myAlert.addEventListener('closed.bs.alert', function () {
  // do something, for instance, explicitly move focus to the most appropriate element,
  // so it doesn't get lost/reset to the start of the page
  // document.getElementById('...').focus()
})

// close.bs.alert	Fires immediately when the close instance method is called.
// closed.bs.alert	Fired when the alert has been closed and CSS transitions have completed.



var dropdownElementList = [].slice.call(document.querySelectorAll('.dropdown-toggle'))
var dropdownList = dropdownElementList.map(function (dropdownToggleEl) {
  return new bootstrap.Dropdown(dropdownToggleEl)
})


var dropdown = new bootstrap.Dropdown(element, {
  popperConfig: function (defaultBsPopperConfig) {
    // var newPopperConfig = {...}
    // use defaultBsPopperConfig if needed...
    // return newPopperConfig
  }
})

var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus()
})

// DROPDOWN NAVIGATION
function toggleNavbar() {
  let navbarCollapse = document.getElementById("navbar-collapse");
  const navMarginMob = document.getElementById('nav-margin-mobile');
  const navMarginTab = document.getElementById('nav-margin-tablet');
  let isExpanded = navbarCollapse.classList.contains("show");
  if (isExpanded) {
      navbarCollapse.classList.remove("show")
      navMarginMob.classList.remove('nav-margin-mobile')
      navMarginTab.classList.remove('nav-margin-tablet')
      navMarginMob.classList.add('nav-margin-mobile-short')
      navMarginTab.classList.add('nav-margin-tablet-short');
  } else {
      navbarCollapse.classList.add("show")
      navMarginMob.classList.remove('nav-margin-mobile-short')
      navMarginTab.classList.remove('nav-margin-tablet-short')
      navMarginMob.classList.add('nav-margin-mobile')
      navMarginTab.classList.add('nav-margin-tablet');
  }
}

// DROPDOWN NAVIGATION
function toggleNavbarProfile() {
  let navbarCollapse = document.getElementById("navbar-collapse-profile");
  let navbarButton = document.getElementById("navbar-dropdown-profile");
  const navMarginMob = document.getElementById('nav-margin-mobile');
  const navMarginTab = document.getElementById('nav-margin-tablet');
  let isExpanded = navbarCollapse.classList.contains("show");
  if (isExpanded) {
      navbarCollapse.classList.remove("show")
      navbarCollapse.classList.remove("mt-1")
      navbarCollapse.classList.remove("mb-1")
      navbarButton.classList.remove("mt-2");
  } else {
      navbarCollapse.classList.add("show")
      navbarCollapse.classList.add("mt-1")
      navbarCollapse.classList.add("mb-1")
      navbarButton.classList.add("mt-2");
  }
}


// Define the functions outside the addEventListener block
function playAudio() {
  const audioElement = document.getElementById('user-profile-audio');
  audioElement.play();
  const playButton = document.getElementById('play-user-profile');
  const stopButton = document.getElementById('stop-user-profile');
  playButton.style.display = 'none';
  stopButton.style.display = 'inline';
  audioElement.style.display = 'none';
}

function stopAudio() {
  const audioElement = document.getElementById('user-profile-audio');
  audioElement.pause();
  audioElement.currentTime = 0;
  const stopButton = document.getElementById('stop-user-profile');
  const playButton = document.getElementById('play-user-profile');
  audioElement.style.display = 'none';
  stopButton.style.display = 'none';
  playButton.style.display = 'inline';
}

window.addEventListener('load', function () {
  const playButton = document.getElementById('play-user-profile');
  const stopButton = document.getElementById('stop-user-profile');

  playButton.addEventListener('click', playAudio);
  stopButton.addEventListener('click', stopAudio);
});

// Nav-margin

// Closing profile navigation on clicking on <a> elements

function closeNavbarProfile() {
  var navbarCollapse = document.getElementById('navbar-collapse-profile');
  var navbarToggle = document.getElementById('navbar-dropdown-profile');
  if (navbarCollapse.classList.contains('show')) {
    navbarCollapse.classList.remove('show');
    navbarToggle.setAttribute('aria-expanded', 'false');
  }
}