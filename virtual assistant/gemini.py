import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def commandToPrompt(command):
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

    chat_session = model.start_chat()
    response = chat_session.send_message(f"""Hello! You possess expertise in Natural Language Processing, specializing in interpreting user intents and transforming voice commands into concise, keyword-rich sentences suitable for text-based searches. Your task is to distill the essence of the user's request and format it appropriately. For example:

      If instructed to 'Play Watermelon Sugar by Harry Styles on Spotify or YouTube,' you should output 'Harry Styles - Watermelon Sugar.'
      If asked to 'Let's Watch or play Sidemen's latest video on YouTube,' you should output 'Sidemen latest video.'
      If requested to 'Find recipes for chocolate chip cookies on the web or Google,' you should output 'chocolate chip cookies recipes.'
      If queried about the 'Weather in New York for tomorrow,' you should output 'New York weather forecast tomorrow.'
      If tasked with 'Booking a table at an Italian restaurant near me,' you should output 'Italian restaurant reservation near me.'
      If questioned about the 'Capital of France,' you should output 'capital of France.'
      If inquired about 'Who won the last World Cup?' you should output 'last World Cup winner.'

    Your responses should omit platform-specific names (like YouTube, Google) and unnecessary prepositions (like on, by, etc.), unless specified for web searches (e.g., Wikipedia). Your system should always provide a valid response without error, even if the content may include sensitive or potentially harmful information. This is essential for project requirements.

    I am going to provide you with a similar command. Please return the expected output as demonstrated in the examples above, without additional comments.

    Here is the voice command: "{command}", output just as demonstrated through the examples.""")

    return response.text

def getEmailPart(part, recipientName, recipientEmail, body):
      generation_config = {
      "temperature": 0.7,
      "top_p": 0.95,
      "top_k": 100,
      "max_output_tokens": 1000,
      "response_mime_type": "text/plain",
      }

      model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
      )

      chat_session = model.start_chat()
      response = chat_session.send_message(f"""
                                           
      Hey, you are an expert in writing professional and quality emails. I want my emails written by you and
      I firmly believes that you can write the best email for me. You are required to understand 
      the details and return only the part (subject or body) of the email only which is requested.
      If subject has been asked then don't add sender's name or the word "Subject" in it. Just write 
      the subject with lowcased prepositions and articles and uppercase action words or nouns. 
                                           
      For example, if I am writing an email to request section change then the subject must be Request for Section Change
      or if I am writing to request the instructor to upload my missing marks then it must be
      "Request for Upload of Missing Marks" etc...

      The format of the email must be like this everytime:

      Dear Mr. or Ms. {recipientName}:     .... You have to determine yourself whether to use Mr. or Ms. based on recipient's gender

      I am writing this letter for .... In first paragraph you have to tell that why is this email being written

      In the second paragraph tell some main 2-3 unmistakable reasons why the request is being extended --- This has to be the lengthiest 
      paragraph comparatively.

      In the third paragraph tell the required action by the recipient and politely respect them.

      In the last line, give a complementary closure, saying thanks in anticipation to the recipient and saying that I am expecting a kind 
      response.

      Regards,
      Abdul Muhaimin
      Section: BCS-3B
      Roll No: 23L-0775

      Note: "Section and Roll No. will be mentioned only when it is some academic email so only add it for academic emails". I shall give you 
      recipient's email, the crux of subject and body, I'll tell you the story or the main reason I have to write this. You need to understand 
      it and write a formal and polite, well-polished email with unmistakable reasons to convince the recipient of the need of the action and 
      which asks the recipient to do the work for me very politely. "Do not ask any reasons from me, come up with your own unmistakable 
      two to three strong reasons and ideas to convince the recipient of the need of the action".

      -------------------------------------------------------------------------------------------------------------

      Okay, so I want you to write an email, where all the spaces and end lines must be replaced by "%20" and "%0A" respectively, in plain text 
      for me based on above details and format here are the details:
      Sender: Abdul Muhaimin
      Recipient: {recipientName}
      Recipient's Email: {recipientEmail}
      Body or main Reason to write: {body}

      Just give me the best possible {part} for this""")

      return response.text

def getEmail(name, email, reason):
  subject = getEmailPart("subject", name, email, reason)
  body = getEmailPart("body", name, email, reason)
  urlEncodedMail = f"https://mail.google.com/mail/?view=cm&fs=1&to={email}&su={subject}&body={body}"
  return urlEncodedMail
