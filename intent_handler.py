# class IntentHandler:
#     def __init__(self):
#         self.intents = {
#             "greeting": ["hello", "hi", "hey", "good morning", "namaste", "start"],
#             "registration": ["register", "sign up", "enroll", "webinar", "join", "book"],
#             "vr_training_inquiry": ["vr training", "virtual reality", "vr", "immersive", "virtual training"],
#             "ai_dashboard_inquiry": ["ai dashboard", "dashboard", "monitoring", "audit", "ai powered"],
#             "consulting_inquiry": ["consulting", "fire consulting", "safety consulting", "consultant", "advice"],
#             "custom_requirement": ["custom", "own requirement", "specific needs", "tailored"]
#         }

#     def classify_intent(self, message: str) -> str:
#         message_lower = message.lower()
#         for intent, keywords in self.intents.items():
#             if any(keyword in message_lower for keyword in keywords):
#                 return intent
#         return "general"

#     def get_greeting(self) -> dict:
#         return {
#             "text": "Hello! Welcome to Burkan Engineering! 🔥\n\nHow can I help you today?",
#             "buttons": [
#                 {"id": "vr_training", "text": "VR Fire Safety Training"},
#                 {"id": "ai_dashboard", "text": "AI Powered Audit Dashboard"},
#                 {"id": "consulting", "text": "Fire Consulting Services"}
#             ]
#         }

#     def get_vr_training_options(self) -> dict:
#         return {
#             "text": "🔥 **VR Fire Safety Training Options**\n\nImmersive, hands-on fire safety training using Virtual Reality technology.\n\nSelect your package:",
#             "buttons": [
#                 {"id": "vr_individual", "text": "Individual VR (Up to 20 users)"},
#                 {"id": "vr_team", "text": "Team VR with Projector (Min 500)"},
#                 {"id": "vr_workshop", "text": "Workshop 8hrs (Min 500)"},
#                 {"id": "vr_custom", "text": "📝 Custom Requirement"}
#             ]
#         }

#     def get_ai_dashboard_options(self) -> dict:
#         return {
#             "text": "🔥 **AI Powered Audit Dashboard Packages**\n\n*3/5 Year Plans + 1 Free Comprehensive Audit*\n\nReal-time fire safety monitoring with predictive analytics.\n\nSelect your facility size:",
#             "buttons": [
#                 {"id": "ai_1lakh", "text": "1 Lakh Sqft"},
#                 {"id": "ai_10lakh", "text": "10 Lakhs Sqft"},
#                 {"id": "ai_20lakh", "text": "20 Lakhs Sqft"},
#                 {"id": "ai_30plus", "text": "30+ Lakhs Sqft"},
#                 {"id": "ai_custom", "text": "📝 Custom Requirement"}
#             ]
#         }

#     def get_consulting_response(self) -> dict:
#         return {
#             "text": "Great! I can help you with our Fire Safety Consulting Services. 🔥\n\nWe offer:\n\n✓ Fire Risk Assessments\n✓ Safety Compliance Audits\n✓ Fire Protection System Design\n✓ Code Compliance Consulting\n✓ Emergency Evacuation Planning\n\nWhat specific fire safety challenge can I help you with today?",
#             "buttons": [
#                 {"id": "consulting_custom", "text": "📝 Share My Requirement"}
#             ]
#         }

#     def get_custom_requirement_form(self) -> dict:
#         return {
#             "text": "Please share your specific requirements and our team will provide a customized solution for you.",
#             "needs_custom_form": True
#         }

