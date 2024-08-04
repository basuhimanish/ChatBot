import google.generativeai as genai
API_KEY="AIzaSyAKXKtG1sQc4WOdwd83d9XgnuRXgKJpxuY"

genai.configure(
    api_key=API_KEY
)

model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

# instruction=" in short"
while(True):
    question=input("You: ")

    if(question.strip()=='bye'):
        break

    response= chat.send_message(question)
    # print(question+instruction)
    print("\n")
    print(f"Bot:{response.text}")
    print("\n")
    # instruction=""
