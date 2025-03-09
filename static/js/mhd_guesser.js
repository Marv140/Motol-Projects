// JavaScript to handle the game logic
document.addEventListener('DOMContentLoaded', function() {
  const questionImage = document.getElementById('question-image');
  const answerButtons = document.querySelectorAll('.answer-button');
  const resultDiv = document.getElementById('result');

  function loadQuestion() {
    fetch('/get-mhd-question')
      .then(response => response.json())
      .then(data => {
        questionImage.src = data.image;
        questionImage.alt = data.alt;
      });
  }

  answerButtons.forEach(button => {
    button.addEventListener('click', function() {
      const answer = this.getAttribute('data-answer');
      fetch('/submit-mhd-answer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ answer: answer })
      })
      .then(response => response.json())
      .then(data => {
        resultDiv.textContent = data.result;
        if (data.result === 'correct') {
          loadQuestion();
        }
      });
    });
  });

  loadQuestion();
});