#     def get_service_details(self, service_id: str) -> dict:
#         details = {
#             "vr_individual": {
#                 "text": "**Individual VR Training** (Up to 20 users)\n\n✓ Immersive hands-on experience\n✓ Perfect for small teams\n✓ Expert-led sessions\n✓ Safety certification included\n\nThis interactive training helps your team practice fire safety scenarios in a safe, controlled virtual environment.",
#                 "buttons": [{"id": "book_demo", "text": "📅 Book a Demo"}]
#             },
#             "vr_team": {
#                 "text": "**Team VR Training with Projector** (Min 500 people)\n\n✓ Large-scale group training\n✓ Interactive collaborative learning\n✓ Projector display for all attendees\n✓ Professional certification\n\nIdeal for company-wide safety training programs.",
#                 "buttons": [{"id": "book_demo", "text": "📅 Book a Demo"}]
#             },
#             "vr_workshop": {
#                 "text": "**Audience Workshop Training** (8 hours, Min 500 people)\n\n✓ Comprehensive fire safety program\n✓ Full-day intensive training\n✓ Hands-on practice sessions\n✓ Official certification\n\nOur most complete training package for organizations.",
#                 "buttons": [{"id": "book_demo", "text": "📅 Book a Demo"}]
#             },
#             "ai_1lakh": {
#                 "text": "**AI Powered Audit Dashboard - 1 Lakh Sqft Package**\n\n✓ Real-time fire safety monitoring\n✓ Predictive analytics & alerts\n✓ 24/7 cloud access\n✓ 1 Free comprehensive audit\n\nPerfect for small to medium facilities.",
#                 "buttons": [{"id": "book_demo", "text": "📅 Schedule Demo"}]
#             },
#             "ai_10lakh": {
#                 "text": "**AI Powered Audit Dashboard - 10 Lakhs Sqft Package**\n\n✓ Advanced monitoring for large facilities\n✓ Automated compliance tracking\n✓ Incident management system\n✓ 1 Free comprehensive audit\n\nIdeal for large commercial buildings.",
#                 "buttons": [{"id": "book_demo", "text": "📅 Schedule Demo"}]
#             },
#             "ai_20lakh": {
#                 "text": "**AI Powered Audit Dashboard - 20 Lakhs Sqft Package**\n\n✓ Enterprise-grade monitoring\n✓ Multi-building support\n✓ Advanced analytics dashboard\n✓ Priority support + Free audit\n\nDesigned for industrial complexes.",
#                 "buttons": [{"id": "book_demo", "text": "📅 Schedule Demo"}]
#             },
#             "ai_30plus": {
#                 "text": "**AI Powered Audit Dashboard - 30+ Lakhs Sqft Package**\n\n✓ Custom enterprise solution\n✓ Unlimited facility coverage\n✓ Dedicated account manager\n✓ Quarterly audits included\n\nOur premium package for mega facilities.",
#                 "buttons": [{"id": "book_demo", "text": "📅 Schedule Demo"}]
#             }
#         }
#         return details.get(service_id, {"text": "Service details unavailable", "buttons": []})

#     def get_registration_prompt(self) -> str:
#         return "Excellent! To proceed with your demo booking, please provide:\n• Your Name\n• Email Address\n• Phone Number\n• Service you're interested in\n\nOur team will reach out within 24 hours."


# Code 2
# class IntentHandler:
#     def __init__(self):
#         self.intents = {
#             "greeting": ["hello", "hi", "hey", "good morning", "namaste", "start"],
#             "registration": ["register", "sign up", "enroll", "webinar", "join", "book"],
#             "vr_training_inquiry": ["vr training", "virtual reality", "vr", "immersive", "virtual training"],
#             "ai_dashboard_inquiry": ["ai dashboard", "dashboard", "monitoring", "audit", "ai powered"],
#             "consulting_inquiry": ["consulting", "fire consulting", "safety consulting", "consultant", "advice"],
#             "custom_requirement": ["custom", "own requirement", "specific needs", "tailored"],
#         }

#     def classify_intent(self, message: str) -> str:
#         message_lower = message.lower()
#         for intent, keywords in self.intents.items():
#             if any(keyword in message_lower for keyword in keywords):
#                 return intent
#         return "general"

#     def get_greeting(self) -> dict:
#         return {
#             "text": "Hello! Welcome to Burkan Engineering! 🔥\n\nHow can I help you today?",
#             "buttons": [
#                 {"id": "vr_training", "text": "VR Fire Safety Training"},
#                 {"id": "ai_dashboard", "text": "AI Powered Audit Dashboard"},
#                 {"id": "consulting", "text": "Fire Consulting Services"},
#             ],
#         }

