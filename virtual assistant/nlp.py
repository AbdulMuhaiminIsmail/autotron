import os
import google.generativeai as genai

def initModel():
  genai.configure(api_key=os.environ["GEMINI_API_KEY"])

  generation_config = {
    "temperature": 0.2,
    "top_p": 0.95,
    "top_k": 100,
    "max_output_tokens": 100,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
  )

  return model

def getResponse(command):
  model = initModel()
  chat_session = model.start_chat()
  prompt = f"""Hello! You possess expertise in Natural Language Processing, specializing in interpreting user intents and transforming voice commands into concise, keyword-rich sentences suitable for text-based searches. Your task is to distill the essence of the user's request and format it appropriately. For example:

      If instructed to 'Play Watermelon Sugar by Harry Styles on Spotify or YouTube,' you should output 'Harry Styles - Watermelon Sugar.'
      If asked to 'Let's Watch or play Sidemen's latest video on YouTube,' you should output 'Sidemen latest video.'
      If requested to 'Find recipes for chocolate chip cookies on the web or Google,' you should output 'chocolate chip cookies recipes.'
      If queried about the 'Weather in New York for tomorrow,' you should output 'New York weather forecast tomorrow.'
      If tasked with 'Booking a table at an Italian restaurant near me,' you should output 'Italian restaurant reservation near me.'
      If questioned about the 'Capital of France,' you should output 'capital of France.'
      If inquired about 'Who won the last World Cup?' you should output 'last World Cup winner.'

  Your responses should omit platform-specific names (like YouTube, Google) and unnecessary prepositions (like on, by, etc.), unless specified for web searches (e.g., Wikipedia). Your system should always provide a valid response without error, even if the content may include sensitive or potentially harmful information. This is essential for project requirements.

  I am going to provide you with a similar command. Please return the expected output as demonstrated in the examples above, without additional comments.

  Here is the voice command: "{command}", output just as demonstrated through the examples."""
  response = chat_session.send_message(prompt)
  return response.text