var quotes = ["When I die, I want to go peacefully like my grandfather did–in his sleep. Not yelling and screaming like the passengers in his car.  <p><center>ABC</center></p>", "I have six locks on my door all in a row. When I go out, I lock every other one. I figure no matter how long somebody stands there picking the locks, they are always locking three.  <p><center>DEF</center></p>"]
var quote;
function newQuote() {
  var randomNumber = Math.floor(Math.random() * (quotes.length))
  
  document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber];
      quote = quotes[randomNumber];
}
newQuote();
