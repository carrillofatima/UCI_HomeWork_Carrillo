function Responsive(){
//Set up our chart
var svgWidth = 560;
var svgHeight =100;

var svgArea = d3.select("body").select("svg");
//clear svg 
if (!svgArea.empty()){
    svgArea.remove()
}

var margin =  {
    top: 10,
    right: 10,
    bottom: 90,
    left: 90
};

var svgWidth = window.innerWidth; 
var svgHeight = window.innerHeight;

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;
console.log(height)

//SVG element
var svg = d3
    .select("#scatter")
    .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth);

var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);
//Initial Params
var chosenXAxis = 'poverty';
var chosenYAxis = 'healthcare';

//function used for updating x-scale var upon click on axis label
function xScale(censusData, chosenXAxis) {
    var xLinearScale = d3.scaleLinear()
        .domain([d3.min(censusData, d => d[chosenXAxis] * 0.9), 
        d3.max(censusData, d => d[chosenXAxis] * 1.1)])
        .range([0, width]);
        
        return xLinearScale;
}
// function used for updating xAxis var upon click on axis label
function renderAxeX(newXScale, xAxis) {
    var bottomAxis = d3.axisBottom(newXScale);

    xAxis.transition()
        .duration(1000)
        .call(bottomAxis);
    
    return xAxis;
}
function yScale(censusData, chosenYAxis) {
    var yLinearScale = d3.scaleLinear()
        .domain([d3.min(censusData, d => d[chosenYAxis] * 0.9),
        d3.max(censusData, d => d[chosenYAxis] * 1.1)])
        .range([height, 0]);

        return yLinearScale;
}
// function used for updating yAxis var upon click on axis label
function renderAxeY(newYScale, yAxis) {
    var leftAxis = d3.axisLeft(newYScale);

    yAxis.transition()
        .duration(1000)
        .call(leftAxis);
    
    return yAxis;
}

// function used for updating circles group with a transition to new circles on XAxis 
function renderCircles(circlesGroup, newXScale, chosenXAxis) {

    circlesGroup.transition()
        .duration(1000)
        .attr("cx", d => newXScale(d[chosenXAxis]));
    
    return circlesGroup;
}
// function used for updating circles group with a transition to new circles on YAxis 
function renderCirclesY(circlesGroup, newYScale, chosenYAxis) {

    circlesGroup.transition()
        .duration(1000)
        .attr("cy", d => newYScale(d[chosenYAxis]) + 5);
    
    return circlesGroup;
}

//function for adding text in circles
function renderCirclesText(textCirclesGroup, newXScale, chosenXAxis) {
    textCirclesGroup.transition()
        .duration(1000)
        .attr("x", d => newXScale(d[chosenXAxis]));
    
    return textCirclesGroup;

}
function renderCirclesTextY(textCirclesGroup, newYScale, chosenYAxis) {
    textCirclesGroup.transition()
        .duration(1000)
        .attr("y", d => newYScale(d[chosenYAxis]) + 3);
    
    return textCirclesGroup;

}

