import { Bot, User, Send, Sparkles } from "https://cdn.jsdelivr.net/npm/lucide-react@latest/+esm";

const { useState, useRef, useEffect } = React;

const CASChatbot = () => {
  const [messages, setMessages] = useState([
    {
      type: "bot",
      text: "Hello! 👋 I'm the CAS Vattamkulam College Assistant...\n\n• Course info\n• Admission\n• Facilities\n• Contact\n\nHow can I help?"
    }
  ]);
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const generateResponse = (userMessage) => {
    const msg = userMessage.toLowerCase();

    if (msg.includes("course")) return "📚 Courses Offered:\n• BSc CS\n• BSc Electronics\n• BCA\n• BCom CA\n• BBA Logistics\n• MSc CS\n• M.Com Finance";
    if (msg.includes("admission")) return "📝 Admission Process:\n• 50% University seats\n• 50% IHRD seats\n• UG: ₹205/₹495 application fee";

    return "I can help with courses, admission, fees, facilities, activities & contact details!";
  };

  const handleSend = () => {
    if (!input.trim()) return;
    const userMessage = input.trim();

    setMessages((prev) => [...prev, { type: "user", text: userMessage }]);
    setInput("");
    setIsTyping(true);

    setTimeout(() => {
      const botReply = generateResponse(userMessage);
      setMessages((prev) => [...prev, { type: "bot", text: botReply }]);
      setIsTyping(false);
    }, 400);
  };

  return (
    <div className="flex flex-col h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="bg-red-600 text-white p-4 shadow-lg">
        <h1 className="text-xl font-bold">CAS Vattamkulam – AI Assistant</h1>
      </div>

      <div className="flex-1 overflow-y-auto p-4">
        {messages.map((msg, i) => (
          <div key={i} className={`flex my-2 ${msg.type === "user" ? "justify-end" : "justify-start"}`}>
            <div className={`p-3 rounded-xl shadow-md max-w-lg ${msg.type === "user" ? "bg-blue-600 text-white" : "bg-white"}`}>
              {msg.text}
            </div>
          </div>
        ))}

        {isTyping && (
          <div className="text-gray-600 italic">Assistant is typing...</div>
        )}

        <div ref={messagesEndRef}></div>
      </div>

      <div className="p-4 bg-white border-t flex gap-2">
        <input
          className="flex-1 border rounded-xl px-3 py-2"
          placeholder="Ask me anything about CAS Vattamkulam..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
        />
        <button onClick={handleSend} className="bg-blue-600 text-white px-4 rounded-xl shadow">
          Send
        </button>
      </div>
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<CASChatbot />);