#     def get_vr_training_options(self) -> dict:
#         return {
#             "text": "🔥 **VR Fire Safety Training Options**\n\nImmersive, hands-on fire safety training using Virtual Reality technology.\n\nSelect your package:",
#             "buttons": [
#                 {"id": "vr_individual", "text": "Individual VR (Up to 20 users)"},
#                 {"id": "vr_team", "text": "Team VR with Projector (Min 500)"},
#                 {"id": "vr_workshop", "text": "Workshop 8hrs (Min 500)"},
#                 {"id": "vr_custom", "text": "📝 Custom Requirement"},
#             ],
#         }

#     def get_ai_dashboard_options(self) -> dict:
#         return {
#             "text": "🔥 **AI Powered Audit Dashboard Packages**\n\n*3/5 Year Plans + 1 Free Comprehensive Audit*\n\nReal-time fire safety monitoring with predictive analytics.\n\nSelect your facility size:",
#             "buttons": [
#                 {"id": "ai_1lakh", "text": "1 Lakh Sqft"},
#                 {"id": "ai_10lakh", "text": "10 Lakhs Sqft"},
#                 {"id": "ai_20lakh", "text": "20 Lakhs Sqft"},
#                 {"id": "ai_30plus", "text": "30+ Lakhs Sqft"},
#                 {"id": "ai_custom", "text": "📝 Custom Requirement"},
#             ],
#         }

#     def get_consulting_response(self) -> dict:
#         return {
#             "text": (
#                 "Great! I can help you with our Fire Safety Consulting Services. 🔥\n\n"
#                 "We offer:\n\n"
#                 "✓ Fire Risk Assessments\n"
#                 "✓ Safety Compliance Audits\n"
#                 "✓ Fire Protection System Design\n"
#                 "✓ Code Compliance Consulting\n"
#                 "✓ Emergency Evacuation Planning\n\n"
#                 "What specific fire safety challenge can I help you with today?"
#             ),
#             "buttons": [
#                 {"id": "consulting_custom", "text": "📝 Share My Requirement"},
#             ],
#         }

#     def get_custom_requirement_form(self) -> dict:
#         return {
#             "text": "Please share your specific requirements and our team will provide a customized solution for you.",
#             "needs_custom_form": True,
#         }

#     def get_service_details(self, service_id: str) -> dict:
#         details = {
#             "vr_individual": {
#                 "text": (
#                     "**Individual VR Training** (Up to 20 users)\n\n"
#                     "✓ Immersive hands-on experience\n"
#                     "✓ Perfect for small teams\n"
#                     "✓ Expert-led sessions\n"
#                     "✓ Safety certification included\n\n"
#                     "This interactive training helps your team practice fire safety scenarios "
#                     "in a safe, controlled virtual environment."
#                 ),
#                 "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
#             },
#             "vr_team": {
#                 "text": (
#                     "**Team VR Training with Projector** (Min 500 people)\n\n"
#                     "✓ Large-scale group training\n"
#                     "✓ Interactive collaborative learning\n"
#                     "✓ Projector display for all attendees\n"
#                     "✓ Professional certification\n\n"
#                     "Ideal for company-wide safety training programs."
#                 ),
#                 "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
#             },
#             "vr_workshop": {
#                 "text": (
#                     "**Audience Workshop Training** (8 hours, Min 500 people)\n\n"
#                     "✓ Comprehensive fire safety program\n"
#                     "✓ Full-day intensive training\n"
#                     "✓ Hands-on practice sessions\n"
#                     "✓ Official certification\n\n"
#                     "Our most complete training package for organizations."
#                 ),
#                 "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
#             },
#             "ai_1lakh": {
#                 "text": (
#                     "**AI Powered Audit Dashboard - 1 Lakh Sqft Package**\n\n"
#                     "✓ Real-time fire safety monitoring\n"
#                     "✓ Predictive analytics & alerts\n"
#                     "✓ 24/7 cloud access\n"
#                     "✓ 1 Free comprehensive audit\n\n"
#                     "Perfect for small to medium facilities."
#                 ),
#                 "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
#             },
#             "ai_10lakh": {
#                 "text": (
#                     "**AI Powered Audit Dashboard - 10 Lakhs Sqft Package**\n\n"
#                     "✓ Advanced monitoring for large facilities\n"
#                     "✓ Automated compliance tracking\n"
#                     "✓ Incident management system\n"
#                     "✓ 1 Free comprehensive audit\n\n"
#                     "Ideal for large commercial buildings."
#                 ),
#                 "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
#             },
#             "ai_20lakh": {
#                 "text": (
#                     "**AI Powered Audit Dashboard - 20 Lakhs Sqft Package**\n\n"
#                     "✓ Enterprise-grade monitoring\n"
#                     "✓ Multi-building support\n"
#                     "✓ Advanced analytics dashboard\n"
#                     "✓ Priority support + Free audit\n\n"
#                     "Designed for industrial complexes."
#                 ),
#                 "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
#             },
#             "ai_30plus": {
#                 "text": (
#                     "**AI Powered Audit Dashboard - 30+ Lakhs Sqft Package**\n\n"
#                     "✓ Custom enterprise solution\n"
#                     "✓ Unlimited facility coverage\n"
#                     "✓ Dedicated account manager\n"
#                     "✓ Quarterly audits included\n\n"
#                     "Our premium package for mega facilities."
#                 ),
#                 "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
#             },
#         }
#         return details.get(service_id, {"text": "Service details unavailable", "buttons": []})

