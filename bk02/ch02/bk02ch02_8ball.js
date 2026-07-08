document.addEventListener('DOMContentLoaded', function () {
  let question = prompt('Ask magic 8 ball a question');
  let answer = Math.floor(Math.random() * 8) + 1;
  if (answer == 1) {
    alert('It is certain');
  } else if (answer == 2) {
    alert('Outlook good');
  } else if (answer == 3) {
    alert('You may rely on it');
  } else if (answer == 4) {
    alert('Ask again later');
  } else if (answer == 5) {
    alert('Concentrate and ask again');
  } else if (answer == 6) {
    alert('Reply hazy, try again');
  } else if (answer == 7) {
    alert('My reply is no');
  } else if (answer == 8) {
    alert('My sources say no');
  }
});
