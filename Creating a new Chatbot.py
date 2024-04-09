import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
  response = openai.ChatComletion.create(
    modle="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
  )
  
  
  return response.choices[0].message.content.strip()
  
  
if __name == "__main__":
   while True:
     user_input = input("You: ")
     if user_input.lower() in ["quite", "exit", "bye",]:
         break
         
     response = chat_with_gpt(user_input) 
     print("Chatbot ", response)  