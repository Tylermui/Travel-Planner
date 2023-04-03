document.getElementById("add").addEventListener("click", function() {
    var container = document.getElementById("addContainer");
    var newSection = document.createElement("section");
	var newH1 = document.createElement("h1");
	newH1.contentEditable = true;
	newH1.textContent = "New Section";
	var newSubnotes = document.createElement("div");
	newSubnotes.className = "subnotes";
	newSubnotes.contentEditable = true;
	newSection.appendChild(newH1);
	newSection.appendChild(newSubnotes);
	container.appendChild(newSection);
});
