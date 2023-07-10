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
  const breadcrumbMargin = document.getElementById('post-breadcrumb');
  let isExpanded = navbarCollapse.classList.contains("show");
  if (isExpanded) {
      navbarCollapse.classList.remove("show")
      navMarginMob.classList.remove('nav-margin-mobile')
      navMarginTab.classList.remove('nav-margin-tablet')
      breadcrumbMargin.classList.remove('d-none')
      navMarginMob.classList.add('nav-margin-mobile-short')
      navMarginTab.classList.add('nav-margin-tablet-short')

  } else {
      navbarCollapse.classList.add("show")
      navMarginMob.classList.add('nav-margin-mobile')
      navMarginTab.classList.add('nav-margin-tablet');
      breadcrumbMargin.classList.add('d-none');
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


// POST BACKGROUND AUDIO
// Define the functions outside the addEventListener block
function playPostAudio() {
  const audioElement = document.getElementById('post-audio');
  audioElement.play();
  audioElement.volume = 0.4
  const playButton = document.getElementById('play-post-background');
  const stopButton = document.getElementById('stop-post-background');
  playButton.style.display = 'none';
  stopButton.style.display = 'inline';
  audioElement.style.display = 'none';
}

function stopPostAudio() {
  const audioElement = document.getElementById('post-audio');
  audioElement.pause();
  audioElement.currentTime = 0;
  const stopButton = document.getElementById('stop-post-background');
  const playButton = document.getElementById('play-post-background');
  audioElement.style.display = 'none';
  stopButton.style.display = 'none';
  playButton.style.display = 'inline';
}

window.addEventListener('load', function () {
  const playPostButton = document.getElementById('play-post-background');
  const stopPostButton = document.getElementById('stop-post-background');

  playPostButton.addEventListener('click', playPostAudio);
  stopPostButton.addEventListener('click', stopPostAudio);
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

// CREATE & EDIT POST SAVE MODAL
function modalEditPostActivate() {
  $('#edit-post-save').modal('toggle');
}

function modalEditPostClose() {
  $('#edit-post-save').modal('hide');
}


// STOCKS OFFER MODAL
function modalStocksActivate() {
  $('#stocks-modal').modal('toggle');
}

function modalStocksClose() {
  $('#stocks-modal').modal('hide');
}

// OWNERSHIP PERCENTAGE OFFER MODAL
function modalOwnershipPctActivate() {
  $('#ownership-pct-modal').modal('toggle');
}

function modalOwnershipPctClose() {
  $('#ownership-pct-modal').modal('hide');
}

// PRODUCTS OR SERVICES OFFER MODAL
function modalProductsServicesActivate() {
  $('#products-services-modal').modal('toggle');
}

function modalProductsServicesClose() {
  $('#products-services-modal').modal('hide');
}

// LIFETIME DISCOUNT OFFER MODAL
function modalLifetimeDiscountActivate() {
  $('#lifetime-discount-modal').modal('toggle');
}

function modalLifetimeDiscountClose() {
  $('#lifetime-discount-modal').modal('hide');
}

// GUARANTEED TEAM POSITION OFFER MODAL
function modalGuaranteedTeamActivate() {
  $('#team-position-modal').modal('toggle');
}

function modalGuaranteedTeamClose() {
  $('#team-position-modal').modal('hide');
}

// PARTNERSHIPS OFFER MODAL
function modalPartnershipsActivate() {
  $('#partnerships-modal').modal('toggle');
}

function modalPartnershipsClose() {
  $('#partnerships-modal').modal('hide');
}

// COLLABORATIONS OFFER MODAL
function modalCollaborationsActivate() {
  $('#collaborations-modal').modal('toggle');
}

function modalCollaborationsClose() {
  $('#collaborations-modal').modal('hide');
}

// SPONSORSHIPS OFFER MODAL
function modalSponsorshipsActivate() {
  $('#sponsorships-modal').modal('toggle');
}

function modalSponsorshipsClose() {
  $('#sponsorships-modal').modal('hide');
}

// OPEN OFFER MODAL
function modalOpenOfferActivate() {
  $('#open-offer-modal').modal('toggle');
}

function modalOpenOfferClose() {
  $('#open-offer-modal').modal('hide');
}

$(document).ready(function() {
  // Enable tooltip functionality
  $('[data-toggle="tooltip"]').tooltip();

  // Enable popover functionality
  $('[data-bs-toggle="popover"]').popover({
    trigger: 'focus'
  });
});

// let popover;

// document.addEventListener('DOMContentLoaded', function() {
//   const profileExamplePopover = document.getElementById('profile-example');
//   popover = new bootstrap.Popover(profileExamplePopover);


//   })

// function showPopover() {

//   // Destroy previous popover instance
//   if (popover) {
//     console.log('profileExamplePopover exists')
//     popover.hide();
//     console.log('profileExamplePopover disposed')
//   }
  
//   // Create new popover instance
//   popover.show();
//   console.log('popover shown')
// }

// function closePopover() {
//   popover.hide();
// }



function showPopover() {

  const profileExamplePopover = document.getElementById('profile-example');
  let popover = new bootstrap.Popover(profileExamplePopover);
  
  // Destroy previous popover instance
  if (popover) {
    console.log('profileExamplePopover exists')
    popover.show();
    console.log('profileExamplePopover disposed')
  } else {
    // / Create new popover instance;
    popover.hide();
    console.log('popover shown')
  }
  
}

// function closePopover() {
//   const profileExamplePopover = document.getElementById('profile-example');
//   const popover = new bootstrap.Popover(profileExamplePopover);
//   popover.hide();
// }


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

// EDIT PROFILE COLLAPSES

// EDIT PRIVACY COLLAPSE
function editProfilePrivacy() {
  let editPopover = document.getElementById('edit-privacy');
  let editPopoverButton = document.getElementById('edit-privacy-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");

  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// EDIT CARD COLLAPSE
function editProfileCard() {
  let editPopover = document.getElementById('edit-card');
  let editPopoverButton = document.getElementById('edit-card-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// EDIT VIDEO COLLAPSE
function editProfileVideo() {
  let editPopover = document.getElementById('edit-video');
  let editPopoverButton = document.getElementById('edit-video-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// EDIT GENERAL COLLAPSE
function editProfileGeneral() {
  let editPopover = document.getElementById('edit-general');
  let editPopoverButton = document.getElementById('edit-general-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// EDIT OCCUPATION COLLAPSE
function editProfileOccupation() {
  let editPopover = document.getElementById('edit-occupation');
  let editPopoverButton = document.getElementById('edit-occupation-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// EDIT CAREER COLLAPSE
function editProfileCareer() {
  let editPopover = document.getElementById('edit-career');
  let editPopoverButton = document.getElementById('edit-career-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// EDIT ACHIEVEMENTS COLLAPSE
function editProfileAchievements() {
  let editPopover = document.getElementById('edit-achievements');
  let editPopoverButton = document.getElementById('edit-achievements-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// EDIT ATTRIBUTES COLLAPSE
function editProfileAttributes() {
  let editPopover = document.getElementById('edit-attributes');
  let editPopoverButton = document.getElementById('edit-attributes-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// EDIT BUSINESS FOCUS COLLAPSE
function editProfileFocus() {
  let editPopover = document.getElementById('edit-focus');
  let editPopoverButton = document.getElementById('edit-focus-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// EDIT BUSINESS SPECIALIZATIONS COLLAPSE
function editProfileSpecialization() {
  let editPopover = document.getElementById('edit-specializations');
  let editPopoverButton = document.getElementById('edit-specializations-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// EDIT ACCOMPLISHMENTS COLLAPSE
function editProfileAccomplishments() {
  let editPopover = document.getElementById('edit-accomplishments');
  let editPopoverButton = document.getElementById('edit-accomplishments-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// EDIT REWARDSL COLLAPSE
function editProfileRewards() {
  let editPopover = document.getElementById('edit-rewards');
  let editPopoverButton = document.getElementById('edit-rewards-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// EDIT PERSONAL WALL COLLAPSE
function editProfileWall() {
  let editPopover = document.getElementById('edit-wall');
  let editPopoverButton = document.getElementById('edit-wall-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// CREATE & EDIT POST COLLAPSES

// POST POSTLIST VIEW COLLAPSE
function editPostListView() {
  let editPopover = document.getElementById('post-list-view');
  let editPopoverButton = document.getElementById('post-list-view-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");

  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST STRUCTURE COLLAPSE
function editPostStructure() {
  let editPopover = document.getElementById('post-structure');
  let editPopoverButton = document.getElementById('post-structure-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST KEY INFO COLLAPSE
function editPostKeyInfo() {
  let editPopover = document.getElementById('post-key-info');
  let editPopoverButton = document.getElementById('post-key-info-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST GENERAL INFO COLLAPSE
function editPostGeneral() {
  let editPopover = document.getElementById('post-general');
  let editPopoverButton = document.getElementById('post-general-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST INTRODUCTION COLLAPSE
function editPostIntroduction() {
  let editPopover = document.getElementById('post-intro');
  let editPopoverButton = document.getElementById('post-intro-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST VIDEO COLLAPSE
function editPostVideo() {
  let editPopover = document.getElementById('post-video');
  let editPopoverButton = document.getElementById('post-video-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST LAUNCH COLLAPSE
function editPostLaunch() {
  let editPopover = document.getElementById('post-launch');
  let editPopoverButton = document.getElementById('post-launch-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST DETAILS COLLAPSE
function editPostDetails() {
  let editPopover = document.getElementById('post-details');
  let editPopoverButton = document.getElementById('post-details-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST ABOUT CREATORS COLLAPSE
function editPostAboutCreators() {
  let editPopover = document.getElementById('post-about-creators');
  let editPopoverButton = document.getElementById('post-about-creators-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST MAIN CONTENT COLLAPSE
function editPostBody() {
  let editPopover = document.getElementById('post-body');
  let editPopoverButton = document.getElementById('post-body-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST LIBRARY COLLAPSE
function editPostLibrary() {
  let editPopover = document.getElementById('post-library');
  let editPopoverButton = document.getElementById('post-library-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST DOCUMENTS COLLAPSE
function editPostDocuments() {
  let editPopover = document.getElementById('post-documents');
  let editPopoverButton = document.getElementById('post-documents-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST PROPOSAL COLLAPSE
function editPostProposal() {
  let editPopover = document.getElementById('post-proposal');
  let editPopoverButton = document.getElementById('post-proposal-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}

// POST CONTACT COLLAPSE
function editPostContact() {
  let editPopover = document.getElementById('post-contact');
  let editPopoverButton = document.getElementById('post-contact-bttn');
  let isExpanded = editPopover.classList.contains("collapse");
  if (isExpanded) {
    editPopover.classList.remove("collapse");
    editPopoverButton.classList.add("bg-warning");
  } else {
    editPopover.classList.add("collapse");
    editPopoverButton.classList.remove("bg-warning");
     // Set the desired background color with important
  }
}



// Attach scroll event listener to update the active link on scroll
window.addEventListener('scroll', updateActiveLink);

$(document).ready(function(){
  $("body").scrollspy({
      target: "#profile-occupation"
  }) 
  $('#profile-personal-occupation').addClass('bg-warning');
});


function addBounceClass(elementId) {
  const element = document.getElementById(elementId);
  if (element) {
    element.classList.add('fa-bounce');
    setTimeout(() => {
      element.classList.remove('fa-bounce');
    }, 900);
  }
}

function addShakeClass(elementId) {
  const element = document.getElementById(elementId);
  if (element) {
    element.classList.add('fa-shake');
    setTimeout(() => {
      element.classList.remove('fa-shake');
    }, 900);
  }
}

function addBeatClass(elementId) {
  const element = document.getElementById(elementId);
  if (element) {
    element.classList.add('fa-beat');
    setTimeout(() => {
      element.classList.remove('fa-beat');
    }, 900);
  }
}

var postNavButton = document.getElementById("post-nav-button");
  if (postNavButton.classList.contains("bg-dark")) {
    postNavButton.classList.add("text-warning");
    postNavButton.classList.remove("text-dark");
    postNavButton.classList.remove("text-muted");
  } else {
    postNavButton.classList.add("text-dark");
    postNavButton.classList.add("text-muted");
    postNavButton.classList.remove("text-warning");
  }

