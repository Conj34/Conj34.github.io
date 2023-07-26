var quotes = [
"Be realistic, demand the impossible.  <p><center><i>-Che Guevara-</i></center></p>", 
"It took a few years, but bit by bit, Lindy began to love me. I didn’t dare believe it at first, but after a while there was nothing else to believe.  <p><center><i>-K. Ishiguro-</i></center></p>", 
"We don't get the families we deserve.  <p><center><i>-H. Yanagihara-</i></center></p>", 
"Stepping out into the world in which no one knew him, and in which he could be anyone.  <p><center><i>-H. Yanagihara-</i></center></p>", 
"But at what point had Findlay decided he would give up acting, and how had it happened? Was it simply age? [...]. How did you know that it was time to give up? [...] How did you know when to stop? <p><center><i>-H. Yanagihara-</i></center></p>", 
"In their deaths, Willem was able to remember that he had loved them after all, and that they had taught him things he treasured knowing.  <p><center><i>-H. Yanagihara-</i></center></p>", 
"In life, sometimes nice things happen to good people. You don’t need to worry, they don’t happen as often as they should. But when they do, it’s up to the good people to just say ‘thank you,’ and move on, and maybe consider that the person who’s doing the nice thing gets a bang out of it as well. </i></center></p>", 
"[...] in the years to come he will, again and again, test Harold’s claims of devotion, will throw himself against his promises to see how steadfast they are. [...] because part of him will never believe Harold and Julia; as much as he wants to, as much as he thinks he does, he won’t, and he will always be convinced that they will eventually tire of him [...]. And so he will challenge them, because when their relationship inevitably ends, he will be able to look back and know for certain that he caused it, and not only that, but the specific incident that caused it, and he will never have to wonder, or worry, about what he did wrong, or what he could have done better.  <p><center><i>-H. Yanagihara-</i></center></p>", 
" And then I went to college, and I met people who, for whatever reason, decided to be my friends, and they taught me—everything, really. They made me, and make me, into someone better than I really am.  <p><center><i>-H. Yanagihara-</i></center></p>", 
"The only trick of friendship, I think, is to find people who are better than you are—not smarter, not cooler, but kinder, and more generous, and more forgiving—and then to appreciate them for what they can teach you, and to try to listen to them when they tell you something about yourself, no matter how bad—or good—it might be, and to trust them, which is the hardest thing of all. But the best, as well.  <p><center><i>-H. Yanagihara-</i></center></p>", 
"At least you’re in the arts. I might as well be working for an arms dealer. Dorothy Wharton asked me tonight how it felt waking up each morning knowing I’d sacrificed yet another piece of my soul the day before. <p><center><i>-H. Yanagihara-</i></center></p>", 
"Enjoying as he always did the pleasure of walking by himself, of feeling alone in a city of so many.  <p><center><i>-H. Yanagihara-</i></center></p>"]
var quote;
function newQuote() {
  var randomNumber = Math.floor(Math.random() * (quotes.length))
  
  document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber];
      quote = quotes[randomNumber];
}
newQuote();
