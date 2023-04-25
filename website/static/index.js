document.getElementById("addSection").addEventListener("click", function() {
    var container = document.getElementById("addContainer");
    var newSection = document.createElement("section");
	var newH1 = document.createElement("h1");
	newH1.contentEditable = true;
	newH1.textContent = "New Section";
	var newSubnotes = document.createElement("ul");
	newSubnotes.id = "subnotes";
	newSubnotes.contentEditable = true;
  newSection.style.paddingBottom = '10px';
	newSection.appendChild(newH1);
	container.appendChild(newSection);
});

document.getElementById("add").addEventListener("click", function() {
    var container = document.getElementById("overviewList");
    var list = document.createElement("li");
    list.appendChild(document.createTextNode("New Item"));
    list.contentEditable = true;
	container.appendChild(list);
});

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('Save').addEventListener('click', function() {
    var body = document.getElementById("tripcontainer").outerHTML;

    // Get the current center coordinates of the map
    var mapCenter = window.map.getCenter();
    // Log the latitude and longitude coordinates to the console
    var lat = mapCenter.lat();
    var lng = mapCenter.lng();

    // send body variable to the server using ajax: /save route as POST request
    // create a new XMLHttpRequest object
    var xhttp = new XMLHttpRequest();
    // set the callback function to handle the response
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        console.log("Response received: " + this.responseText);
      }
    };
    // open a new POST request with the Flask route as the endpoint
    xhttp.open("POST", "/save");
    // set the request header to send data as JSON
    xhttp.setRequestHeader("Content-type", "application/json");
    // send the request with the data
    // Create a data object with the body and location data
    var data = {
      body: body,
      lat: lat,
      lng: lng
    };
    xhttp.send(JSON.stringify(data));   
  });
});

var textbox = document.getElementById('boxArea');
textbox.addEventListener('input', function() {
  var currentValue = textbox.value;
});

window.map = undefined;

// Google Maps and Places function
function initAutocomplete() {
  
  window.map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -33.8688, lng: 151.2195 },
    zoom: 13,
    mapTypeId: "roadmap",
  });

  // Create the search box and link it to the UI element.
  const input = document.getElementById("pac-input");
  const searchBox = new google.maps.places.SearchBox(input);

  window.map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
  // Bias the SearchBox results towards current map's viewport.
  window.map.addListener("bounds_changed", () => {
    searchBox.setBounds(window.map.getBounds());
  });

  let markers = [];

  // Listen for the event fired when the user selects a prediction and retrieve
  // more details for that place.
  searchBox.addListener("places_changed", () => {
    const places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }

    // Clear out the old markers.
    markers.forEach((marker) => {
      marker.setMap(null);
    });
    markers = [];

    // For each place, get the icon, name and location.
    const bounds = new google.maps.LatLngBounds();

    places.forEach((place) => {
      if (!place.geometry || !place.geometry.location) {
        console.log("Returned place contains no geometry");
        return;
      }

      const icon = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25),
      };

      // Create a marker for each place.
      markers.push(
        new google.maps.Marker({
          map,
          icon,
          title: place.name,
          position: place.geometry.location,
        })
      );
      if (place.geometry.viewport) {
        // Only geocodes have viewport.
        bounds.union(place.geometry.viewport);
      } else {
        bounds.extend(place.geometry.location);
      }
    });
    window.map.fitBounds(bounds);
  });
}

window.initAutocomplete = initAutocomplete;