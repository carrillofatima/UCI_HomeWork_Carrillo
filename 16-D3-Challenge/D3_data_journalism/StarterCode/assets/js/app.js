// Import data from the CSV file
// =================================
d3.csv('./assets/data/data.csv').then(function(censusData) {
    console.log(censusData);
    //Parse Data
    censusData.forEach(function(data) {
        data.poverty = + data.poverty;
        data.healthcare = + data.healthcare;
    });

// Set up our chart
var svgWidth = 960;
var svgHeight = 500;

var margin =  {
    top: 20,
    right: 40,
    bottom: 80,
    left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

//Create an SVG wrapper
var svg = d3.select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

var chartGroup = svg.append("g")
    .attr("transform", `translate(${ margin.left}, ${ margin.top})`);


//Create Scale Functions
    var xLinearScale = d3.scaleLinear()
        .domain([20, d3.max(censusData, d => d.poverty)])
        .range([0, width]);

    var yLinearScale = d3.scaleLinear()
        .domain([20, d3.max(censusData, d => d.healthcare)])
        .range([0, width]);

//Create Axis function
var bottomAxis = d3.axisBottom(xLinearScale);
var leftAxis = d3.axisLeft(yLinearScale);

//Append axes to the chart
chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

chartGroup.append("g")
    .call(leftAxis);

//create circles
var circlesGroup = chartGroup.selectAll("circle")
    .data(censusData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.poverty))
    .attr("cy", d => yLinearScale(d.healthcare))
    .attr("r", "15")
    .attr("fill", "blue")
    .attr("Opacity", ".5")
    .classed("stateCircle", true);

//Initialize tool tip
var tooTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function(d) {
        return (`${d.abbr}<br>Healthcare (%): ${d.healthcare}%<br>Poverty: ${d.poverty}`)
    });

chartGroup.call(tooTip)

//event listener
circlesGroup.on("mouseover", function(data) {
    tooTip.show(data, this);
});
    on("mouseout", function(data, index) {
        tooTip.hide(data);
    });

//Create axes labels
chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 30)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Lacks Healthcare (%)");

    chartGroup.append("text")
    .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
    .attr("class", "axisText")
    .text("In Poverty (%)");
    
}).catch(function(error) {
  console.log(error);
      
    

});
  
  

    




















 