"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

def ask_genie(question):
  
	genai.configure(api_key="AIzaSyC6RHJeUG9cifYM9MZJp6h3EOCEbyrufqc")

	#Set up the model
	generation_config = {
  	"temperature": 1,
  	"top_p": 0.95,
  	"top_k": 0,
  	"max_output_tokens": 8192,
	}

	safety_settings = [
  	{
    	"category": "HARM_CATEGORY_HARASSMENT",
    	"threshold": "BLOCK_MEDIUM_AND_ABOVE"
  	},
  	{
    	"category": "HARM_CATEGORY_HATE_SPEECH",
    	"threshold": "BLOCK_MEDIUM_AND_ABOVE"
  	},
  	{
    	"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    	"threshold": "BLOCK_MEDIUM_AND_ABOVE"
  	},
  	{
    	"category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    	"threshold": "BLOCK_MEDIUM_AND_ABOVE"
  	},
	]

	model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

	convo = model.start_chat(history=[
	])

	convo.send_message(question)
	print(convo.last.text)

question = input("Ask the genie: ")
answer = ask_genie("only answer about bash question else write sorry i can't answer this questions"+question)
    
