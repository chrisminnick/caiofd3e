/*
 * Prompt: Write a JavaScript module for a multiple-choice trivia game.
 * The script should load questions from a globally available `triviaData` array,
 * where each question object has a `question` string, an `answers` array of strings,
 * and a `correct` index indicating the correct answer.
 *
 * The script should:
 * - Pick a random question each time, avoiding repeating the current question back-to-back.
 * - Render the question text into an element with id "question".
 * - Render each answer as a radio button inside a <label> inside a div with id "answers".
 * - When a radio button is selected, disable all inputs and highlight the correct answer
 *   in green and the selected wrong answer in red (using "correct" and "incorrect" CSS classes).
 * - Automatically advance to the next random question after 1.5 seconds.
 * - Start the game immediately when the script loads.
 */

let currentQuestion = null;

function getRandomQuestion() {
  const remaining = triviaData.filter((q) => q !== currentQuestion);
  const index = Math.floor(Math.random() * remaining.length);
  return remaining[index];
}

function showQuestion() {
  currentQuestion = getRandomQuestion();

  document.getElementById('question').textContent = currentQuestion.question;

  const answersDiv = document.getElementById('answers');
  answersDiv.innerHTML = '';

  currentQuestion.answers.forEach((answer, index) => {
    const label = document.createElement('label');

    const radio = document.createElement('input');
    radio.type = 'radio';
    radio.name = 'answer';
    radio.value = index;
    radio.addEventListener('change', handleAnswer);

    label.appendChild(radio);
    label.appendChild(document.createTextNode(answer));
    answersDiv.appendChild(label);
  });
}

function handleAnswer(event) {
  const selected = parseInt(event.target.value);
  const labels = document.querySelectorAll('#answers label');

  labels.forEach((label, index) => {
    const radio = label.querySelector('input');
    radio.disabled = true;
    if (index === currentQuestion.correct) {
      label.classList.add('correct');
    } else if (index === selected) {
      label.classList.add('incorrect');
    }
  });

  setTimeout(showQuestion, 1500);
}

showQuestion();
