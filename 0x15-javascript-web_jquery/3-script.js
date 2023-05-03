// Import jQuery library
import $ from 'jquery';

// Get the DIV#red_header tag using jQuery
const redHeader = $('DIV#red_header');

// Add a click event listener to the DIV#red_header tag
redHeader.click(() => {
  // Get the header element using jQuery and add the "red" class to it
  $('header').addClass('red');
});
