var music = [
"Under Pressure  <p><center><i>-Queen, David Bowie-</i></center></p>",
"Don Chisciotte  <p><center><i>-Francesco Guccini-</i></center></p>",
"Vedi Cara  <p><center><i>-Francesco Guccini-</i></center></p>",
"Dio è morto  <p><center><i>-Francesco Guccini-</i></center></p>",
"L'avvelenata  <p><center><i>-Francesco Guccini-</i></center></p>",
"Brothers in Arms  <p><center><i>-Club For Five-</i></center></p>",
"La ballata del Miché  <p><center><i>-Fabrizio De André-</i></center></p>",
"Amore che vieni, amore che vai  <p><center><i>-Fabrizio De André-</i></center></p>",
"Girl from the North Country  <p><center><i>-Bob Dylan, Johnny Cash-</i></center></p>",
"Unchained Melody  <p><center><i>-The Righteous Brothers-</i></center></p>",
"Tears in Heaven  <p><center><i>-Eric Clapton-</i></center></p>",
"Wonderful Tonight  <p><center><i>-Eric Clapton-</i></center></p>",
"Canzone del Maggio  <p><center><i>-Fabrizio De André-</i></center></p>",
"Locked out  <p><center><i>-S-X, KSI-</i></center></p>",
"Dark as a Dungeon  <p><center><i>-Tennessee Ernie Ford-</i></center></p>",
"Apocalypse  <p><center><i>-Cigarettes After Sex-</i></center></p>",
"All of Me  <p><center><i>-John Legend-</i></center></p>",
"Plastic Heart  <p><center><i>-Nostalghia, et. al.-</i></center></p>",
"Happy Heart  <p><center><i>-Andy Williams-</i></center></p>",
"July  <p><center><i>-Noah Cyrus-</i></center></p>",
"I Got a Name  <p><center><i>-Jim Croce-</i></center></p>",
"Right Here Waiting  <p><center><i>-Richard Marx-</i></center></p>",
"Ovunque Sarai  <p><center><i>-Irama-</i></center></p>",
"Before You Go  <p><center><i>-Lewis Capaldi-</i></center></p>",
"Twist in My Sobriety <p><center><i>-Tanita Tikaram-</i></center></p>",
"I Want to Break Free <p><center><i>-Queen-</i></center></p>",
"Stand by Me <p><center><i>-Ben E. King-</i></center></p>",
"Better Days <p><center><i>-Dermot Kennedy-</i></center></p>",
"Happiness in Liquid Form <p><center><i>-Alfie Templeman-</i></center></p>",
"Magic City <p><center><i>-Gorillaz-</i></center></p>",
"Survivin'<p><center><i>-Bastille-</i></center></p>",
"Little Bit of Love<p><center><i>-Tom Grennan-</i></center></p>",
"I Will Wait<p><center><i>-Mumford & Sons-</i></center></p>",
"Stubborn Love<p><center><i>-The Lumineers-</i></center></p>",
"Dirty Paws<p><center><i>-Of Monsters and Men-</i></center></p>",
"Break My Heart<p><center><i>-Dua Lipa-</i></center></p>",
"Think About Things<p><center><i>-Daði Freyr-</i></center></p>",
"Via del Campo  <p><center><i>-Fabrizio De André-</i></center></p>",
"Il Gorilla <p><center><i>-Fabrizio De André-</i></center></p>",
"Un Medico <p><center><i>-Fabrizio De André-</i></center></p>",
"Mermaids On Acid <p><center><i>-Sedef Adasi-</i></center></p>",
"Starman <p><center><i>-David Bowie-</i></center></p>",
"Hurt <p><center><i>-Johnny Cash-</i></center></p>",
"Dance Me to the End of Love <p><center><i>-Leonard Cohen-</i></center></p>",
"Bird on the Wire <p><center><i>-Leonard Cohen-</i></center></p>",
"If it Be Your Will <p><center><i>-Leonard Cohen-</i></center></p>",
"Anomaly <p><center><i>-Frede-</i></center></p>",
"Nothing Compares 2 U <p><center><i>-Sinéad O'Connor-</i></center></p>",
"Walk on the Wild Side <p><center><i>-Lou Reed-</i></center></p>",
"Vincent <p><center><i>-Don McLean-</i></center></p>",
"Respect <p><center><i>-Aretha Franklin-</i></center></p>",
"I Say a Little Prayer <p><center><i>-Aretha Franklin-</i></center></p>",
"Blinding Lights <p><center><i>-The Weeknd-</i></center></p>",
"I Just Called to Say I Love You <p><center><i>-Stevie Wonder-</i></center></p>",
"What a Wonderful World <p><center><i>-Luis armstrong-</i></center></p>",
]
var quote;
function newMusic() {
  var randomNumber = Math.floor(Math.random() * (music.length))
  
  document.getElementById('musicDisplay').innerHTML = music[randomNumber];
      quote = music[randomNumber];
}
newMusic();









