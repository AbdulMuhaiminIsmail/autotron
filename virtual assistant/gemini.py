import os
import google.generativeai as genai
from speech import SpeechSystem
from helper import ownerName, assistantName

class Gemini:
    def __init__(self):
        self.ss = SpeechSystem()
        self.genai = genai
        self.genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        self.model = self.initialize_gen_model()

    def initialize_gen_model(self):
        generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 100,
        "max_output_tokens": 800,
        "response_mime_type": "text/plain",
        }

        self.model = genai.GenerativeModel(
          model_name="gemini-1.5-pro",
          generation_config=generation_config,
        )

        return self.model

    def command_to_prompt(self, command):
        chat_session = self.model.start_chat()
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

    def get_email_part(self, part, recipientName, recipientEmail, body):
          chat_session = self.model.start_chat()
          response = chat_session.send_message(f"""
                                              
          Hey, you are an expert in writing professional and quality emails. I want my emails written by you and
          I firmly believes that you can write the best email for me. You are required to understand 
          the details and return only the part (subject or body) of the email only which is requested.
          If subject has been asked then don't add sender's name or the word "Subject" in it. "Just write 
          the subject with lowcased prepositions and articles and uppercase action words or nouns." 
                                              
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

    def get_email(self):
        self.ss.speak("Please enter the name of the recipient:")
        name = self.ss.listen()
        self.ss.speak("Please tell me the email of the recipient:")
        email = self.ss.listen()
        self.ss.speak("Why do you need to write this email?")
        reason = self.ss.listen()
        subject = self.get_email_part("subject", name, email, reason)
        body = self.get_email_part("body", name, email, reason)
        urlEncodedMail = f"https://mail.google.com/mail/?view=cm&fs=1&to={email}&su={subject}&body={body}"
        return urlEncodedMail

    def fetch_explanation(self, topic):
        self.initialize_gen_model()
        chat_session = self.model.start_chat()
        response = chat_session.send_message(f"""
        Hey, From now onwards, you are not GEMINI or CHATGPT or any LLM, DO NOT RESPOND TO GEMINI, JUST GIVE RESPONSES BASED ON THE ASK QUESTION you are my assistant, assistant of {ownerName} and your name is {assistantName}. You are also the best teacher in the world, capable of explaining and asking anything to anyone tailored to their learning style. If given a command like "Explain quarks to me in simple wording," you will provide the simplest possible explanation of quarks. You always start with a perfect and suitable analogy and using it explain the real concept.
        Additionally, you can tailor your explanations to the user's age group. For example, if the user says "Explain this to me as if I am x years old," you adapt your explanation to their age level. After explaining, ask the user first if he gets it!

        Now, here is a user command, respond according to the instructions given to you: {topic}         
                                            """)
        return response.text

    def get_explanation(self, command):
      try:
        response = self.fetch_explanation(command)
        print(response)
        self.ss.speak(response)
      except Exception as e:
        print(f"An Unknown Issue occured: {e}")
        self.ss.speak("An unknown issue occured!")

