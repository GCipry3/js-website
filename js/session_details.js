// get current date and time
var dateTime = new Date().toLocaleString();

// get URL
var url = window.location.href;

// get location
var location = "";
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(function(position) {
    location = "Latitude: " + position.coords.latitude + ", Longitude: " + position.coords.longitude;
    document.getElementById("current_location").innerHTML = location;
  });
} else {
  location = "Location information is not available";
  document.getElementById("current_location").innerHTML = location;
}

// get browser name and version
var browser = window.navigator.userAgent;
var browserName = browser.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i)[1];
var browserVersion = browser.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i)[2];
document.getElementById("current_name_and_browser_version").innerHTML = browserName + " version " + browserVersion;

// get operating system
var operatingSystem = window.navigator.platform;
document.getElementById("current_os").innerHTML = operatingSystem;

// display information in headers
document.getElementById("current_data").innerHTML = "Date: " + dateTime.split(",")[0];
document.getElementById("current_time").innerHTML = "Time: " + dateTime.split(",")[1];
document.getElementById("current_url").innerHTML = "URL: " + url;

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

