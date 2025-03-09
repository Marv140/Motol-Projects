// JavaScript to handle the game logic
document.addEventListener('DOMContentLoaded', function() {
  const questionImage = document.getElementById('question-image');
  const answerButtonsContainer = document.getElementById('answer-buttons');
  const resultDiv = document.getElementById('result');
  const nextButton = document.getElementById('next-button');
  const tryAgainButton = document.getElementById('try-again-button');

  function loadQuestion() {
    fetch('/get-mhd-question')
      .then(response => response.json())
      .then(data => {
        if (data.result) {
          resultDiv.textContent = data.result;
          nextButton.style.display = 'none';
          tryAgainButton.style.display = 'none';
          return;
        }
        questionImage.src = data.image;
        questionImage.alt = 'MHD Image';
        createAnswerButtons(data.options, data.answer);
        resultDiv.textContent = '';
        nextButton.style.display = 'none';
        tryAgainButton.style.display = 'none';
      });
  }

  function createAnswerButtons(options, correctAnswer) {
    answerButtonsContainer.innerHTML = '';
    options.forEach(option => {
      const button = document.createElement('button');
      button.classList.add('answer-button');
      button.textContent = option;
      button.dataset.answer = option;
      button.dataset.correctAnswer = correctAnswer;
      button.addEventListener('click', handleAnswerClick);
      answerButtonsContainer.appendChild(button);
    });
  }

  function handleAnswerClick(event) {
    const answer = event.target.dataset.answer;
    const correctAnswer = event.target.dataset.correctAnswer;
    fetch('/submit-mhd-answer', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ answer: answer, correct_answer: correctAnswer })
    })
    .then(response => response.json())
    .then(data => {
      answerButtonsContainer.style.display = 'none'; // Hide options after submission

      if (data.result === 'correct') {
        resultDiv.textContent = 'Správně!';
        resultDiv.classList.add('correct-result');
        resultDiv.classList.remove('incorrect-result');
        nextButton.style.display = 'block';
      } else {
        resultDiv.textContent = 'Špatně... Zkus to znovu';
        resultDiv.classList.add('incorrect-result');
        resultDiv.classList.remove('correct-result');
        tryAgainButton.style.display = 'block';
      }
    });
  }

  nextButton.addEventListener('click', () => {
    loadQuestion();
    answerButtonsContainer.style.display = 'flex'; // Show options when loading next question
  });

  tryAgainButton.addEventListener('click', () => {
    resultDiv.textContent = '';
    resultDiv.classList.remove('correct-result', 'incorrect-result');
    tryAgainButton.style.display = 'none';
    answerButtonsContainer.style.display = 'flex'; // Show options when trying again
  });

  loadQuestion();
});

// Show the popup on page load
window.onload = function() {
  document.getElementById('popup').style.display = 'flex';
};

// Close the popup when the close button is clicked
document.getElementById('close-popup').onclick = function() {
  document.getElementById('popup').style.display = 'none';
};

document.getElementById('fullscreen-button').addEventListener('click', function() {
  const image = document.getElementById('question-image');
  if (image.requestFullscreen) {
    image.requestFullscreen();
  } else if (image.mozRequestFullScreen) { // Firefox
    image.mozRequestFullScreen();
  } else if (image.webkitRequestFullscreen) { // Chrome, Safari and Opera
    image.webkitRequestFullscreen();
  } else if (image.msRequestFullscreen) { // IE/Edge
    image.msRequestFullscreen();
  }
});