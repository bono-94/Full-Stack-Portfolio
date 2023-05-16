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
  let navbarSticky = document.getElementById("sticky-profile");
  let navbarCollapse = document.getElementById("navbar-collapse-profile");
  let navbarButton = document.getElementById("navbar-dropdown-profile");
  let navbarIcon = document.getElementById("profile-nav-icon");
  let isExpanded = navbarCollapse.classList.contains("show");
  if (isExpanded) {
      navbarCollapse.classList.remove("show")
      navbarCollapse.classList.remove("mt-1")
      navbarCollapse.classList.remove("mb-1")
      navbarButton.classList.remove("mt-2")
      navbarSticky.classList.remove("bg-secondary")
      navbarSticky.classList.remove("bg-gradient")
      navbarSticky.classList.add("bg-transparent")
      navbarSticky.classList.remove("border")
      navbarSticky.classList.remove("border-2")
      navbarSticky.classList.remove("border-dark")
      navbarIcon.classList.remove("fa-ellipsis-vertical")
      navbarIcon.classList.add("fa-ellipsis");
  } else {
      navbarCollapse.classList.add("show")
      navbarCollapse.classList.add("mt-1")
      navbarCollapse.classList.add("mb-1")
      navbarButton.classList.add("mt-2")
      navbarSticky.classList.remove("bg-transparent")
      navbarSticky.classList.add("bg-secondary")
      navbarSticky.classList.add("bg-gradient")
      navbarSticky.classList.add("border")
      navbarSticky.classList.add("border-2")
      navbarSticky.classList.add("border-dark")
      navbarIcon.classList.remove("fa-ellipsis")
      navbarIcon.classList.add("fa-ellipsis-vertical");
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
  let navbarSticky = document.getElementById("sticky-profile");
  var navbarCollapse = document.getElementById('navbar-collapse-profile');
  var navbarToggle = document.getElementById('navbar-dropdown-profile');
  if (navbarCollapse.classList.contains('show')) {
    navbarCollapse.classList.remove('show');
    navbarToggle.setAttribute('aria-expanded', 'false')
    navbarSticky.classList.remove("bg-secondary");
  }
}

const videoElement = document.getElementById('user-video');
const audioElement = document.getElementById('user-profile-audio');
const playButton = document.getElementById('play-user-profile');
const stopButton = document.getElementById('stop-user-profile');

videoElement.addEventListener('play', function() {
  stopAudio();
});

videoElement.addEventListener('pause', function() {
  playAudio();
});

// PUBLIC PROFILE CONTACT MODAL
function modalPublicProfileActivate() {
  $('#contact-modal').modal('toggle');
  const audioElement = document.getElementById('modal-audio-fx');
  audioElement.play();
}

function modalPublicProfileClose() {
  $('#contact-modal').modal('hide');
}

// EDIT PROFILE SAVE MODAL
function modalEditProfileActivate() {
  $('#edit-profile-save').modal('toggle');
}

function modalEditProfileClose() {
  $('#edit-profile-save').modal('hide');
}

$(document).ready(function() {
  // Enable tooltip functionality
  $('[data-toggle="tooltip"]').tooltip();

  // Enable popover functionality
  $('[data-bs-toggle="popover"]').popover({
    trigger: 'focus'
  });
});

function showPopover() {
  const profileExamplePopover = document.getElementById('profile-example');

  // Destroy previous popover instance
  if (profileExamplePopover._popover) {
    profileExamplePopover._popover.dispose();
  }

  // Create new popover instance
  const popover = new bootstrap.Popover(profileExamplePopover);
  popover.show();

  // Store the popover instance on the element for later reference
  profileExamplePopover._popover = popover;
}

function closePopover() {
  const profileExamplePopover = document.getElementById('profile-example');
  const popover = new bootstrap.Popover(profileExamplePopover);
  popover.hide();
}

// PUBLIC PROFILE COLLAPSES

function publicPersonalCollapse() {
  const profileExamplePopover = document.getElementById('profile-information-collapse');
  const profileExamplePopoverIcon = document.getElementById('profile-personal-icon');
  let isExpanded = profileExamplePopover.classList.contains("collapse");
  if (isExpanded) {
    profileExamplePopover.classList.remove("collapse");
    profileExamplePopoverIcon.classList.remove("fa-square-plus");
    profileExamplePopoverIcon.classList.add("fa-square-minus");
  } else {
    profileExamplePopover.classList.add("collapse");
    profileExamplePopoverIcon.classList.remove("fa-square-minus");
    profileExamplePopoverIcon.classList.add("fa-square-plus");
  }

}