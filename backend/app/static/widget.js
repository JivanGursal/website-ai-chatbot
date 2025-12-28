(function () {
  const botId = "testbot";
  const api = "http://127.0.0.1:8000/api/chat/";

  // inject css
  const css = document.createElement("link");
  css.rel = "stylesheet";
  css.href = "http://127.0.0.1:8000/static/widget.css";
  document.head.appendChild(css);

  // button
  const btn = document.createElement("div");
  btn.id = "ai-chat-btn";
  btn.innerText = "AI Chat";
  document.body.appendChild(btn);

  // box
  const box = document.createElement("div");
  box.id = "ai-chat-box";
  box.innerHTML = `
    <div id="ai-header">Website Assistant</div>
    <div id="ai-messages"></div>
    <input id="ai-input" placeholder="Ask something..." />
  `;
  document.body.appendChild(box);

  btn.onclick = () => {
    box.style.display = box.style.display === "flex" ? "none" : "flex";
  };

  const input = box.querySelector("#ai-input");
  const msgs = box.querySelector("#ai-messages");

  input.addEventListener("keypress", async (e) => {
    if (e.key === "Enter") {
      const text = input.value;
      if (!text) return;

      msgs.innerHTML += `<div class="ai-user">${text}</div>`;
      input.value = "";

      const res = await fetch(api, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ bot_id: botId, message: text }),
      });

      const data = await res.json();
      msgs.innerHTML += `<div class="ai-bot">${data.reply}</div>`;
      msgs.scrollTop = msgs.scrollHeight;
    }
  });
})();
