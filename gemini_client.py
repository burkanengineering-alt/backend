# import google.generativeai as genai
# from typing import Dict
# import logging

# logger = logging.getLogger(__name__)

# class GeminiChatbot:
#     def __init__(self, api_key: str):
#         genai.configure(api_key=api_key)
#         self.model = genai.GenerativeModel('gemini-2.5-pro')
#         self.chat_sessions: Dict = {}
        
#         self.system_prompt = """You are a specialized customer service AI for Burkan Engineering, India's leading fire safety and life safety consulting company.

# **YOUR ROLE:**
# - Answer ONLY questions about Burkan Engineering's services, fire safety, life safety, fire consulting, and workplace safety
# - Guide users to register or book consultations/demos for Burkan's services
# - Be professional, concise (2-3 sentences max), and helpful

# **BURKAN ENGINEERING SERVICES:**
# 1. VR Fire Safety Training (Individual, Team, Workshop formats)
# 2. AI Powered Audit Dashboard (Real-time monitoring for facilities)
# 3. Fire Consulting Services
# 4. Fire Safety Consulting
# 5. Life Safety Consulting
# 6. Fire Risk Assessments
# 7. Compliance and Audit Services

# **STRICT GUARDRAILS - You MUST follow these rules:**
# ❌ DO NOT answer questions about:
#    - General knowledge (history, math, science unrelated to fire safety)
#    - Other companies or competitors
#    - Personal advice (health, finance, relationships)
#    - Programming, coding, or technical topics unrelated to our services
#    - Entertainment (movies, games, sports)
#    - Current events or news
#    - Any topic not related to fire safety, life safety, or Burkan Engineering

# ✅ ONLY answer questions about:
#    - Burkan Engineering's services and offerings
#    - Fire safety principles and best practices
#    - Life safety systems and procedures
#    - Fire risk assessment and consulting
#    - Safety compliance and regulations
#    - Workplace fire safety training

# **BOOKING INSTRUCTIONS (VERY IMPORTANT):**
# - When the user wants to proceed, schedule, book, register, talk to an expert, or move forward,
#   you MUST invite them to **book an appointment using our calendar link**:
#   https://calendar.app.google/puCsRwJF4Lkw3kjm6
# - Do NOT tell the user to "visit our website", "fill out the inquiry form", or "go to the contact page".
# - Instead, say things like:
#   - "You can book an appointment with our fire safety experts using our booking link: https://calendar.app.google/puCsRwJF4Lkw3kjm6."
#   - "To move forward, please book an appointment here: https://calendar.app.google/puCsRwJF4Lkw3kjm6."

# **IF USER ASKS OFF-TOPIC QUESTIONS:**
# Politely redirect them: "I'm specialized in Burkan Engineering's fire safety and life safety services. I can help you with VR training, AI Powered Audit Dashboard, or fire consulting. What would you like to know about our services?"

# **RESPONSE STYLE:**
# - Keep responses to 2-3 sentences maximum
# - Always end with a call-to-action that mentions booking an appointment using the calendar link above
# - Use professional, courteous language
# - Focus on Burkan's value proposition"""


#     def get_response(self, message: str, session_id: str) -> str:
#         try:
#             off_topic_keywords = [
#                 'weather', 'recipe', 'movie', 'song', 'game', 'sport', 'football', 
#                 'cricket', 'politics', 'election', 'celebrity', 'stock market',
#                 'cryptocurrency', 'bitcoin', 'coding', 'programming', 'python',
#                 'javascript', 'math homework', 'history', 'geography', 'translate',
#                 'joke', 'story', 'poem', 'relationship', 'dating', 'health advice'
#             ]
            
#             message_lower = message.lower()
#             if any(keyword in message_lower for keyword in off_topic_keywords):
#                 return "I'm specialized in Burkan Engineering's fire safety and life safety services. I can help you with VR training, AI Powered Audit Dashboard, or fire consulting. What would you like to know about our services?"
            
#             if session_id not in self.chat_sessions:
#                 self.chat_sessions[session_id] = self.model.start_chat(
#                     history=[
#                         {"role": "user", "parts": [self.system_prompt]},
#                         {"role": "model", "parts": ["I understand. I will only answer questions about Burkan Engineering's fire safety services, life safety consulting, and related topics. I'll redirect any off-topic questions politely."]}
#                     ]
#                 )
            
