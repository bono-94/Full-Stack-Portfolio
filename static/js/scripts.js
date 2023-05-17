var exampleTwoElement = document.getElementById("example-three"); // Get the element by ID
// exampleTwoElement.style.backgroundColor = "pink"; // Change the background color to pink

function exampleOne () {

  var exampleTwoElement = document.getElementById("example-seven"); // Get the element by ID
  exampleTwoElement.style.backgroundColor = "pink"; // Change the background color to pink

}

var exampleTwoElement = document.getElementById("example-seven"); // Get the element by ID
// exampleTwoElement.style.backgroundColor = "pink"; // Change the background color to pink

// Dismissal triggers:

var alertList = document.querySelectorAll('.alert')
alertList.forEach(function (alert) {
  new bootstrap.Alert(alert)
})

/* <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button> */


// var myAlert = document.getElementById('myAlert')
// myAlert.addEventListener('closed.bs.alert', function () {
//   // do something, for instance, explicitly move focus to the most appropriate element,
//   // so it doesn't get lost/reset to the start of the page
//   // document.getElementById('...').focus()
// })

// close.bs.alert	Fires immediately when the close instance method is called.
// closed.bs.alert	Fired when the alert has been closed and CSS transitions have completed.



var dropdownElementList = [].slice.call(document.querySelectorAll('.dropdown-toggle'))
var dropdownList = dropdownElementList.map(function (dropdownToggleEl) {
  return new bootstrap.Dropdown(dropdownToggleEl)
})


// var dropdown = new bootstrap.Dropdown(element, {
//   popperConfig: function (defaultBsPopperConfig) {
//     // var newPopperConfig = {...}
//     // use defaultBsPopperConfig if needed...
//     // return newPopperConfig
//   }
// })

var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

// myModal.addEventListener('shown.bs.modal', function () {
//   myInput.focus()
// })

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
      navbarIcon.classList.add("fa-ellipsis")
      navbarIcon.classList.remove("text-light");
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
      navbarIcon.classList.add("fa-ellipsis-vertical")
      navbarIcon.classList.add("text-light");
  }
}

function stopVideo() {
  const videoElement = document.getElementById('user-video');
  videoElement.pause()
}

