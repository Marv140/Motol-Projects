document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("theme-toggle");
      const icon = themeToggle.querySelector("i");
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

      const editor = CodeMirror(document.getElementById("code-editor"), {
        value: "",
        mode: "python",
        lineNumbers: true,
        theme: "material",
        readOnly: true
      });

      async function loadQuestion() {
        try {
          const response = await fetch("/get-question");
          const data = await response.json();

          if (data.language === null) {
            editor.setValue("Sada hádanek dokončena!");
            document.getElementById("options-container").style.display = "none";
            return;
          }

          editor.setValue(data.code);
          createOptions(data.language);
        } catch (error) {
          console.error("Error loading question:", error);
        }
      }

      function createOptions(correctLanguage) {
        const container = document.getElementById("options-container");
        container.innerHTML = "";

        const distractors = ["JavaScript", "Python", "Ruby", "C++", "Java"].filter(
          lang => lang !== correctLanguage
        );

        const options = [correctLanguage, ...distractors.slice(0, 2)];
        options.sort(() => Math.random() - 0.5);

        options.forEach(option => {
          const button = document.createElement("button");
          button.textContent = option;
          button.onclick = () => {
            if (option === correctLanguage) {
              document.getElementById("result").textContent = "Správně!";
            } else {
              document.getElementById("result").textContent = "Špatně, zkuste znovu.";
            }
          };
          container.appendChild(button);
        });
      }

      loadQuestion();
    });