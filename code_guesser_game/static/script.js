document.addEventListener("DOMContentLoaded", () => {
  // Grab references
  const optionsContainer = document.getElementById("options-container");
  const resultText       = document.getElementById("result");
  const nextButton       = document.getElementById("next-button");
  const themeToggle      = document.getElementById("theme-toggle");
  const icon             = themeToggle.querySelector("i");

  // =====================
  // 1) DARK MODE
  // =====================
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

  // =====================
  // 2) CODEMIRROR INIT
  // =====================
  const editorEl = document.getElementById("code-editor");
  // Create our scrollable editor
  const editor = CodeMirror(editorEl, {
    value: "",              // We'll set the text after fetch
    mode: "python",         // Default fallback
    lineNumbers: true,
    theme: "material",      // Matches the .css theme
    readOnly: false,        // Let user scroll and edit
  });

  // Map from language to CodeMirror mode
  const languageMap = {
    "Python": "python",
    "JavaScript": "javascript",
    "C++": "text/x-c++src",
    "Ruby": "ruby",
    "Java": "text/x-java"
  };

  // =====================
  // 3) LOAD A QUESTION
  // =====================
  async function loadQuestion() {
    try {
      const response = await fetch("/get-question");
      const data     = await response.json();
      // data = { code: "...", language: "Python" }

      // Set the editor text
      editor.setValue(data.code);

      // Update syntax highlighting mode
      const cmMode = languageMap[data.language] || "python";
      editor.setOption("mode", cmMode);

      // Create answer buttons
      createOptionButtons(data.language);

      // Clear old result
      resultText.textContent = "";
      resultText.className = "";
      nextButton.style.display = "none";
    } catch (error) {
      console.error("Error loading question:", error);
      resultText.textContent = "Chyba při načítání otázky.";
      resultText.className = "incorrect";
    }
  }

  // =====================
  // 4) CREATE ANSWER BUTTONS
  // =====================
  function createOptionButtons(correctLanguage) {
    optionsContainer.innerHTML = "";
    const languages = ["Python", "JavaScript", "C++", "Ruby", "Java"];

    languages.forEach(lang => {
      const btn = document.createElement("button");
      btn.textContent = lang;
      btn.addEventListener("click", () => {
        // Disable all buttons to lock in choice
        disableAllButtons();
        // Submit user’s guess
        submitAnswer(lang, correctLanguage);
      });
      optionsContainer.appendChild(btn);
    });
  }

  function disableAllButtons() {
    const buttons = optionsContainer.querySelectorAll("button");
    buttons.forEach(btn => {
      btn.disabled = true;
    });
  }

  // =====================
  // 5) SUBMIT ANSWER
  // =====================
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
      // Show 'Next' button
      nextButton.style.display = "inline-block";
    } catch (error) {
      console.error("Error submitting answer:", error);
      resultText.textContent = "Chyba při odesílání odpovědi.";
      resultText.className = "incorrect";
    }
  }

  // =====================
  // 6) NEXT QUESTION
  // =====================
  nextButton.addEventListener("click", loadQuestion);

  // Initial load
  loadQuestion();
});
