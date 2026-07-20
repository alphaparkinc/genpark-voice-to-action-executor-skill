from client import VoiceToActionExecutorClient
client = VoiceToActionExecutorClient()
result = client.parse("Schedule a meeting with the design team for tomorrow at 3pm")
print(f"Action: {result['action_type']} (confidence: {result['confidence']})")
print(f"Payload: {result['action_payload']}")
