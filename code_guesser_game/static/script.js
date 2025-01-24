document.addEventListener("DOMContentLoaded", () => {
    const imageContainer = document.getElementById("code-image");
    const optionsContainer = document.getElementById("options-container");
    const resultText = document.getElementById("result");
    const nextButton = document.getElementById("next-button");
    const scoreSpan = document.getElementById("score");
  
    let currentQuestion = null;
    let score = 0;
  
    function loadQuestion() {
      fetch("/get-question")
        .then(response => response.json())
        .then(data => {
          currentQuestion = data;
          
          // Update image
          imageContainer.src = `/static/images/${data.image}`;
          imageContainer.alt = `Code in ${data.language}`;
          
          // Clear old options
          optionsContainer.innerHTML = "";
  
          const languages = ["Python", "JavaScript", "C++", "Ruby", "Java"];
          languages.forEach(language => {
            const button = document.createElement("button");
            button.className = "btn btn-outline-primary m-1 option-button";
            button.textContent = language;
            button.addEventListener("click", () => submitAnswer(language, data.language));
            optionsContainer.appendChild(button);
          });
  
          // Hide result and next button
          resultText.textContent = "";
          nextButton.style.display = "none";
        });
    }
  
    function submitAnswer(selected, correct) {
      fetch("/submit-answer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ language: selected, correct_language: correct })
      })
        .then(response => response.json())
        .then(data => {
          if (data.result === "correct") {
            resultText.textContent = "Správně!";
            resultText.classList.remove("text-danger");
            resultText.classList.add("text-success");
            score += 1;
            scoreSpan.textContent = score;
          } else {
            resultText.textContent = "Špatně...";
            resultText.classList.remove("text-success");
            resultText.classList.add("text-danger");
          }
          nextButton.style.display = "inline-block";
        });
    }
  
    nextButton.addEventListener("click", () => {
      loadQuestion();
    });
  
    loadQuestion();
  });
  