#     def get_registration_prompt(self) -> str:
#         return (
#             "Excellent! To proceed with your booking, please provide:\n"
#             "• Your Name\n"
#             "• Email Address\n"
#             "• Phone Number\n"
#             "• Service you're interested in\n\n"
#             "Our team will reach out within 24 hours."
#         )

# Code 3
class IntentHandler:
    def __init__(self):
        self.intents = {
            "greeting": ["hello", "hi", "hey", "good morning", "namaste", "start"],
            "registration": ["register", "sign up", "enroll", "webinar", "join", "book"],
            "vr_training_inquiry": ["vr training", "virtual reality", "vr", "immersive", "virtual training"],
            "ai_dashboard_inquiry": ["ai dashboard", "dashboard", "monitoring", "audit", "ai powered"],
            "consulting_inquiry": ["consulting", "fire consulting", "safety consulting", "consultant", "advice"],
            "custom_requirement": ["custom", "own requirement", "specific needs", "tailored"],
        }

    def classify_intent(self, message: str) -> str:
        message_lower = message.lower()
        for intent, keywords in self.intents.items():
            if any(keyword in message_lower for keyword in keywords):
                return intent
        return "general"

    def get_greeting(self) -> dict:
        return {
            "text": "Hello! Welcome to Burkan Engineering! 🔥\n\nHow can I help you today?",
            "buttons": [
                {"id": "vr_training", "text": "VR Fire Safety Training"},
                {"id": "ai_dashboard", "text": "AI Powered Audit Dashboard"},
                {"id": "consulting", "text": "Fire Consulting Services"},
            ],
        }

    def get_vr_training_options(self) -> dict:
        return {
            "text": "🔥 **VR Fire Safety Training Options**\n\nImmersive, hands-on fire safety training using Virtual Reality technology.\n\nSelect your package:",
            "buttons": [
                {"id": "vr_individual", "text": "Individual VR (Up to 20 users)"},
                {"id": "vr_team", "text": "Team VR with Projector (Min 500)"},
                {"id": "vr_workshop", "text": "Workshop 8hrs (Min 500)"},
                {"id": "vr_custom", "text": "📝 Custom Requirement"},
            ],
        }

    def get_ai_dashboard_options(self) -> dict:
        return {
            "text": "🔥 **AI Powered Audit Dashboard Packages**\n\n*3/5 Year Plans + 1 Free Comprehensive Audit*\n\nReal-time fire safety monitoring with predictive analytics.\n\nSelect your facility size:",
            "buttons": [
                {"id": "ai_1lakh", "text": "1 Lakh Sqft"},
                {"id": "ai_10lakh", "text": "10 Lakhs Sqft"},
                {"id": "ai_20lakh", "text": "20 Lakhs Sqft"},
                {"id": "ai_30plus", "text": "30+ Lakhs Sqft"},
                {"id": "ai_custom", "text": "📝 Custom Requirement"},
            ],
        }

    def get_consulting_response(self) -> dict:
        return {
            "text": (
                "Great! I can help you with our Fire Safety Consulting Services. 🔥\n\n"
                "We offer:\n\n"
                "✓ Fire Risk Assessments\n"
                "✓ Safety Compliance Audits\n"
                "✓ Fire Protection System Design\n"
                "✓ Code Compliance Consulting\n"
                "✓ Emergency Evacuation Planning\n\n"
                "What specific fire safety challenge can I help you with today?"
            ),
            "buttons": [
                {"id": "book_appointment", "text": "📅 Book an Appointment"},
            ],
        }

    def get_custom_requirement_form(self) -> dict:
        return {
            "text": "Please share your specific requirements and our team will provide a customized solution for you.",
            "needs_custom_form": True,
        }

    def get_service_details(self, service_id: str) -> dict:
        details = {
            "vr_individual": {
                "text": (
                    "**Individual VR Training** (Up to 20 users)\n\n"
                    "✓ Immersive hands-on experience\n"
                    "✓ Perfect for small teams\n"
                    "✓ Expert-led sessions\n"
                    "✓ Safety certification included\n\n"
                    "This interactive training helps your team practice fire safety scenarios "
                    "in a safe, controlled virtual environment."
                ),
                "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
            },
            "vr_team": {
                "text": (
                    "**Team VR Training with Projector** (Min 500 people)\n\n"
                    "✓ Large-scale group training\n"
                    "✓ Interactive collaborative learning\n"
                    "✓ Projector display for all attendees\n"
                    "✓ Professional certification\n\n"
                    "Ideal for company-wide safety training programs."
                ),
                "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
            },
            "vr_workshop": {
                "text": (
                    "**Audience Workshop Training** (8 hours, Min 500 people)\n\n"
                    "✓ Comprehensive fire safety program\n"
                    "✓ Full-day intensive training\n"
                    "✓ Hands-on practice sessions\n"
                    "✓ Official certification\n\n"
                    "Our most complete training package for organizations."
                ),
                "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
            },
            "ai_1lakh": {
                "text": (
                    "**AI Powered Audit Dashboard - 1 Lakh Sqft Package**\n\n"
                    "✓ Real-time fire safety monitoring\n"
                    "✓ Predictive analytics & alerts\n"
                    "✓ 24/7 cloud access\n"
                    "✓ 1 Free comprehensive audit\n\n"
                    "Perfect for small to medium facilities."
                ),
                "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
            },
            "ai_10lakh": {
                "text": (
                    "**AI Powered Audit Dashboard - 10 Lakhs Sqft Package**\n\n"
                    "✓ Advanced monitoring for large facilities\n"
                    "✓ Automated compliance tracking\n"
                    "✓ Incident management system\n"
                    "✓ 1 Free comprehensive audit\n\n"
                    "Ideal for large commercial buildings."
                ),
                "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
            },
            "ai_20lakh": {
                "text": (
                    "**AI Powered Audit Dashboard - 20 Lakhs Sqft Package**\n\n"
                    "✓ Enterprise-grade monitoring\n"
                    "✓ Multi-building support\n"
                    "✓ Advanced analytics dashboard\n"
                    "✓ Priority support + Free audit\n\n"
                    "Designed for industrial complexes."
                ),
                "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
            },
            "ai_30plus": {
                "text": (
                    "**AI Powered Audit Dashboard - 30+ Lakhs Sqft Package**\n\n"
                    "✓ Custom enterprise solution\n"
                    "✓ Unlimited facility coverage\n"
                    "✓ Dedicated account manager\n"
                    "✓ Quarterly audits included\n\n"
                    "Our premium package for mega facilities."
                ),
                "buttons": [{"id": "book_appointment", "text": "📅 Book an Appointment"}],
            },
        }
        return details.get(service_id, {"text": "Service details unavailable", "buttons": []})

    def get_consulting_booking(self) -> dict:
        return {
            "text": (
                "Excellent. Our team can provide a detailed consultation to assess your "
                "facility's specific needs and ensure complete compliance.\n\n"
                "Use the button below to book an appointment with our fire safety specialist."
            ),
            "buttons": [
                {"id": "book_appointment", "text": "📅 Book an Appointment"}
            ],
        }

    def get_registration_prompt(self) -> str:
        return (
            "Excellent! To proceed with your booking, please provide:\n"
            "• Your Name\n"
            "• Email Address\n"
            "• Phone Number\n"
            "• Service you're interested in\n\n"
            "Our team will reach out within 24 hours."
        )
