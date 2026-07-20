class VoiceToActionExecutorClient:
    ACTION_RULES = [
        (["schedule", "meeting", "call"], "CALENDAR_CREATE"),
        (["send", "email", "message", "write"], "EMAIL_COMPOSE"),
        (["search", "find", "look", "show"], "WEB_SEARCH"),
        (["remind", "reminder", "alarm"], "REMINDER_SET"),
        (["create", "make", "build", "draft"], "DOCUMENT_CREATE"),
        (["summarize", "summary", "brief"], "SUMMARIZE"),
        (["translate", "translation"], "TRANSLATE"),
    ]

    def parse(self, voice_transcript: str) -> dict:
        text_lower = voice_transcript.lower()
        words = set(text_lower.split())
        best_action, best_score = "GENERAL_QUERY", 0
        for keywords, action in self.ACTION_RULES:
            score = sum(1 for kw in keywords if kw in words)
            if score > best_score:
                best_score, best_action = score, action
        payload = {
            "original_text": voice_transcript,
            "extracted_intent": best_action,
            "key_entities": [w for w in voice_transcript.split() if len(w) > 4][:5]
        }
        confidence = round(min(best_score / 2.0, 1.0), 2) if best_score else 0.3
        return {"action_type": best_action, "action_payload": payload, "confidence": confidence}
