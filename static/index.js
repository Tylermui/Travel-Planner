document.getElementById("add").addEventListener("click", function() {
      var newTextbox = document.createElement("input");
      newTextbox.type = "text";
      var container = document.getElementById("addContainer");
      container.appendChild(newTextbox);
});