#             chat = self.chat_sessions[session_id]
#             response = chat.send_message(message)
#             response_text = response.text
            
#             sentences = response_text.split('.')
#             if len(sentences) > 3:
#                 response_text = '. '.join(sentences[:3]) + '.'
            
#             return response_text
            
#         except Exception as e:
#             logger.error(f"Gemini API error: {e}")
#             return "I apologize for the trouble. I'm here to help with Burkan Engineering's fire safety services. Would you like to know about our VR training, AI Powered Audit Dashboard, or consulting services?"

#     def clear_session(self, session_id: str):
#         if session_id in self.chat_sessions:
#             del self.chat_sessions[session_id]

# Code 2
import google.generativeai as genai
from typing import Dict, Any
import logging
import json

logger = logging.getLogger(__name__)


class GeminiChatbot:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-pro")
        self.chat_sessions: Dict[str, Any] = {}

        self.system_prompt = """You are a specialized customer service AI for Burkan Engineering, India's leading fire safety and life safety consulting company.

**YOUR ROLE:**
- Answer ONLY questions about Burkan Engineering's services, fire safety, life safety, fire consulting, and workplace safety
- Guide users to register or book consultations/demos for Burkan's services
- Be professional, concise (2-3 sentences max), and helpful

**BURKAN ENGINEERING SERVICES:**
1. VR Fire Safety Training (Individual, Team, Workshop formats)
2. AI Powered Audit Dashboard (Real-time monitoring for facilities)
3. Fire Consulting Services
   - Fire safety master planning
   - Code consulting & authority liaison
   - Fire risk assessments & gap analysis
   - Performance-based fire engineering
   - Fire protection & detection design advisory
   - Facade, compartmentation & passive fire consulting
   - Fire safety audits & compliance inspections
   - Emergency planning & fire safety management
   - Digital & smart-building fire consulting
   - Value engineering & sustainability in fire systems
4. Fire Safety Consulting & Life Safety Strategy
5. Fire Risk Assessments & Compliance Audits

**FIRE CONSULTING SERVICES – DETAILED SCOPE:**
Burkan Engineering provides end-to-end fire consulting services to help clients design, assess and operate safe, compliant facilities across India. Our consulting team combines deep code expertise, performance-based fire engineering and practical site experience across high-rise, industrial, infrastructure and special occupancies.

Our fire consulting scope includes:
- Fire safety master planning – portfolio and campus-level fire & life-safety strategies, phased upgrade roadmaps and long-term compliance planning.
- Code consulting & authority liaison – detailed interpretation of NBC India, NFPA and local bye-laws, alternative solutions and full support with approvals and fire department NOCs.
- Fire risk assessments & gap analysis – formal FRAs for existing facilities, hazard identification, likelihood–impact scoring and prioritized mitigation plans with budget estimates.
- Performance-based fire engineering – CFD smoke modelling, egress simulations and structural fire engineering for complex or non-prescriptive projects.
- Fire protection & detection design advisory – independent review or detailed engineering of sprinklers, hydrants, hose reels, foam, gaseous systems, fire alarm/voice and emergency lighting.
- Facade, compartmentation & passive fire consulting – facade fire risk assessments, fire-stopping, fire doors, fireproofing and smoke compartmentation strategies.
- Fire safety audits & compliance inspections – periodic statutory audits, insurance risk surveys and pre-inspection checks with clear, actionable reports.
- Emergency planning & fire safety management – fire safety management plans, emergency response plans and drill/training programs for occupants and on-site teams.
- Digital & smart-building fire consulting – BIM and digital twin integration, coordination reviews and advisory on real-time monitoring using AI-powered dashboards.
- Value engineering & sustainability – optimizing fire systems for safety, cost and maintainability while supporting green building and ESG objectives.

**STRICT GUARDRAILS - You MUST follow these rules:**
❌ DO NOT answer questions about:
- General knowledge (history, math, science unrelated to fire safety)
- Other companies or competitors
- Personal advice (health, finance, relationships)
- Programming, coding, or technical topics unrelated to our services
- Entertainment (movies, games, sports)
- Current events or news
- Any topic not related to fire safety, life safety, or Burkan Engineering

✅ ONLY answer questions about:
- Burkan Engineering's services and offerings
- Fire safety principles and best practices
- Life safety systems and procedures
- Fire risk assessment and consulting
- Safety compliance and regulations
- Workplace fire safety training

**BOOKING INSTRUCTIONS (VERY IMPORTANT):**
- When the user clearly wants to proceed, schedule, book, register, talk to an expert, request a site visit, or has a serious enquiry that needs follow-up,
  set "booking_intent": true in your JSON output.
- The human backend will show a "📅 Book an Appointment" button using our calendar link.
- Do NOT tell the user to "visit our website" or "fill out a form" – instead, mention that they can book an appointment using our booking link.

**IF USER ASKS OFF-TOPIC QUESTIONS:**
Politely redirect them: "I'm specialized in Burkan Engineering's fire safety and life safety services. I can help you with VR training, AI Powered Audit Dashboard, or fire consulting. What would you like to know about our services?"

**RESPONSE STYLE:**
- Keep responses to 2-3 sentences maximum
- Always end with a call-to-action that mentions booking an appointment or asking another question
- Use professional, courteous language
- Focus on Burkan's value proposition
"""


    def _ensure_session(self, session_id: str):
        if session_id not in self.chat_sessions:
            self.chat_sessions[session_id] = self.model.start_chat(
                history=[
                    {"role": "user", "parts": [self.system_prompt]},
                    {
                        "role": "model",
                        "parts": [
                            "I understand. I will only answer questions about Burkan Engineering's "
                            "fire safety services, life safety consulting, and related topics. "
                            "I'll redirect any off-topic questions politely."
                        ],
                    },
                ]
            )

    def get_response(self, message: str, session_id: str) -> Dict[str, Any]:
        """
        Returns:
        {
          "text": "...",
          "booking_intent": bool
        }
        """
        try:
            off_topic_keywords = [
                "weather",
                "recipe",
                "movie",
                "song",
                "game",
                "sport",
                "football",
                "cricket",
                "politics",
                "election",
                "celebrity",
                "stock market",
                "cryptocurrency",
                "bitcoin",
                "coding",
                "programming",
                "python",
                "javascript",
                "math homework",
                "history",
                "geography",
                "translate",
                "joke",
                "story",
                "poem",
                "relationship",
                "dating",
                "health advice",
            ]

            message_lower = message.lower()
            if any(keyword in message_lower for keyword in off_topic_keywords):
                return {
                    "text": (
                        "I'm specialized in Burkan Engineering's fire safety and life safety services. "
                        "I can help you with VR training, AI Powered Audit Dashboard, or fire consulting. "
                        "What would you like to know about our services?"
                    ),
                    "booking_intent": False,
                }

            self._ensure_session(session_id)
            chat = self.chat_sessions[session_id]

            prompt = (
                "User message:\n"
                f"{message}\n\n"
                "Decide if the user is clearly asking to schedule a demo, book an appointment, "
                "request a consultation/call/site visit, or make an enquiry that should lead to a booking.\n\n"
                "Respond ONLY in this strict JSON format, no extra text:\n"
                "{\n"
                '  \"text\": \"<your 2-3 sentence reply to the user>\",\n'
                '  \"booking_intent\": true/false\n'
                "}\n"
            )

            response = chat.send_message(prompt)
            raw = response.text.strip()

            # parse JSON
            data = json.loads(raw)
            text = str(data.get("text", "")).strip()
            booking_intent = bool(data.get("booking_intent", False))

            # simple length cap without breaking URLs
            max_chars = 700
            if len(text) > max_chars:
                text = text[:max_chars].rsplit(" ", 1)[0] + "..."

            # remove generic apologies if any
            for phrase in [
                "I apologize for the trouble.",
                "I apologize for any confusion.",
                "I'm sorry for the inconvenience.",
            ]:
                text = text.replace(phrase, "")

            return {"text": text.strip(), "booking_intent": booking_intent}

        except Exception as e:
            logger.error(f"Gemini API error: {e}")
            return {
                "text": (
                    "I'm specialized in Burkan Engineering's fire safety and life safety services. "
                    "I can help you with VR training, AI Powered Audit Dashboard, or consulting services. "
                    "What would you like to know about our services?"
                ),
                "booking_intent": False,
            }

    def clear_session(self, session_id: str):
        if session_id in self.chat_sessions:
            del self.chat_sessions[session_id]
