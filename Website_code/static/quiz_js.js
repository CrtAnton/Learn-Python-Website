let currentQuestion = 0;
const questions = {{ questions | tojson }};

function displayQuestion() {
    const question = questions[currentQuestion];
    const questionDiv = document.querySelector('.question');
    const optionsDiv = document.querySelector('.options');

    questionDiv.innerHTML = question.question;
    optionsDiv.innerHTML = '';

    question.options.forEach(option => {
        const button = document.createElement('button');
        button.innerText = option;
        button.addEventListener('click', () => checkAnswer(option));
        optionsDiv.appendChild(button);
    });
}

function checkAnswer(selected) {
    const correctAnswer = questions[currentQuestion].answer;
    const optionsDiv = document.querySelector('.options');
    const buttons = optionsDiv.querySelectorAll('button');

    buttons.forEach(button => {
        if (button.innerText === correctAnswer) {
            button.classList.add('correct');
        } else if (button.innerText === selected && selected !== correctAnswer) {
            button.classList.add('wrong');
        }
    });
}

function nextQuestion() {
    currentQuestion++;
    if (currentQuestion >= questions.length) currentQuestion = 0;
    displayQuestion();
}

function prevQuestion() {
    currentQuestion--;
    if (currentQuestion < 0) currentQuestion = questions.length - 1;
    displayQuestion();
}

displayQuestion();