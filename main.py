# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, EmailStr, validator
# import uuid, os, logging
# from typing import Optional
# from datetime import datetime
# from dotenv import load_dotenv
# import pandas as pd
# from pathlib import Path

# from gemini_client import GeminiChatbot
# from intent_handler import IntentHandler

# load_dotenv()
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# app = FastAPI(title="Burkan Engineering Chatbot API", version="1.0.0")

# allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=allowed_origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# gemini_bot = GeminiChatbot(api_key=os.getenv("GEMINI_API_KEY"))
# intent_handler = IntentHandler()
# active_sessions = {}

# EXCEL_FILE = "burkan_leads.xlsx"

# def save_to_excel(data: dict):
#     try:
#         file_path = Path(EXCEL_FILE)
        
#         if file_path.exists():
#             df = pd.read_excel(EXCEL_FILE)
#         else:
#             df = pd.DataFrame(columns=[
#                 "Timestamp", "Name", "Email", "Phone", 
#                 "Service Type", "Message", "Session ID"
#             ])
        
#         new_row = pd.DataFrame([{
#             "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             "Name": data.get("name", ""),
#             "Email": data.get("email", ""),
#             "Phone": data.get("phone", ""),
#             "Service Type": data.get("service_type", ""),
#             "Message": data.get("message", ""),
#             "Session ID": data.get("session_id", "")
#         }])
        
#         df = pd.concat([df, new_row], ignore_index=True)
#         df.to_excel(EXCEL_FILE, index=False, engine='openpyxl')
#         logger.info(f"Data saved to {EXCEL_FILE}")
#         return True
#     except Exception as e:
#         logger.error(f"Error saving to Excel: {e}")
#         return False

# class ChatMessage(BaseModel):
#     message: str
#     session_id: Optional[str] = None
#     button_id: Optional[str] = None
    
#     @validator('message')
#     def non_empty(cls, v):
#         if not v.strip():
#             raise ValueError('Message cannot be empty')
#         return v.strip()

# class RegistrationData(BaseModel):
#     name: str
#     email: EmailStr
#     phone: str
#     service_type: str
#     message: Optional[str] = ""
#     session_id: Optional[str] = None
    
#     @validator('name')
#     def not_empty(cls, v):
#         if not v.strip():
#             raise ValueError('Name is required')
#         return v.strip()

# @app.get("/")
# def root():
#     return {"service": "Burkan Engineering Chatbot API", "status": "running", "version": "1.0.0"}

# @app.get("/api/health")
# def health_check():
#     return {"status": "healthy", "gemini": "connected"}

# @app.post("/api/chat")
# def chat(data: ChatMessage):
#     try:
#         session_id = data.session_id or str(uuid.uuid4())
#         if session_id not in active_sessions:
#             active_sessions[session_id] = {"messages": [], "context": {}}

#         # ---------- BUTTON FLOWS ----------
#         if data.button_id:
#             if data.button_id == "vr_training":
#                 response = intent_handler.get_vr_training_options()

#             elif data.button_id == "ai_dashboard":
#                 response = intent_handler.get_ai_dashboard_options()

#             elif data.button_id == "consulting":
#                 response = intent_handler.get_consulting_response()

#             elif data.button_id in ["vr_custom", "ai_custom", "consulting_custom"]:
#                 response = intent_handler.get_custom_requirement_form()

#             elif data.button_id in [
#                 "vr_individual", "vr_team", "vr_workshop",
#                 "ai_1lakh", "ai_10lakh", "ai_20lakh", "ai_30plus"
#             ]:
#                 # final VR/AI detail cards (already return Book an Appointment button)
#                 response = intent_handler.get_service_details(data.button_id)

#             elif data.button_id in ["book_demo"]:
#                 response = {
#                     "text": "Excellent choice! To schedule your demo, please share your contact details and our team will reach out within 24 hours.",
#                     "needs_form": True
#                 }

#             else:
#                 response = {"text": "Let me know how else I can help you!", "buttons": []}

#         # ---------- TEXT FLOWS ----------
#         else:
#             intent = intent_handler.classify_intent(data.message)
#             logger.info(f"Session {session_id[:8]}: Intent - {intent}")

#             confirmations = ["yes", "yeah", "yep", "sure", "ok", "okay"]
#             msg_lower = data.message.strip().lower()

#             # 1) If user is in consulting flow and agrees → send booking payload
#             last_intent = active_sessions[session_id]["context"].get("last_intent")

#             if last_intent == "consulting_inquiry" and msg_lower in confirmations:
#                 booking_payload = intent_handler.get_consulting_booking()
#                 response = booking_payload
#                 active_sessions[session_id]["context"]["last_intent"] = "consulting_booking"

