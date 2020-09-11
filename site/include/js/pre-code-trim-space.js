$("pre code").each(function(){
  var html = $(this).html();
  var pattern = html.match(/\s*\n\s*/);
  $(this).html(html.replace(new RegExp(pattern, "g"),'\n'));
});
