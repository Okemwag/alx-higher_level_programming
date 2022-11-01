// JavaScript script that fetches from url and displays the value of hello from that fetch in the HTML tag DIV#hello
$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  $('#hello').text(data.hello);
});