// function used for updating circles group with new tooltip
function updateToolTip(chosenXAxis, chosenYAxis, circlesGroup) {
    
    var xlabel
    var ylabel

    if (chosenXAxis === 'poverty') {
        xlabel = "Poverty";
    }
        else if (chosenXAxis === 'age') {
            xlabel = "Age";
    }

    else {
        xlabel = "Household Income";
    }

    if (chosenYAxis === 'obesity') {
        ylabel = "Obesity";
    }
        else if (chosenYAxis === "smokes") {
            ylabel = "Smokers";
        }
    else {
        ylabel = "Lacks HealthCare"
    }

    var toolTip = d3.tip()
        .attr("class", "d3.tip")
        .offset([80, -60])
        .html(function(d) {
            return (`${d.state}<br>${xlabel}${d[chosenXAxis]}<br>${ylabel} ${d[chosenYAxis]}`);
        });
    circlesGroup.call(toolTip);
    
    circlesGroup.on("mouseover", function(data) {
        toolTip.show(data, this);
    })
    //Onmouseout event
    .on("mouseout", function(data, index) {
        toolTip.hide(data);
    });

    return circlesGroup;

}
// Import data from the CSV file
// =================================
d3.csv('assets/data/data.csv').then(function(censusData) {
    // console.log(censusData);
    //Parse Data
    censusData.forEach(function(data) {
        data.poverty = + data.poverty;
        data.age = + data.age;
        data.income = + data.income;
        data.obesity = + data.obesity;
        data.smokes = + data.smokes;
        data.healthcare = + data.healthcare;
    });

console.log(censusData)
//XLinear scale / Ylinear scale
var xLinearScale = xScale(censusData, chosenXAxis);
var yLinearScale = yScale(censusData, chosenYAxis);

var bottomAxis = d3.axisBottom(xLinearScale)
var leftAxis = d3.axisLeft(yLinearScale)

//append xAxis
var xAxis = chartGroup.append("g")
    .classed("x-axis", true)
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);
// append y axis
var yAxis = chartGroup.append("g")
    .call(leftAxis);
  // append initial circles
  var circlesAll = chartGroup.selectAll("circlesGroup")
    .data(censusData)
    .enter()
    var circlesGroup = circlesAll
    .append("circle")
    .attr("cx", d => xLinearScale(d[chosenXAxis]))
    .attr("cy", d => yLinearScale(d[chosenYAxis]))
    .attr("r", 15)
    .classed("stateCircle callTip", true)
    .attr("fill", "pink")
    .attr("opacity", ".5");
//Add text to each circle
var textCirclesGroup = circlesAll
.append("text")
.text(d => d.abbr)
.attr("x", d => xLinearScale(d[chosenXAxis]))
.attr("y", d => yLinearScale(d[chosenYAxis])+3)
// .attr("r", 20)
.classed("stateText callTip", true)
.attr("fill", "black")
.attr("opacity", ".5");


  // Create group for three x-axis labels
  var labelsGroup = chartGroup.append("g")
    .attr("transform", `translate(${width / 2}, ${height + 20})`);
    
    var povertyLabel = labelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("value", "poverty") // value to grab for event listener
    .classed("active", true)
    .text("Poverty");

    var ageLabel = labelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 40)
    .attr("value", "age") // value to grab for event listener
    .classed("inactive", true)
    .text("Age(Median)");

    var householdIncomeLabel = labelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 60)
    .attr("value", "income") // value to grab for event listener
    .classed("inactive", true)
    .text("Household Income(Median");

   // Create group for three y-axis labels
   var labelsGroupY = chartGroup.append("g")
   .attr("transform", "rotate(-90)");

   var obeseLabel = labelsGroupY.append("text")
    .attr("x", -height/2)
    .attr("y", -70)
    .attr("dy","1em")
    .attr("value", "obesity") // value to grab for event listener
    .classed("inactive", true)
    .text("Obesse(%)");

    var smokesLabel = labelsGroupY.append("text")
    .attr("x", -height/2)
    .attr("y", -50)
    .attr("dy", "1em")
    .attr("value", "smokes") // value to grab for event listener
    .classed("inactive", true)
    .text("Smokes(%)");

    var healthcareLabel = labelsGroupY.append('text')
    .attr('x', -height/2)
    .attr("y", -90)
    .attr("dy", "1em")
    .attr("value", "healthcare") // value to grab for event listener
    .classed("active", true)
    .text("Lacks Healthcare(%)");

    //var tipGroup = d3.selectAll(".callTip")

    //Update toolTip
    var circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circlesGroup);
    //xaxis labels event listern
    labelsGroup.selectAll("text").on("click", function(){
        //fetch the value
        var value = d3.select(this).attr("value")
          if (value !== chosenXAxis){
              chosenXAxis = value
              //update x scale
              xLinearScale = xScale(censusData, chosenXAxis)
              //update xAxis
              xAxis = renderAxeX(xLinearScale, xAxis)
              //update circles
              circlesGroup = renderCircles(circlesGroup, xLinearScale, chosenXAxis)
              textCirclesGroup = renderCirclesText(textCirclesGroup, xLinearScale, chosenXAxis)
              circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circlesGroup)
              //change classes
              if (chosenXAxis === 'age'){
                  ageLabel.classed("active", true)
                  .classed("inactive", false)
                  povertyLabel.classed("active", false)
                  .classed("inactive", true)
                  householdIncomeLabel.classed("active", false)
                  .classed("inactive", true)
              }
              else if (chosenXAxis === 'poverty'){
                  ageLabel.classed("active", false)
                  .classed("inactive", true)
                  povertyLabel.classed("active", true)
                  .classed("inactive", false)
                  householdIncomeLabel.classed("active", false)
                  .classed("inactive", true)
              }
              else {
              ageLabel.classed("active", false)
              .classed("inactive", true)
              povertyLabel.classed("active", false)
              .classed("inactive", true)
              householdIncomeLabel.classed("active", true)
              .classed("inactive", false)
          }
      }
      });
      labelsGroupY.selectAll("text").on("click", function(){
          //fetch the value
          var value = d3.select(this).attr("value")
          if (value !== chosenYAxis){
              chosenYAxis = value
              //update x scale
              yLinearScale = yScale(censusData, chosenYAxis)
              //update xAxis
              yAxis = renderAxeY(yLinearScale, yAxis)
              //update circles
              circlesGroup = renderCirclesY(circlesGroup, yLinearScale, chosenYAxis)
              textCirclesGroup = renderCirclesTextY(textCirclesGroup, yLinearScale, chosenYAxis)
              circlesGroup = updateToolTip(chosenXAxis, chosenYAxis, circlesGroup)
              //change classes
              if (chosenYAxis === 'healthcare'){
                  healthcareLabel.classed("active", true)
                  .classed("inactive", false)
                  smokesLabel.classed("active", false)
                  .classed("inactive", true)
                  obeseLabel.classed("active", false)
                  .classed("inactive", true)
              }
              else if (chosenXAxis === 'smokes'){
                  healthcareLabel.classed("active", false)
                  .classed("inactive", true)
                  smokesLabel.classed("active", true)
                  .classed("inactive", false)
                  obeseLabel.classed("active", false)
                  .classed("inactive", true)
              }
              else {
              healthcareLabel.classed("active", false)
              .classed("inactive", true)
              smokesLabel.classed("active", false)
              .classed("inactive", true)
              obeseLabel.classed("active", true)
              .classed("inactive", false)
          }
      }
  })
  }).catch(function(error){console.log(error)});}
  Responsive();
  d3.select(window).on("resize", Responsive);