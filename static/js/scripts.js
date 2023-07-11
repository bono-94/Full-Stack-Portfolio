// DROPDOWN
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

// POST & PROFILE AUDIO
// PLAYING PROFILE AUDIO
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

// STOPPING PROFILE AUDIO
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

// DEFINING PRODFILE AUDIO BUTTONS ON LOAD
window.addEventListener('load', function () {
  const playButton = document.getElementById('play-user-profile');
  const stopButton = document.getElementById('stop-user-profile');

  playButton.addEventListener('click', playAudio);
  stopButton.addEventListener('click', stopAudio);
});

// POST AUDIO PLAY
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

// STOPPING POST AUDIO
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

// NAVBARS
// CLOSING PROFILE NAVIGATION

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

// SAVING MODAL
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

// IF COLLAPSED CHECKER
function isCollapsed(elementId) {
  let element = document.getElementById(elementId);
  return element.classList.contains('collapse');
}


// PROFILE NAVIGATION COLLAPSE
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
  }
}

// EDIT REWARDS COLLAPSE
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
  }
}

// FONT AWESOME ANIMATIONS
// BOUNCE
function addBounceClass(elementId) {
  const element = document.getElementById(elementId);
  if (element) {
    element.classList.add('fa-bounce');
    setTimeout(() => {
      element.classList.remove('fa-bounce');
    }, 900);
  }
}

// SHAKE
function addShakeClass(elementId) {
  const element = document.getElementById(elementId);
  if (element) {
    element.classList.add('fa-shake');
    setTimeout(() => {
      element.classList.remove('fa-shake');
    }, 900);
  }
}

// BEAT
function addBeatClass(elementId) {
  const element = document.getElementById(elementId);
  if (element) {
    element.classList.add('fa-beat');
    setTimeout(() => {
      element.classList.remove('fa-beat');
    }, 900);
  }
}

// BASE DOCUMENT STYLING
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

