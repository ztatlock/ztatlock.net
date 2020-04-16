
var yd = new Date(new Date().setDate(new Date().getDate()-1));
var yd_iso = yd.toISOString().substring(0, 10);

location.href =  "https://mail.google.com/mail/u/0/#search/in%3Ainbox++after%3A" + yd_iso;


http://ted.mielczarek.org/code/mozilla/bookmarklet.html


