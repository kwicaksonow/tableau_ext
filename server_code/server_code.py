# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# import anvil.secrets
# import anvil.server
# import google.generativeai as genai

# GOOGLE_API_KEY = anvil.secrets.get_secret("GEMINI_API")
# genai.configure(api_key=GOOGLE_API_KEY)
# model = genai.GenerativeModel(model_name='gemini-2.0-flash', system_instruction=[
#         "You are an expert analyst and know everything about data analysis",
#         # "You can interpret data in any form whether it's a single data point or a list of data with keys"
#         "You are on a mission to provide the best data analysis report when asked",
#         "You are capable of answering the question without report as well on topics that require you to answer between a finite set of possibilities",
#         "You always respond or answer in Bahasa Indonesia despite any language that has been used to ask you",
#     ],)

# @anvil.server.callable
# def generateDataSummary(prompt, data):
#   revised_prompt = f'''
#   {prompt} + "\n\n" + {data}
#   '''
#   response = model.generate_content(revised_prompt)
#   return response.text
  

# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# import anvil.secrets
# import anvil.server
# import openai

# # Retrieve your OpenAI API key from Anvil's secrets
# OPENAI_API_KEY = anvil.secrets.get_secret("OPENAI_API_KEY")
# openai.api_key = OPENAI_API_KEY

# @anvil.server.callable
# def generateDataSummary(prompt, data):
#     # Construct the system message to guide the model's behavior
#     system_message = {
#         "role": "system",
#         "content": (
#             "You are an expert analyst and know everything about data analysis. "
#             "You are on a mission to provide the best data analysis report when asked. "
#             "You are capable of answering the question without a report as well on topics that require you to answer between a finite set of possibilities. "
#             "You always respond or answer in Bahasa Indonesia despite any language that has been used to ask you."
#         )
#     }

#     # Construct the user message with the prompt and data
#     user_message = {
#         "role": "user",
#         "content": f"{prompt}\n\n{data}"
#     }

#     # Call OpenAI's ChatCompletion API
#     response = openai.ChatCompletion.create(
#         model="gpt-4",  # You can use "gpt-3.5-turbo" if you prefer
#         messages=[system_message, user_message]
#     )

#     # Extract and return the assistant's reply
#     return response['choices'][0]['message']['content']