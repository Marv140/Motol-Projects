document.addEventListener("DOMContentLoaded", () => {
  // References
  const optionsContainer = document.getElementById("options-container");
  const resultText       = document.getElementById("result");
  const nextButton       = document.getElementById("next-button");
  const themeToggle      = document.getElementById("theme-toggle");
  const icon             = themeToggle.querySelector("i");

  // Dark Mode Setup
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    document.body.classList.add("dark");
    icon.classList.replace("fa-sun", "fa-moon");
  }

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

  // Initialize CodeMirror
  const editorEl = document.getElementById("code-editor");
  const editor = CodeMirror(editorEl, {
    value: "",
    mode: "python",     // fallback
    lineNumbers: true,
    theme: "material",  // must match the .css theme
    readOnly: false
  });

  // Simple map from your snippet’s language to CodeMirror mode
  const languageMap = {
    "Python": "python",
    "JavaScript": "javascript",
    "C++": "text/x-c++src",
    "Ruby": "ruby",
    "Java": "text/x-java",
    // Add more if needed, e.g. "holyC", "C#", "React", etc.
  };

  // Fetch and display a question
  async function loadQuestion() {
    try {
      const response = await fetch("/get-question");
      const data = await response.json();
    
      // If language === null => no more questions
      if (data.language === null) {
        editor.setValue(data.code);
        optionsContainer.innerHTML = "";
        optionsContainer.style.display = "none";
        nextButton.style.display = "none";
        return;
      }
    
      // Otherwise show the snippet
      editor.setValue(data.code);
      createOptionButtons(data.language);

      // Reset result and hide 'Next'
      resultText.textContent = "";
      resultText.className = "";
      nextButton.style.display = "none";
      optionsContainer.style.display = "flex";
    } catch (error) {
      console.error("Error loading question:", error);
      resultText.textContent = "Chyba při načítání otázky.";
      resultText.className = "incorrect";
    }
  }

  // Master list of possible languages
  const ALL_LANGUAGES = ["Python", "JavaScript", "C++", "Ruby", "Java", "Lua"];

  // Create 3 options: correct + 2 distractors
  function createOptionButtons(correctLanguage) {
    optionsContainer.innerHTML = "";

    const distractors = ALL_LANGUAGES.filter(lang => lang !== correctLanguage);
    shuffleArray(distractors);
    const chosenDistractors = distractors.slice(0, 2);

    const finalOptions = [correctLanguage, ...chosenDistractors];
    shuffleArray(finalOptions);

    finalOptions.forEach(lang => {
      const btn = document.createElement("button");
      btn.textContent = lang;
      btn.addEventListener("click", () => {
        disableAllButtons();
        submitAnswer(lang, correctLanguage);
      });
      optionsContainer.appendChild(btn);
    });
  }

  // Shuffle array (Fisher–Yates)
  function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }

  function disableAllButtons() {
    const buttons = optionsContainer.querySelectorAll("button");
    buttons.forEach(btn => (btn.disabled = true));
  }

  // Submit user's guess
  async function submitAnswer(selectedLanguage, correctLanguage) {
    try {
      const response = await fetch("/submit-answer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          language: selectedLanguage,
          correct_language: correctLanguage
        })
      });
      const data = await response.json();

      if (data.result === "correct") {
        resultText.textContent = "Správně!";
        resultText.className = "correct";
      } else {
        resultText.textContent = `Špatně... Správně je ${data.correct_language}.`;
        resultText.className = "incorrect";
      }
      // Show next
      nextButton.style.display = "inline-block";
    } catch (error) {
      console.error("Error submitting answer:", error);
      resultText.textContent = "Chyba při odesílání odpovědi.";
      resultText.className = "incorrect";
    }
  }

  // "Next" button -> load next question
  nextButton.addEventListener("click", loadQuestion);

  // Initial question
  loadQuestion();
});