// Define the functions outside the addEventListener block
function playAudio() {
  const audioElement = document.getElementById('user-profile-audio');
  audioElement.play();
  audioElement.volume = 0.4
  const playButton = document.getElementById('play-user-profile');
  const stopButton = document.getElementById('stop-user-profile');
  playButton.style.display = 'none';
  stopButton.style.display = 'inline';
  audioElement.style.display = 'none';
  stopVideo()
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

function pauseAudio() {
  const audioElement = document.getElementById('user-profile-audio');
  audioElement.pause();
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

function closeNavbarProfileTop() {
  let navbarSticky = document.getElementById("sticky-profile");
  var navbarCollapse = document.getElementById('navbar-collapse-profile');
  var navbarToggle = document.getElementById('navbar-dropdown-profile');
  let targetElement = document.getElementById('public-profile-hook');
  if (navbarCollapse.classList.contains('show')) {
    navbarCollapse.classList.remove('show');
    navbarToggle.setAttribute('aria-expanded', 'false')
    navbarSticky.classList.remove("bg-secondary");
    navbarSticky.classList.remove("bg-transparent")
    navbarSticky.classList.remove("bg-gradient")
    navbarSticky.classList.remove("border")
    navbarSticky.classList.remove("border-2")
    navbarSticky.classList.remove("border-dark")
  }
  targetElement.style.paddingTop = '';
    targetElement.style.marginTop = '';
}

function closeNavbarProfile() {
  let navbarSticky = document.getElementById("sticky-profile");
  var navbarCollapse = document.getElementById('navbar-collapse-profile');
  var navbarToggle = document.getElementById('navbar-dropdown-profile');
  if (navbarCollapse.classList.contains('show')) {
    navbarCollapse.classList.remove('show');
    navbarToggle.setAttribute('aria-expanded', 'false')
    navbarSticky.classList.remove("bg-secondary");
    navbarSticky.classList.remove("bg-transparent")
    navbarSticky.classList.remove("bg-gradient")
    navbarSticky.classList.remove("border")
    navbarSticky.classList.remove("border-2")
    navbarSticky.classList.remove("border-dark")
  }
}

const videoElement = document.getElementById('user-video');
const audioElement = document.getElementById('user-profile-audio');
const playButton = document.getElementById('play-user-profile');
const stopButton = document.getElementById('stop-user-profile');

videoElement.addEventListener("play", (event) => {
  console.log(
    "The Boolean paused property is now 'false'. Either the play() method was called or the autoplay attribute was toggled."
  );
});

videoElement.addEventListener('play', function() {
  videoElement.volume = 0.5
  pauseAudio()
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
id=profile-expand-all-icon
id=profile-collapse-all-icon
// PUBLIC PROFILE COLLAPSES

// FULL PAGE COLLAPSE
function expandAllProfileColapses() {
  personalCollapse();
  occupationCollapse();
  pastEmploymentCollapse();
  achievementsCollapse();
  attributesCollapse();
  focusCollapse();
  specializationsCollapse();
  resultsCollapse();
  rewardsCollapse();
  personalWallCollapse();

  // Check if all elements are collapsed
  if (
    isCollapsed('profile-information-collapse') &&
    isCollapsed('profile-occupation-collapse') &&
    isCollapsed('profile-career-collapse') &&
    isCollapsed('profile-achievements-collapse') &&
    isCollapsed('profile-attributes-collapse') &&
    isCollapsed('profile-focus-collapse') &&
    isCollapsed('profile-specializations-collapse') &&
    isCollapsed('profile-results-collapse') &&
    isCollapsed('profile-rewards-collapse') &&
    isCollapsed('profile-profile-wall-collapse')
  ) {
    // All elements are collapsed, add class 'd-none' to profile-expand-all-icon
    let expandIcon = document.getElementById('profile-expand-all-icon');
    let collapseIcon = document.getElementById('profile-collapse-all-icon');
    expandIcon.classList.remove('d-none');
    collapseIcon.classList.add('d-none');
  } else if (
    !isCollapsed('profile-information-collapse') ||
    !isCollapsed('profile-occupation-collapse') ||
    !isCollapsed('profile-career-collapse') ||
    !isCollapsed('profile-achievements-collapse') ||
    !isCollapsed('profile-attributes-collapse') ||
    !isCollapsed('profile-focus-collapse') ||
    !isCollapsed('profile-specializations-collapse') ||
    !isCollapsed('profile-results-collapse') ||
    !isCollapsed('profile-rewards-collapse') ||
    !isCollapsed('profile-profile-wall-collapse')
  ) {
    let expandIcon = document.getElementById('profile-expand-all-icon');
    let collapseIcon = document.getElementById('profile-collapse-all-icon');
    collapseIcon.classList.remove('d-none');
    expandIcon.classList.add('d-none');
  }
}

// Function to check if an element is collapsed
function isCollapsed(elementId) {
  let element = document.getElementById(elementId);
  return element.classList.contains('collapse');
}



// PERSONAL INFO COLLAPSE
function personalCollapse() {
  let profilePopover = document.getElementById('profile-information-collapse');
  let profilePopoverIcon = document.getElementById('profile-personal-icon');
  let isExpanded = profilePopover.classList.contains("collapse");
  if (isExpanded) {
    profilePopover.classList.remove("collapse");
    profilePopoverIcon.classList.remove("fa-square-plus");
    profilePopoverIcon.classList.add("fa-square-minus");
  } else {
    profilePopover.classList.add("collapse");
    profilePopoverIcon.classList.remove("fa-square-minus");
    profilePopoverIcon.classList.add("fa-square-plus");
  }
}

// OCCUPATION COLLAPSE
function occupationCollapse() {
  let profilePopover = document.getElementById('profile-occupation-collapse');
  let profilePopoverIcon = document.getElementById('profile-occupation-icon');
  let isExpanded = profilePopover.classList.contains("collapse");
  if (isExpanded) {
    profilePopover.classList.remove("collapse");
    profilePopoverIcon.classList.remove("fa-square-plus");
    profilePopoverIcon.classList.add("fa-square-minus");
  } else {
    profilePopover.classList.add("collapse");
    profilePopoverIcon.classList.remove("fa-square-minus");
    profilePopoverIcon.classList.add("fa-square-plus");
  }
}

// EMPLOYMENT HISTORY COLLAPSE
function pastEmploymentCollapse() {
  let profilePopover = document.getElementById('profile-career-collapse');
  let profilePopoverIcon = document.getElementById('profile-career-icon');
  let isExpanded = profilePopover.classList.contains("collapse");
  if (isExpanded) {
    profilePopover.classList.remove("collapse");
    profilePopoverIcon.classList.remove("fa-square-plus");
    profilePopoverIcon.classList.add("fa-square-minus");
  } else {
    profilePopover.classList.add("collapse");
    profilePopoverIcon.classList.remove("fa-square-minus");
    profilePopoverIcon.classList.add("fa-square-plus");
  }
}

// ACHIEVEMENTS COLLAPSE
function achievementsCollapse() {
  let profilePopover = document.getElementById('profile-achievements-collapse');
  let profilePopoverIcon = document.getElementById('profile-achievements-icon');
  let isExpanded = profilePopover.classList.contains("collapse");
  if (isExpanded) {
    profilePopover.classList.remove("collapse");
    profilePopoverIcon.classList.remove("fa-square-plus");
    profilePopoverIcon.classList.add("fa-square-minus");
  } else {
    profilePopover.classList.add("collapse");
    profilePopoverIcon.classList.remove("fa-square-minus");
    profilePopoverIcon.classList.add("fa-square-plus");
  }
}

// ATTRIBUTES COLLAPSE
function attributesCollapse() {
  let profilePopover = document.getElementById('profile-attributes-collapse');
  let profilePopoverIcon = document.getElementById('profile-attributes-icon');
  let isExpanded = profilePopover.classList.contains("collapse");
  if (isExpanded) {
    profilePopover.classList.remove("collapse");
    profilePopoverIcon.classList.remove("fa-square-plus");
    profilePopoverIcon.classList.add("fa-square-minus");
  } else {
    profilePopover.classList.add("collapse");
    profilePopoverIcon.classList.remove("fa-square-minus");
    profilePopoverIcon.classList.add("fa-square-plus");
  }
}

// BUSINESS FOCUS COLLAPSE
function focusCollapse() {
  let profilePopover = document.getElementById('profile-focus-collapse');
  let profilePopoverIcon = document.getElementById('profile-focus-icon');
  let isExpanded = profilePopover.classList.contains("collapse");
  if (isExpanded) {
    profilePopover.classList.remove("collapse");
    profilePopoverIcon.classList.remove("fa-square-plus");
    profilePopoverIcon.classList.add("fa-square-minus");
  } else {
    profilePopover.classList.add("collapse");
    profilePopoverIcon.classList.remove("fa-square-minus");
    profilePopoverIcon.classList.add("fa-square-plus");
  }
}

// SPECIALIZATIONS COLLAPSE
function specializationsCollapse() {
  let profilePopover = document.getElementById('profile-specializations-collapse');
  let profilePopoverIcon = document.getElementById('profile-specializations-icon');
  let isExpanded = profilePopover.classList.contains("collapse");
  if (isExpanded) {
    profilePopover.classList.remove("collapse");
    profilePopoverIcon.classList.remove("fa-square-plus");
    profilePopoverIcon.classList.add("fa-square-minus");
  } else {
    profilePopover.classList.add("collapse");
    profilePopoverIcon.classList.remove("fa-square-minus");
    profilePopoverIcon.classList.add("fa-square-plus");
  }
}

// RESULTS COLLAPSE
function resultsCollapse() {
  let profilePopover = document.getElementById('profile-results-collapse');
  let profilePopoverIcon = document.getElementById('profile-results-icon');
  let isExpanded = profilePopover.classList.contains("collapse");
  if (isExpanded) {
    profilePopover.classList.remove("collapse");
    profilePopoverIcon.classList.remove("fa-square-plus");
    profilePopoverIcon.classList.add("fa-square-minus");
  } else {
    profilePopover.classList.add("collapse");
    profilePopoverIcon.classList.remove("fa-square-minus");
    profilePopoverIcon.classList.add("fa-square-plus");
  }
}

// REWARDS COLLAPSE
function rewardsCollapse() {
  let profilePopover = document.getElementById('profile-rewards-collapse');
  let profilePopoverIcon = document.getElementById('profile-rewards-icon');
  let isExpanded = profilePopover.classList.contains("collapse");
  if (isExpanded) {
    profilePopover.classList.remove("collapse");
    profilePopoverIcon.classList.remove("fa-square-plus");
    profilePopoverIcon.classList.add("fa-square-minus");
  } else {
    profilePopover.classList.add("collapse");
    profilePopoverIcon.classList.remove("fa-square-minus");
    profilePopoverIcon.classList.add("fa-square-plus");
  }
}

// PERSONAL WALL COLLAPSE
function personalWallCollapse() {
  let profilePopover = document.getElementById('profile-profile-wall-collapse');
  let profilePopoverIcon = document.getElementById('profile-wall-icon');
  let isExpanded = profilePopover.classList.contains("collapse");
  if (isExpanded) {
    profilePopover.classList.remove("collapse");
    profilePopoverIcon.classList.remove("fa-square-plus");
    profilePopoverIcon.classList.add("fa-square-minus");
  } else {
    profilePopover.classList.add("collapse");
    profilePopoverIcon.classList.remove("fa-square-minus");
    profilePopoverIcon.classList.add("fa-square-plus");
  }
}

// REMOVING EXTRA SPACE UPON CLICKING TOP OF PROFILE
let targetElement = document.getElementById('public-profile-hook');
// Listen for hash changes in the URL
window.addEventListener('hashchange', function() {
  // Check if the target element is the current target
  if (window.location.hash === '#' + targetElement.id) {
    // Remove or modify the styles when the element is the target
    targetElement.style.paddingTop = '';
    targetElement.style.marginTop = '';
  } else {
    // Restore the default styles when the element is not the target
    targetElement.style.paddingTop = '120px';
    targetElement.style.marginTop = '120px';
  }
});