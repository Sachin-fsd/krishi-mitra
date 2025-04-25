from groq import Groq  

def chat_with_groq(user_input, api_key, language="english"):
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": f"You are an agricultural expert assistant. Provide helpful, accurate information about farming, crops, and agricultural practices. return answer in  only {language} langugage"},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"