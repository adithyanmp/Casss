import React, { useState, useRef, useEffect } from 'react';
import { Send, Bot, User, Sparkles } from 'lucide-react';

const CASChatbot = () => {
  const [messages, setMessages] = useState([
    {
      type: 'bot',
      text: 'Hello! 👋 I\'m the CAS Vattamkulam College Assistant. I can help you with:\n\n• Course information (BSc CS, BCA, Electronics, Commerce, etc.)\n• Admission procedures and fees\n• Facilities and infrastructure\n• Contact details and location\n• Activities and clubs\n\nWhat would you like to know?'
    }
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const collegeData = {
    courses: {
      ug: [
        'BSc Computer Science',
        'BSc Electronics',
        'BCA (Bachelor of Computer Applications)',
        'BCom with Computer Application',
        'BBA Logistics Honours'
      ],
      pg: [
        'MSc Computer Science',
        'M.Com Finance'
      ]
    },
    contact: {
      phone: ['0494-2689655', '8547006802'],
      email: 'casvattamkulam@ihrd.ac.in',
      address: 'College of Applied Science, Vattamkulam, Nellissery, Sukapuram (P.O.), Edappal, Malappuram, Kerala - 679576'
    },
    facilities: [
      'Smart classrooms with interactive smartboards',
      'Computer Lab with latest software',
      'Electronics Lab',
      'Library',
      'Open Gym',
      'Volleyball court'
    ],
    activities: [
      'National Service Scheme (NSS)',
      'Placement Cell',
      'Women Cell',
      'Anti-Ragging Cell',
      'College Union',
      'Various clubs and associations'
    ],
    admission: {
      ugFee: 'SC/ST: ₹205, Others: ₹495',
      process: 'Online registration through University of Calicut portal (admission.uoc.ac.in)',
      ihrdSeats: '50% seats through IHRD direct admission (ihrdadmissions.org)'
    }
  };

  const generateResponse = (userMessage) => {
    const msg = userMessage.toLowerCase();

    // Courses
    if (msg.includes('course') || msg.includes('program') || msg.includes('degree')) {
      return '📚 **Courses Offered at CAS Vattamkulam:**\n\n**Undergraduate Programs:**\n' + collegeData.courses.ug.map(c => '• ' + c).join('\n') + '\n\n**Postgraduate Programs:**\n' + collegeData.courses.pg.map(c => '• ' + c).join('\n') + '\n\nAll programs are affiliated to University of Calicut.';
    }

    // Seats availability
    if (msg.includes('seat') || msg.includes('intake') || msg.includes('capacity')) {
      return '🎓 **Available Seats - Academic Year 2025-26:**\n\n**Postgraduate Programs:**\n• MSc Computer Science: 10 seats (+ marginal increase)\n• M.Com Finance: 15 seats (+ marginal increase)\n\n**Undergraduate Programs:**\n• BSc Computer Science Honours: 36 seats (+ marginal increase)\n• BSc Electronics: 36 seats (+ marginal increase)\n• BCA: 24 seats\n• BCom Honours with Computer Application: 48 seats (+ marginal increase)\n• BBA Logistics Honours: 30 seats\n\n**Total Intake: 199+ seats**\n\n**Important Information:**\n• 50% seats through University of Calicut\n• 50% seats through IHRD direct admission\n• Marginal increase means additional seats may be available\n• Selection based on merit/marks\n\nFor latest seat availability, contact:\n📞 0494-2689655 | 📧 casvattamkulam@ihrd.ac.in';
    }

    // BSc Computer Science
    if (msg.includes('bsc') && (msg.includes('computer') || msg.includes('cs'))) {
      return '💻 **BSc Computer Science Honours**\n\n**Program Details:**\n• Duration: 4 Years (8 Semesters)\n• Seats: 36 + marginal increase\n• Eligibility: Higher Secondary with Maths or Electronics\n• Selection: Based on marks of optional subjects in +2\n• Notification: After publication of Kerala +2 results\n\n**Fee Structure (Per Semester):**\n• Semester Fee: ₹17,270\n• Admission Fee (one-time): ₹330\n• Alumni Fee: ₹200\n• Caution Deposit (refundable): ₹1,000\n• *SC/ST and OEC students are exempted*\n\nThis comprehensive program offers knowledge in computer science, programming, software development, and emerging technologies.';
    }

    // BCA
    if (msg.includes('bca')) {
      return '💻 **Bachelor of Computer Applications (BCA)**\n\n**Program Details:**\n• Duration: 4 Years (8 Semesters)\n• Seats: 24\n• Eligibility: Higher Secondary with Mathematics/Computer Science/Computer Application/IT as one subject\n• Selection: Based on marks of optional subjects in +2\n• Notification: After publication of Kerala +2 results\n\n**Fee Structure (Per Semester):**\n• Semester Fee: ₹17,270\n• Admission Fee (one-time): ₹330\n• Alumni Fee: ₹200\n• Caution Deposit (refundable): ₹1,000\n• *SC/ST and OEC students are exempted*\n\nThis professional degree focuses on computer applications, programming, database management, and software engineering for IT careers.';
    }

    // Electronics
    if (msg.includes('electronic') || msg.includes('bsc electronic')) {
      return '⚡ **BSc Electronics**\n\n**Program Details:**\n• Duration: 3 Years (6 Semesters)\n• Seats: 36 + marginal increase\n• Eligibility: Higher Secondary with Maths or Electronics\n• Selection: Based on marks of optional subjects in +2\n• Notification: After publication of Kerala +2 results\n\n**Fee Structure (Per Semester):**\n• Semester Fee: ₹17,270\n• Admission Fee (one-time): ₹330\n• Alumni Fee: ₹200\n• Caution Deposit (refundable): ₹1,000\n• *SC/ST and OEC students are exempted*\n\nThis program covers electronic circuits, microprocessors, communication systems, and embedded systems with hands-on experience in our well-equipped Electronics Lab.';
    }

    // Commerce
    if (msg.includes('bcom') || msg.includes('commerce') || msg.includes('m.com') || msg.includes('mcom')) {
      if (msg.includes('m.com') || msg.includes('mcom')) {
        return '📊 **M.Com Finance**\n\n**Program Details:**\n• Duration: 2 Years (4 Semesters)\n• Seats: 15 + marginal increase\n• Eligibility: Bachelor of Commerce\n• Selection: Based on marks of UG course\n• Notification: After publication of Calicut University UG results\n\n**Fee Structure (Per Semester):**\n• Semester Fee: ₹18,425\n• Admission Fee (one-time): ₹1,100\n• Alumni Fee: ₹200\n• Caution Deposit (refundable): ₹1,000\n• *SC/ST and OEC students are exempted*\n\nThis specialized program focuses on financial management, accounting, taxation, and business analytics.';
      }
      return '📊 **BCom Honours with Computer Application**\n\n**Program Details:**\n• Duration: 4 Years (8 Semesters)\n• Seats: 48 + marginal increase\n• Eligibility: Higher Secondary or Equivalent\n• Selection: Based on marks of optional subjects in +2\n• Notification: After publication of Kerala +2 results\n\n**Fee Structure (Per Semester):**\n• Semester Fee: ₹13,035\n• Admission Fee (one-time): ₹330\n• Alumni Fee: ₹200\n• Caution Deposit (refundable): ₹1,000\n• *SC/ST and OEC students are exempted*\n\nThis program combines commerce education with computer skills, covering accounting, business management, taxation, and computer applications.';
    }

    // BBA Logistics
    if (msg.includes('bba') || msg.includes('logistic')) {
      return '🚚 **BBA Logistics Honours**\n\n**Program Details:**\n• Duration: 4 Years (8 Semesters)\n• Seats: 30\n• Eligibility: Higher Secondary with minimum 45% marks (40% for OBC/OEC, Pass for SC/ST)\n• Selection: Based on marks of optional subjects in +2\n• Notification: After publication of Kerala +2 results\n\n**Fee Structure (Per Semester):**\n• Semester Fee: ₹8,470\n• Admission Fee (one-time): ₹330\n• Alumni Fee: ₹200\n• Caution Deposit (refundable): ₹1,000\n• *SC/ST and OEC students are exempted*\n\nThis specialized program focuses on supply chain management, logistics operations, transportation management, and warehouse operations for careers in the growing logistics sector.';
    }

    // MSc Computer Science
    if (msg.includes('msc') || msg.includes('master')) {
      return '🎓 **MSc Computer Science**\n\n**Program Details:**\n• Duration: 2 Years (4 Semesters)\n• Seats: 10 + marginal increase\n• Eligibility: Bachelor of Computer Science\n• Selection: Based on marks of UG course\n• Notification: After publication of Calicut University degree results\n\n**Fee Structure (Per Semester):**\n• Semester Fee: ₹22,550\n• Admission Fee (one-time): ₹1,100\n• Alumni Fee: ₹200\n• Caution Deposit (refundable): ₹1,000\n• *SC/ST and OEC students are exempted*\n\nThis advanced program offers in-depth knowledge in algorithms, software engineering, AI, data science, and research methodologies.';
    }

    // Admission
    if (msg.includes('admission') || msg.includes('apply') || msg.includes('enroll') || msg.includes('join')) {
      return '📝 **Admission Information:**\n\n**For University Seats (50%):**\n• Online registration: admission.uoc.ac.in\n• Application Fee: ' + collegeData.admission.ugFee + '\n• Registration opens in June (5 PM deadline)\n\n**For IHRD Direct Seats (50%):**\n• Register at: ihrdadmissions.org\n• These seats are managed by IHRD Kerala Government\n\nFor detailed procedures, contact the college office.';
    }

    // Fees
    if (msg.includes('fee') || msg.includes('cost') || msg.includes('price')) {
      return '💰 **Complete Fee Structure (Per Semester):**\n\n**Postgraduate Programs:**\n• MSc Computer Science: ₹22,550\n• M.Com Finance: ₹18,425\n\n**Undergraduate Programs:**\n• BSc Computer Science: ₹17,270\n• BSc Electronics: ₹17,270\n• BCA: ₹17,270\n• BCom with Computer Application: ₹13,035\n• BBA Logistics Honours: ₹8,470\n\n**One-Time Fees (at admission):**\n• PG Courses: Admission ₹1,100 + Alumni ₹200 + Caution Deposit ₹1,000\n• UG Courses: Admission ₹330 + Alumni ₹200 + Caution Deposit ₹1,000\n\n**Important Notes:**\n• SC/ST and OEC students are exempted from fees\n• PTA Fee & University affiliation fee not included\n• Caution Deposit is refundable\n\n**Application Fees:**\n• SC/ST Category: ₹205\n• Other Categories: ₹495\n\n💳 Online payment: SBI Collect portal';
    }

    // Facilities
    if (msg.includes('facilit') || msg.includes('infrastructure') || msg.includes('lab') || msg.includes('library')) {
      return '🏛️ **Facilities at CAS Vattamkulam:**\n\n' + collegeData.facilities.map(f => '• ' + f).join('\n') + '\n\nThe college provides a modern learning environment with state-of-the-art infrastructure to support both academic and physical development.';
    }

    // Placement
    if (msg.includes('placement') || msg.includes('job') || msg.includes('career')) {
      return '💼 **Placement & Career Support:**\n\nCAS Vattamkulam has an active **Placement Cell** that:\n• Organizes campus recruitment drives\n• Conducts job fairs (recent Job Fair 2023)\n• Provides career guidance and training\n• Connects students with industry opportunities\n\nMany students have been successfully placed in reputed companies.';
    }

    // Activities
    if (msg.includes('activit') || msg.includes('club') || msg.includes('nss') || msg.includes('event')) {
      return '🎯 **Student Activities & Clubs:**\n\n' + collegeData.activities.map(a => '• ' + a).join('\n') + '\n\n**Associations:**\n• Computer Association\n• Electronics Association\n• Commerce Association\n• Literary Club\n• BMC (Business Management Club)\n\nStudents actively participate in seminars, workshops, cultural events, sports, and community service programs.';
    }

    // Contact
    if (msg.includes('contact') || msg.includes('phone') || msg.includes('email') || msg.includes('call')) {
      return '📞 **Contact Information:**\n\n**Phone:**\n• ' + collegeData.contact.phone[0] + '\n• ' + collegeData.contact.phone[1] + '\n\n**Email:**\n• ' + collegeData.contact.email + '\n\n**Address:**\n' + collegeData.contact.address + '\n\n**Social Media:**\n• Facebook: /casvattamkulamofficial\n• YouTube: @casvattamkulam\n• Instagram: @casvattamkulam.ihrd';
    }

    // Location
    if (msg.includes('location') || msg.includes('address') || msg.includes('where') || msg.includes('reach')) {
      return '📍 **Location:**\n\n' + collegeData.contact.address + '\n\nThe college is located at Vattamkulam, near Edappal (3 km), in a peaceful environment ideal for academic pursuits.\n\n**How to Reach:**\nThe college is easily accessible by road. Edappal is well-connected by bus services from major towns in Malappuram district.';
    }

    // About
    if (msg.includes('about') || msg.includes('history') || msg.includes('establish')) {
      return '🏛️ **About CAS Vattamkulam:**\n\nEstablished in **2005** by the Institute of Human Resource Development (IHRD), Kerala Government, the College of Applied Science Vattamkulam is affiliated to University of Calicut.\n\n**Vision:** To develop into a contributing Centre of excellence in knowledge and technology creating globally competitive professionals.\n\n**Mission:** To impart quality education and create professionals with high competency and values who can make an indelible mark in their respective fields.';
    }

    // IHRD
    if (msg.includes('ihrd')) {
      return '🏢 **IHRD (Institute of Human Resource Development):**\n\nCAS Vattamkulam is established and managed by IHRD, a Kerala Government institution. IHRD manages 50% of the college seats through direct admission. Visit ihrdadmissions.org for IHRD seat registration.';
    }

    // Hostel
    if (msg.includes('hostel') || msg.includes('accommodation')) {
      return 'For information about hostel facilities and accommodation, please contact the college office directly at:\n📞 0494-2689655\n📧 casvattamkulam@ihrd.ac.in';
    }

    // Default response
    return 'I can help you with information about:\n\n• Courses (BSc CS, BCA, Electronics, Commerce, etc.)\n• Admission process and fees\n• College facilities\n• Placements and activities\n• Contact details\n\nPlease ask me about any specific topic you would like to know more about!';
  };

  const handleSend = () => {
    if (!input.trim()) return;

    const userMessage = input.trim();
    setMessages(prev => [...prev, { type: 'user', text: userMessage }]);
    setInput('');
    setIsTyping(true);

    setTimeout(() => {
      const botResponse = generateResponse(userMessage);
      setMessages(prev => [...prev, { type: 'bot', text: botResponse }]);
      setIsTyping(false);
    }, 500);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const quickActions = [
    'Show all courses',
    'Admission process',
    'Contact details',
    'Facilities available'
  ];

  return (
    <div className="flex flex-col h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="bg-gradient-to-r from-red-500 to-red-600 text-white p-4 shadow-lg">
        <div className="max-w-4xl mx-auto">
          <div className="flex items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <div className="bg-white p-2 rounded-full shadow-md">
                <Bot className="w-8 h-8 text-red-600" />
              </div>
              <div>
                <div className="text-xl font-bold leading-tight">COLLEGE OF APPLIED SCIENCE</div>
                <div className="text-lg font-semibold text-red-50">VATTAMKULAM</div>
                <div className="text-xs text-red-100 italic">Affiliated to University of Calicut</div>
              </div>
            </div>
            <div className="hidden md:flex items-center gap-2 bg-white/20 px-3 py-2 rounded-lg backdrop-blur-sm">
              <span className="text-sm font-medium">AI Assistant</span>
            </div>
          </div>
        </div>
      </div>

      <div className="flex-1 overflow-y-auto p-4">
        <div className="max-w-4xl mx-auto space-y-4">
          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`flex gap-3 ${msg.type === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              {msg.type === 'bot' && (
                <div className="bg-white p-2 rounded-full h-10 w-10 flex items-center justify-center shadow-md flex-shrink-0">
                  <Bot className="w-5 h-5 text-blue-600" />
                </div>
              )}
              <div
                className={`max-w-2xl p-4 rounded-2xl shadow-md ${
                  msg.type === 'user'
                    ? 'bg-gradient-to-r from-blue-600 to-indigo-600 text-white'
                    : 'bg-white text-gray-800'
                }`}
              >
                <div className="whitespace-pre-line text-sm leading-relaxed">
                  {msg.text}
                </div>
              </div>
              {msg.type === 'user' && (
                <div className="bg-gradient-to-r from-blue-600 to-indigo-600 p-2 rounded-full h-10 w-10 flex items-center justify-center shadow-md flex-shrink-0">
                  <User className="w-5 h-5 text-white" />
                </div>
              )}
            </div>
          ))}
          
          {isTyping && (
            <div className="flex gap-3 justify-start">
              <div className="bg-white p-2 rounded-full h-10 w-10 flex items-center justify-center shadow-md">
                <Bot className="w-5 h-5 text-blue-600" />
              </div>
              <div className="bg-white p-4 rounded-2xl shadow-md">
                <div className="flex gap-1">
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-100"></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-200"></div>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
      </div>

      {messages.length === 1 && (
        <div className="px-4 pb-2">
          <div className="max-w-4xl mx-auto">
            <div className="flex items-center gap-2 mb-2">
              <Sparkles className="w-4 h-4 text-blue-600" />
              <span className="text-sm text-gray-600 font-medium">Quick questions:</span>
            </div>
            <div className="flex flex-wrap gap-2">
              {quickActions.map((action, idx) => (
                <button
                  key={idx}
                  onClick={() => {
                    setInput(action);
                    setTimeout(() => handleSend(), 100);
                  }}
                  className="px-3 py-2 bg-white text-blue-600 text-sm rounded-lg shadow-sm hover:shadow-md hover:bg-blue-50 transition-all"
                >
                  {action}
                </button>
              ))}
            </div>
          </div>
        </div>
      )}

      <div className="bg-white border-t p-4 shadow-lg">
        <div className="max-w-4xl mx-auto flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Ask me anything about CAS Vattamkulam..."
            className="flex-1 px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
          <button
            onClick={handleSend}
            disabled={!input.trim()}
            className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-6 py-3 rounded-xl hover:from-blue-700 hover:to-indigo-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-md hover:shadow-lg flex items-center gap-2"
          >
            <Send className="w-5 h-5" />
            <span className="font-medium">Send</span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default CASChatbot;