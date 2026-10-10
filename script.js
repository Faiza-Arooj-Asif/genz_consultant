const chatWindow = document.getElementById("chatWindow");
const chatForm = document.getElementById("chatForm");
const questionInput = document.getElementById("questionInput");

const responses = Object.freeze([
  "Honestly? High-key yes.",
  "Low-key a bad idea, no cap.",
  "My neural networks are sensing big red flags.",
  "It's a full-on vibe, go for it.",
  "Error 404: Emotion not found. Try again later.",
  "Bet! The odds are definitely in your favor.",
  "That ain't it, chief.",
  "The vibe check says: absolutely.",
  "Not today, no cap.",
  "Big brain says this could work."
]);

/**
 * Add a plain-text message to the conversation and scroll it into view.
 * @param {"ai" | "user"} sender Message origin, used to select its visual style.
 * @param {string} text Message content.
 */
function addMessage(sender, text) {
  const message = document.createElement("div");
  message.className = `message ${sender}`;

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;

  message.appendChild(bubble);
  chatWindow.appendChild(message);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

/** Add an animated, screen-reader-hidden typing indicator to the chat. */
function showTyping() {
  const wrapper = document.createElement("div");
  wrapper.className = "message ai";
  wrapper.setAttribute("aria-hidden", "true");

  const bubble = document.createElement("div");
  bubble.className = "bubble typing";

  for (let index = 0; index < 3; index += 1) {
    const span = document.createElement("span");
    bubble.appendChild(span);
  }

  wrapper.appendChild(bubble);
  chatWindow.appendChild(wrapper);
  chatWindow.scrollTop = chatWindow.scrollHeight;

  return wrapper;
}

/** Return a random playful reply, or a farewell for exit phrases. */
function getReply(question) {
  const cleanQuestion = question.trim();

  if (!cleanQuestion) {
    return "Ask me something real, bestie.";
  }

  if (["exit", "quit", "bye"].includes(cleanQuestion.toLowerCase())) {
    return "Bye bestie! Stay cool.";
  }

  return responses[Math.floor(Math.random() * responses.length)];
}

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const question = questionInput.value.trim();
  if (!question) {
    questionInput.focus();
    return;
  }

  addMessage("user", question);
  questionInput.value = '';

  const typingBubble = showTyping();

  setTimeout(() => {
    typingBubble.remove();
    addMessage("ai", getReply(question));
    questionInput.focus();
  }, 900);
});