#             # 2) Normal intent-based routing
#             elif intent == "greeting":
#                 response = intent_handler.get_greeting()
#                 active_sessions[session_id]["context"]["last_intent"] = "greeting"

#             elif intent == "vr_training_inquiry":
#                 response = intent_handler.get_vr_training_options()
#                 active_sessions[session_id]["context"]["last_intent"] = "vr_training_inquiry"

#             elif intent == "ai_dashboard_inquiry":
#                 response = intent_handler.get_ai_dashboard_options()
#                 active_sessions[session_id]["context"]["last_intent"] = "ai_dashboard_inquiry"

#             elif intent == "consulting_inquiry":
#                 response = intent_handler.get_consulting_response()
#                 active_sessions[session_id]["context"]["last_intent"] = "consulting_inquiry"

#             elif intent == "registration":
#                 response = {
#                     "text": intent_handler.get_registration_prompt(),
#                     "needs_form": True
#                 }
#                 active_sessions[session_id]["context"]["last_intent"] = "registration"

#             else:
#                 # 3) Fallback to Gemini for general Burkan questions
#                 ai_response = gemini_bot.get_response(data.message, session_id)
#                 response = {"text": ai_response}
#                 active_sessions[session_id]["context"]["last_intent"] = intent

#         # ---------- LOG & RETURN ----------
#         active_sessions[session_id]["messages"].append({
#             "role": "user",
#             "content": data.message,
#             "button_id": data.button_id,
#             "timestamp": datetime.utcnow().isoformat()
#         })

#         return {
#             "response": response.get("text", response) if isinstance(response, dict) else response,
#             "buttons": response.get("buttons", []) if isinstance(response, dict) else [],
#             "needs_form": response.get("needs_form", False) if isinstance(response, dict) else False,
#             "needs_custom_form": response.get("needs_custom_form", False) if isinstance(response, dict) else False,
#             "session_id": session_id,
#             "timestamp": datetime.utcnow().isoformat()
#         }

#     except Exception as e:
#         logger.error(f"Error: {e}")
#         raise HTTPException(status_code=500, detail="Internal server error")

# @app.post("/api/register")
# def register(data: RegistrationData):
#     try:
#         save_success = save_to_excel({
#             "name": data.name,
#             "email": data.email,
#             "phone": data.phone,
#             "service_type": data.service_type,
#             "message": data.message,
#             "session_id": data.session_id
#         })
        
#         if save_success:
#             return {
#                 "status": "success",
#                 "message": f"Thank you, {data.name}! Our team will contact you at {data.email} within 24 hours regarding {data.service_type}."
#             }
#         else:
#             return {
#                 "status": "success",
#                 "message": f"Thank you, {data.name}! Your details have been received. Our team will contact you soon."
#             }
#     except Exception as e:
#         logger.error(f"Registration error: {e}")
#         raise HTTPException(status_code=500, detail="Error processing registration")

# @app.post("/api/clear-session/{session_id}")
# def clear_session(session_id: str):
#     if session_id in active_sessions:
#         del active_sessions[session_id]
#     gemini_bot.clear_session(session_id)
#     return {"status": "success"}

#code 2
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, validator
import uuid, os, logging
from typing import Optional
from datetime import datetime
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path

from gemini_client import GeminiChatbot
from intent_handler import IntentHandler

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Burkan Engineering Chatbot API", version="1.0.0")

allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

gemini_bot = GeminiChatbot(api_key=os.getenv("GEMINI_API_KEY", ""))
intent_handler = IntentHandler()
active_sessions = {}

EXCEL_FILE = "burkan_leads.xlsx"

def save_to_excel(data: dict):
    try:
        file_path = Path(EXCEL_FILE)
        if file_path.exists():
            df = pd.read_excel(EXCEL_FILE)
        else:
            df = pd.DataFrame(
                columns=[
                    "Timestamp", "Name", "Email", "Phone",
                    "Service Type", "Message", "Session ID",
                ]
            )
        new_row = pd.DataFrame(
            [{
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": data.get("name", ""),
                "Email": data.get("email", ""),
                "Phone": data.get("phone", ""),
                "Service Type": data.get("service_type", ""),
                "Message": data.get("message", ""),
                "Session ID": data.get("session_id", ""),
            }]
        )
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")
        logger.info(f"Data saved to {EXCEL_FILE}")
        return True
    except Exception as e:
        logger.error(f"Error saving to Excel: {e}")
        return False

class ChatMessage(BaseModel):
    message: str
    session_id: Optional[str] = None
    button_id: Optional[str] = None

    @validator("message")
    def non_empty(cls, v):
        if not v.strip():
            raise ValueError("Message cannot be empty")
        return v.strip()

