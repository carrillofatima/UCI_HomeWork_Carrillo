// from data.js
var tableData = data;

//Level 2: Multiple Search Categories
var tbody = d3.select("tbody");

// Another method to add the whole table of ufo sightings data when loading the page
tableData.forEach((report) => {
    var row = tbody.append("tr");
    Object.entries(report).forEach(([key, value]) => {
        var cell = row.append("td");
        cell.text(value);
    });
});

// Select the button
var button = d3.select("#filter-btn");

// Select the form
var form = d3.select("form");

// Create event handlers 
button.on("click", runEnter);
form.on("submit", runEnter);

// Complete the event handler function for the form
function runEnter() {
// Clear out current contents in the table
tbody.html("");
  

  // Select the input element and get the raw HTML node
  var date = d3.select("#datetime").property("value");
  var city = d3.select("#city").property("value");
  var state = d3.select("#state").property("value");
  var country = d3.select("#country").property("value");
  var shape = d3.select("#shape").property("value");

  
// Prevent the page from refreshing
d3.event.preventDefault();
	// If date provided is true then
	if (date) {
		filterdata = data.filter(ufoDate => ufoDate.datetime === date)
		console.log(filterdata)

		// tbody.text(`There are no UFO sightings on ${inputValue}.`);
	}
	if (city) {
		filterdata = data.filter(ufoCity => ufoCity.city === city)
		console.log(filterdata)
	}
	if (state) {
		filterdata = data.filter(ufoState => ufoState.state === state)
		console.log(filterdata)
	}
	if (country) {
		filterdata = data.filter(ufoCountry => ufoCountry.country === country)
		console.log(filterdata)
	}
	if (shape) {
		filterdata = data.filter(ufoShape => ufoShape.shape === shape)
		console.log(filterdata)
	}
	if (filterdata.length == 0) {
		d3.select("#message")
		console.log(filterdata)
	}
	// Handle matching results
	else {
		d3.select("#message").text("")

		}
	filterdata.forEach((ufo) => {
			var row = tbody.append("tr");
			Object.entries(ufo).forEach(([key, value]) => {
				var cell = row.append("td");
				cell.text(value);
			});
		});
//Emptying the input fields
$("#datetime").val("");
$("#city").val("");
$("#state").val("");
$("#country").val("");
$("#shape").val("");

	};
