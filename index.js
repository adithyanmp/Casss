// Access components and hooks from the globally available React and lucide objects
const { useState, useRef, useEffect } = React;
const { Bot, User, Send, Sparkles } = lucide.icons;

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

  const renderMessageContent = (text) => {
      // Simple logic to render lines separated by \n as paragraphs
      return text.split('\n').map((line, index) => (
          <p key={index} className={index > 0 ? "mt-1" : ""}>{line}</p>
      ));
  };


  return (
    <div className="flex flex-col h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="bg-red-600 text-white p-4 shadow-lg flex items-center gap-2">
        <Sparkles size={20} />
        <h1 className="text-xl font-bold">CAS Vattamkulam – AI Assistant</h1>
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((msg, i) => (
          <div key={i} className={`flex ${msg.type === "user" ? "justify-end" : "justify-start"}`}>
            <div className={`p-3 rounded-xl shadow-md max-w-[80%] whitespace-pre-wrap ${msg.type === "user" ? "bg-blue-600 text-white" : "bg-white text-gray-800"}`}>
              <div className="flex items-start gap-2">
                {msg.type === "bot" ? <Bot size={20} className="text-red-500 flex-shrink-0" /> : <User size={20} className="flex-shrink-0" />}
                <div>{renderMessageContent(msg.text)}</div>
              </div>
            </div>
          </div>
        ))}

        {isTyping && (
          <div className="flex justify-start">
             <div className="p-3 rounded-xl shadow-md bg-white text-gray-600 italic">
               Assistant is typing...
             </div>
          </div>
        )}

        <div ref={messagesEndRef}></div>
      </div>

      <div className="p-4 bg-white border-t flex gap-2 items-center">
        <input
          className="flex-1 border border-gray-300 rounded-xl px-4 py-2 focus:ring-blue-500 focus:border-blue-500 transition duration-150"
          placeholder="Ask me anything about CAS Vattamkulam..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
          disabled={isTyping}
        />
        <button 
          onClick={handleSend} 
          className="bg-blue-600 text-white p-3 rounded-xl shadow-md hover:bg-blue-700 transition duration-150 disabled:bg-gray-400"
          disabled={!input.trim() || isTyping}
        >
          <Send size={24} />
        </button>
      </div>
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<CASChatbot />);
