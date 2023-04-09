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

function untoggleNavbar() {
  $('#navbarCollapse').removeClass('navbar-collapse');
}
