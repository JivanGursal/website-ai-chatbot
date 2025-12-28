(function () {
  // Read bot id from script tag
  const scriptTag = document.currentScript;
  const BOT_ID = scriptTag.getAttribute("data-bot-id");

  // Create widget container
  const widget = document.createElement("div");
  widget.innerHTML = `
    <div id="ai-chatbot">
      <div id="chat-header">💬 Chat with us</div>
      <div id="chat-messages"></div>
      <input id="chat-input" placeholder="Type your message..." />
    </div>
  `;
  document.body.appendChild(widget);

  const input = document.getElementById("chat-input");
  const messages = document.getElementById("chat-messages");

  function addMessage(sender, text) {
    const div = document.createElement("div");
    div.className = sender;
    div.innerText = text;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  input.addEventListener("keypress", async (e) => {
    if (e.key === "Enter" && input.value.trim()) {
      const userMsg = input.value;
      addMessage("user", userMsg);
      input.value = "";

      try {
        const res = await fetch("http://127.0.0.1:8000/api/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            bot_id: BOT_ID,
            message: userMsg
          })
        });

        const data = await res.json();
        addMessage("bot", data.reply);
      } catch (err) {
        addMessage("bot", "⚠️ Server not responding");
      }
    }
  });
})();
