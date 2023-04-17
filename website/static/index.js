document.getElementById("addSection").addEventListener("click", function() {
    var container = document.getElementById("addContainer");
    var newSection = document.createElement("section");
	var newH1 = document.createElement("h1");
	newH1.contentEditable = true;
	newH1.textContent = "New Section";
	var newSubnotes = document.createElement("ul");
	newSubnotes.id = "subnotes";
	newSubnotes.contentEditable = true;
	newSection.appendChild(newH1);
	newSection.appendChild(newSubnotes);
	container.appendChild(newSection);
});

document.getElementById("add").addEventListener("click", function() {
    var container = document.getElementById("overviewList");
    var list = document.createElement("li");
    list.appendChild(document.createTextNode("New Item"));
    list.contentEditable = true;
	container.appendChild(list);
});


document.getElementById('trip').addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    // Here you can submit the form or trigger a function
    const inputValue = this.innerText;
    const words = inputValue.split(" ")    
    document.getElementById('banner').style.backgroundImage = 
          "url('https://source.unsplash.com/1600x900/?" + words[2] + "')";
  }  
});

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('Save').addEventListener('click', function() {
    var body = document.body.innerHTML;
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
    xhttp.setRequestHeader("Content-type", "text/plain");
    // send the request with the data
    xhttp.send(body);    
  });
});