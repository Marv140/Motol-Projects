document.addEventListener("DOMContentLoaded", () => {
    const codeImage = document.getElementById("code-image");
    const optionsContainer = document.getElementById("options-container");
    const resultText = document.getElementById("result");
    const nextButton = document.getElementById("next-button");
    const themeToggle = document.getElementById("theme-toggle");
    const icon = themeToggle.querySelector("i");
  
    // 1) Check Local Storage for saved theme preference
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme && savedTheme === "dark") {
      document.body.classList.add("dark");
      icon.classList.replace("fa-sun", "fa-moon");
    }
  
    // 2) Theme toggle logic (with local storage)
    themeToggle.addEventListener("click", () => {
      document.body.classList.toggle("dark");
  
      if (document.body.classList.contains("dark")) {
        localStorage.setItem("theme", "dark");
        icon.classList.replace("fa-sun", "fa-moon");
      } else {
        localStorage.setItem("theme", "light");
        icon.classList.replace("fa-moon", "fa-sun");
      }
    });
  
    // Load a question from your backend (example endpoint: /get-question)
    async function loadQuestion() {
      try {
        const response = await fetch("/get-question");
        const data = await response.json();
  
        // Update image
        codeImage.src = `/static/images/${data.image}`;
        codeImage.alt = `Code in ${data.language}`;
  
        // Prepare language buttons
        optionsContainer.innerHTML = "";
        const languages = ["Python", "JavaScript", "C++", "Ruby", "Java"];
  
        languages.forEach(language => {
          const button = document.createElement("button");
          button.textContent = language;
          button.addEventListener("click", () => submitAnswer(button, language, data.language));
          optionsContainer.appendChild(button);
        });
  
        // Reset result text
        resultText.textContent = "";
        resultText.className = "";
        nextButton.style.display = "none";
      } catch (error) {
        console.error("Error loading question:", error);
        resultText.textContent = "Chyba při načítání otázky.";
        resultText.className = "incorrect";
      }
    }
  
    // Submit the selected answer
    async function submitAnswer(selectedButton, selected, correct) {
      try {
        // Disable all buttons once one answer is clicked
        const allButtons = optionsContainer.querySelectorAll("button");
        allButtons.forEach(btn => (btn.disabled = true));
  
        // Make the request to submit the answer
        const response = await fetch("/submit-answer", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ language: selected, correct_language: correct })
        });
        const data = await response.json();
  
        // Show result
        if (data.result === "correct") {
          resultText.textContent = "Správně!";
          resultText.className = "correct";
        } else {
          resultText.textContent = `Špatně... Správně je ${correct}.`;
          resultText.className = "incorrect";
        }
  
        // Show "Další" button
        nextButton.style.display = "inline-block";
      } catch (error) {
        console.error("Error submitting answer:", error);
        resultText.textContent = "Chyba při odesílání odpovědi.";
        resultText.className = "incorrect";
      }
    }
  
    // Load next question on "Další" button click
    nextButton.addEventListener("click", loadQuestion);
  
    // Initial question load
    loadQuestion();
  });
  