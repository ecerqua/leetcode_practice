from google import genai

def ai_tutor(prompt):
    api_key = "AIzaSyC6EpTY47Zors4FfeyJ8XrLW5Ti2MgFwgk"
    client = genai.Client(api_key=api_key)
    system_prompt = "You are a helpful programming tutor answering questions" \
    "from your students. You should never give away the answer but should just" \
    "nudge them in the right direction when they don't understand. If they don't" \
    "have a specific question you should simply try explaing the problem" \
    "and the theory behind it more thoroughly."

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"{system_prompt}\n\n---USER QUESTION---\n\n{prompt}")
    
    return response.text
    


if __name__ == "__main__":
    response = ai_tutor(prompt="testing")
    print(response.text)