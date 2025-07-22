# import os
# import google.generativeai as genai

# GEMINI_API_KEY = "AIzaSyC-apytQpAtMb_dGJ6lkYsDaUk8ChK2l2M"  # Replace with your API key
# genai.configure(api_key= "AIzaSyC-apytQpAtMb_dGJ6lkYsDaUk8ChK2l2M")


# model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
# response = model.generate_content("Hello! What can you do?")
# print(response.text)






# GEMINI_API_KEY = "AIzaSyC-apytQpAtMb_dGJ6lkYsDaUk8ChK2l2M"  # Replace with your API key
# genai.configure(api_key= "AIzaSyC-apytQpAtMb_dGJ6lkYsDaUk8ChK2l2M")


# gemini_enabled = True

# def chat_with_gemini(prompt):
#     try:
#         model = genai.GenerativeModel("models/gemini-1.5-pro")
        
#         # 🔥 Force a direct, short answer (2-3 lines max)
#         short_prompt = f"Answer in 2-3 sentences only: {prompt}"

#         response = model.generate_content(short_prompt)
#         answer = response.text.strip() if response else "I didn't understand that."

#         # 🔹 Limit answer to max 2-3 sentences
#         short_answer = ". ".join(answer.split(". ")[:2])  # Only take the first 2 sentences

#         print("Jarvis:", short_answer)  # Print response
#         TTS(short_answer)  # Speak response

#         return short_answer

#     except Exception as e:
#         error_message = f"Error: {str(e)}"
#         print(error_message)
#         TTS(error_message)
#         return error_message



import google.generativeai as genai

genai.configure(api_key="AIzaSyADOYZ6hKcscjvySJ-G8XhkFA94bOStzp4")

model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
response = model.generate_content("What is 2 + 2?")
print(response.text)

