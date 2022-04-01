// Set the date we're counting down to
var countDownDate = new Date("Apr 1, 2022 13:00:00").getTime();
    
// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();
    
  // Find the distance between now and the count down date
  var distance = countDownDate - now;
    
  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
  // Output the result in an element with id="demo"
  document.getElementById("demo").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";
    
  // If the count down is over, write some text 
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "EXPIRED";
  }
}, 1000);

function playH() {
  var audio = document.getElementById("audioH");
  audio.pause();
  audio.currentTime = 0;
  audio.play();
}
function playK() {
  var audio = document.getElementById("audioK");
  audio.pause();
  audio.currentTime = 0;
  audio.play();
}
function playL() {
  var audio = document.getElementById("audioL");
  audio.pause();
  audio.currentTime = 0;
  audio.play();
}

function co2Rechnen(){

  let x = document.getElementById("kmInput").value;
  let ergebnis = "<table class='blueTable'><thead>";
  ergebnis += "<tr>";
  ergebnis += "<th>Auto</th>";
  ergebnis += "<th>E-Bike</th>";
  ergebnis += "<th>Rad</th>";
  ergebnis += "</tr></thead>";
  ergebnis += "<tbody><tr>";
  ergebnis += "<td>" + x*165 + "g </td>"; 
  ergebnis += "<td>" + x*22 + "g </td>"; 
  ergebnis += "<td>" + x*21 + "g </td>";
  ergebnis += "</tbody></tr></table>";
  
  document.getElementById("ergebnis").innerHTML = ergebnis;
}

//grün 47.8 71 11.4