function passwd_1(){

  var password = prompt('Enter the password to download the file:');
  if(password.toLowerCase() == "ciao"){
    window.open("_site/images/logo.png")    
  }else{
    alert("incorrect password!! please try again");
  }
}