class RegistrationData(BaseModel):
    name: str
    email: EmailStr
    phone: str
    service_type: str
    message: Optional[str] = ""
    session_id: Optional[str] = None

    @validator("name")
    def not_empty(cls, v):
        if not v.strip():
            raise ValueError("Name is required")
        return v.strip()

@app.get("/")
def root():
    return {
        "service": "Burkan Engineering Chatbot API",
        "status": "running",
        "version": "1.0.0",
    }

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "gemini": "connected"}

@app.post("/api/chat")
def chat(data: ChatMessage):
    try:
        session_id = data.session_id or str(uuid.uuid4())
        if session_id not in active_sessions:
            active_sessions[session_id] = {"messages": [], "context": {}}

        context = active_sessions[session_id]["context"]

        # ---------- BUTTON FLOWS ----------
        if data.button_id:
            if data.button_id == "vr_training":
                response = intent_handler.get_vr_training_options()

            elif data.button_id == "ai_dashboard":
                response = intent_handler.get_ai_dashboard_options()

            elif data.button_id == "consulting":
                response = intent_handler.get_consulting_response()
                context["last_intent"] = "consulting_inquiry"

            elif data.button_id in ["vr_custom", "ai_custom", "consulting_custom"]:
                response = intent_handler.get_custom_requirement_form()

            elif data.button_id in [
                "vr_individual", "vr_team", "vr_workshop",
                "ai_1lakh", "ai_10lakh", "ai_20lakh", "ai_30plus",
            ]:
                response = intent_handler.get_service_details(data.button_id)
                context["last_intent"] = "service_details"

            elif data.button_id in ["book_demo"]:
                response = {
                    "text": (
                        "Excellent choice! To schedule your demo, please share your contact "
                        "details and our team will reach out within 24 hours."
                    ),
                    "needs_form": True,
                }

            else:
                response = {"text": "Let me know how else I can help you!", "buttons": []}

        # ---------- TEXT FLOWS ----------
        else:
            user_text = data.message.strip()
            msg_lower = user_text.lower()

            # ---- UNIVERSAL BOOKING/ENQUIRY INTENT DETECTION ----
            booking_phrases = [
                "book", "appointment", "enquiry", "inquiry", "consult",
                "schedule", "demo", "can i book", "want to book", "need an appointment",
                "can we schedule", "can we book"
            ]
            if any(phrase in msg_lower for phrase in booking_phrases):
                response = intent_handler.get_consulting_booking()
                context["last_intent"] = "universal_booking"

            else:
                last_intent = context.get("last_intent")
                confirmations = ["yes", "yeah", "yep", "sure", "ok", "okay"]

                # 1) Fire Risk Assessment (first detail)
                if "fire risk assessment" in msg_lower or "fire risk assessments" in msg_lower:
                    response = {
                        "text": (
                            "Burkan Engineering provides comprehensive Fire Risk Assessments to identify "
                            "potential fire hazards in your facility and evaluate existing safety measures. "
                            "Our consultants review your layouts, systems and operations to ensure "
                            "compliance with fire and life safety codes and to reduce risk for people and property.\n\n"
                            "Would you like to consult our experts or do you have any specific enquiry about a "
                            "Fire Risk Assessment for your site?"
                        ),
                        "buttons": []
                    }
                    context["last_intent"] = "fra_info"

                # 2) Fire Risk Assessment more info
                elif last_intent == "fra_info" and (
                    "tell me more" in msg_lower
                    or "more details" in msg_lower
                    or "how does it work" in msg_lower
                    or "what is included" in msg_lower
                ):
                    response = {
                        "text": (
                            "In a Fire Risk Assessment, we study your processes, layouts, storage, occupancy and existing "
                            "protection systems to identify credible fire scenarios. We then assess likelihood and impact, "
                            "evaluate your current controls and recommend additional measures so that your risk is "
                            "reduced to an acceptable, code-compliant level."
                        ),
                        "buttons": []
                    }
                    # keep last_intent as fra_info

                # 3) After Risk Assessment info, confirm triggers booking button
                elif last_intent == "fra_info" and (
                    msg_lower in confirmations
                    or "enquiry" in msg_lower
                    or "inquiry" in msg_lower
                    or "consult" in msg_lower
                    or "book" in msg_lower
                    or "schedule" in msg_lower
                ):
                    response = intent_handler.get_consulting_booking()
                    context["last_intent"] = "fra_booking"

                # 4) Safety Compliance Audits (first detail)
                elif "safety compliance audit" in msg_lower or "safety compliance audits" in msg_lower:
                    response = {
                        "text": (
                            "Our Safety Compliance Audits review your facility against applicable fire and life "
                            "safety codes, standards and local regulations. We inspect documentation, systems and "
                            "on-ground practices, then provide a clear gap report with prioritized corrective actions.\n\n"
                            "Would you like to consult our experts or raise a specific enquiry about a Safety Compliance Audit "
                            "for your site?"
                        ),
                        "buttons": []
                    }
                    context["last_intent"] = "safety_audit_info"

                # 5) Safety Compliance Audits more info
                elif last_intent == "safety_audit_info" and (
                    "tell me more" in msg_lower
                    or "more details" in msg_lower
                    or "how does it work" in msg_lower
                    or "what is included" in msg_lower
                ):
                    response = {
                        "text": (
                            "During a Safety Compliance Audit, our engineers visit your site to review fire protection "
                            "systems, passive fire measures, documentation and actual practices. We map findings "
                            "against NBC India/NFPA/local bye-laws, assign risk levels and give you a prioritized action "
                            "plan with practical timelines so you know exactly what to fix and when."
                        ),
                        "buttons": []
                    }
                    # keep last_intent as safety_audit_info

                # 6) After Safety Audit info, confirm triggers booking
                elif last_intent == "safety_audit_info" and (
                    msg_lower in confirmations
                    or "enquiry" in msg_lower
                    or "inquiry" in msg_lower
                    or "consult" in msg_lower
                    or "book" in msg_lower
                    or "schedule" in msg_lower
                ):
                    response = intent_handler.get_consulting_booking()
                    context["last_intent"] = "safety_audit_booking"

                # ... (Repeat all other consulting services and their "tell me more"/booking logic as you have it)

                else:
                    intent = intent_handler.classify_intent(user_text)
                    logger.info(f"Session {session_id[:8]}: Intent - {intent}")

                    if intent == "greeting":
                        response = intent_handler.get_greeting()
                        context["last_intent"] = "greeting"
                    elif intent == "vr_training_inquiry":
                        response = intent_handler.get_vr_training_options()
                        context["last_intent"] = "vr_training_inquiry"
                    elif intent == "ai_dashboard_inquiry":
                        response = intent_handler.get_ai_dashboard_options()
                        context["last_intent"] = "ai_dashboard_inquiry"
                    elif intent == "consulting_inquiry":
                        response = intent_handler.get_consulting_response()
                        context["last_intent"] = "consulting_inquiry"
                    elif intent == "registration":
                        response = {
                            "text": intent_handler.get_registration_prompt(),
                            "needs_form": True,
                        }
                        context["last_intent"] = "registration"
                    else:
                        ai_result = gemini_bot.get_response(user_text, session_id)
                        ai_text = ai_result.get("text", "")
                        booking_intent = bool(ai_result.get("booking_intent", False))
                        if booking_intent:
                            response = intent_handler.get_consulting_booking()
                            context["last_intent"] = "ai_detected_booking"
                        else:
                            response = {"text": ai_text}
                            context["last_intent"] = intent

        active_sessions[session_id]["messages"].append(
            {
                "role": "user",
                "content": data.message,
                "button_id": data.button_id,
                "timestamp": datetime.utcnow().isoformat(),
            }
        )

        return {
            "response": response.get("text", response) if isinstance(response, dict) else response,
            "buttons": response.get("buttons", []) if isinstance(response, dict) else [],
            "needs_form": response.get("needs_form", False)
            if isinstance(response, dict)
            else False,
            "needs_custom_form": response.get("needs_custom_form", False)
            if isinstance(response, dict)
            else False,
            "session_id": session_id,
            "timestamp": datetime.utcnow().isoformat(),
        }

    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/api/register")
def register(data: RegistrationData):
    try:
        save_success = save_to_excel(
            {
                "name": data.name,
                "email": data.email,
                "phone": data.phone,
                "service_type": data.service_type,
                "message": data.message,
                "session_id": data.session_id,
            }
        )

        if save_success:
            return {
                "status": "success",
                "message": (
                    f"Thank you, {data.name}! Our team will contact you at {data.email} "
                    f"within 24 hours regarding {data.service_type}."
                ),
            }
        else:
            return {
                "status": "success",
                "message": (
                    f"Thank you, {data.name}! Your details have been received. "
                    "Our team will contact you soon."
                ),
            }
    except Exception as e:
        logger.error(f"Registration error: {e}")
        raise HTTPException(status_code=500, detail="Error processing registration")

@app.post("/api/clear-session/{session_id}")
def clear_session(session_id: str):
    if session_id in active_sessions:
        del active_sessions[session_id]
    gemini_bot.clear_session(session_id)
    return {"status": "success"}
