document.addEventListener("DOMContentLoaded", () => {
    const imageContainer = document.getElementById("code-image");
    const optionsContainer = document.getElementById("options-container");
    const resultText = document.getElementById("result");
    const nextButton = document.getElementById("next-button");

    function loadQuestion() {
        fetch("/get-question")
            .then(response => response.json())
            .then(data => {
                imageContainer.src = `/static/images/${data.image}`;
                imageContainer.alt = `Code in ${data.language}`;
                optionsContainer.innerHTML = "";

                const languages = ["Python", "JavaScript", "C++", "Ruby", "Java"];
                languages.forEach(language => {
                    const button = document.createElement("button");
                    button.textContent = language;
                    button.addEventListener("click", () => submitAnswer(language, data.language));
                    optionsContainer.appendChild(button);
                });

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
                resultText.textContent = data.result === "correct" ? "Správně!" : "Špatně...";
                nextButton.style.display = "block";
            });
    }

    nextButton.addEventListener("click", loadQuestion);
    loadQuestion();
});