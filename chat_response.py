HTML_page = """
<!DOCTYPE html>
<html>
<head>
  <title>English ↔ Nepali Translator</title>
  <style>
    body {
      background-color: #f5f5f5;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 20px;
    }
    .chat-container {
      max-width: 800px;
      margin: 0 auto;
      background: white;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
      color: #2c3e50;
      text-align: center;
      margin-bottom: 30px;
    }
    .message {
      padding: 15px;
      margin: 15px 0;
      border-radius: 8px;
      line-height: 1.6;
    }
    .message.you {
      background-color: #e3f2fd;
      border-left: 5px solid #2196f3;
    }
    .message.bot {
      background-color: #f1f8e9;
      border-left: 5px solid #4caf50;
    }
    form {
      display: flex;
      gap: 15px;
      margin: 30px 0;
      flex-wrap: wrap;
    }
    input[type="text"] {
      flex: 1;
      min-width: 200px;
      padding: 12px;
      border: 1px solid #ddd;
      border-radius: 6px;
      font-size: 16px;
    }
    select {
      padding: 12px;
      border: 1px solid #ddd;
      border-radius: 6px;
      background: white;
      font-size: 16px;
    }
    button {
      padding: 12px 25px;
      background-color: #4caf50;
      color: white;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      font-size: 16px;
      transition: background-color 0.3s;
    }
    button:hover {
      background-color: #3e8e41;
    }
    .language-direction {
      font-size: 0.85em;
      color: #666;
      margin-top: 8px;
      font-style: italic;
    }
    .error {
      color: #d32f2f;
      padding: 15px;
      background-color: #ffebee;
      border-radius: 6px;
      margin: 20px 0;
      border-left: 5px solid #f44336;
    }
    .history {
      margin-top: 30px;
      padding-top: 20px;
      border-top: 1px solid #eee;
    }
    .history h3 {
      color: #2c3e50;
      margin-bottom: 15px;
    }
    .history-item {
      padding: 10px;
      margin: 8px 0;
      background: #f9f9f9;
      border-radius: 4px;
      display: flex;
      justify-content: space-between;
    }
    .history-direction {
      font-size: 0.8em;
      color: #777;
    }
    @media (max-width: 600px) {
      .chat-container {
        padding: 15px;
      }
      form {
        flex-direction: column;
        gap: 10px;
      }
    }
  </style>
</head>
<body>
<div class="chat-container">
  <h1>English ↔ Nepali Translator</h1>
  
  {% if error %}
    <div class="error">Error: {{ error }}</div>
  {% endif %}
  
  <form action="/translate" method="post">
    <input type="text" name="text" value="{{ user_text or '' }}" 
           placeholder="Enter text to translate..." required>
    <select name="direction">
      <option value="en_to_ne" {% if direction == 'en_to_ne' %}selected{% endif %}>
        English → Nepali
      </option>
      <option value="ne_to_en" {% if direction == 'ne_to_en' %}selected{% endif %}>
        Nepali → English
      </option>
    </select>
    <button type="submit">Translate</button>
  </form>
  
  {% if user_text %}
    <div class="message you">
      <strong>You:</strong> {{ user_text }}
      <div class="language-direction">
        {{ "English" if direction == "en_to_ne" else "Nepali" }}
      </div>
    </div>
  {% endif %}
  
  {% if translation %}
    <div class="message bot">
      <strong>Translation:</strong> {{ translation }}
      <div class="language-direction">
        {{ "Nepali" if direction == "en_to_ne" else "English" }}
      </div>
    </div>
  {% endif %}
  
  {% if recent_history %}
    <div class="history">
      <h3>Recent Translations</h3>
      {% for item in recent_history %}
        <div class="history-item">
          <span>{{ item.source }} → {{ item.translation }}</span>
          <span class="history-direction">{{ item.direction.replace('_', ' ') }}</span>
        </div>
      {% endfor %}
    </div>
  {% endif %}
</div>
</body>
</html>
"""