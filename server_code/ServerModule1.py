import anvil.secrets
import anvil.server
import google.generativeai as genai

GOOGLE_API_KEY = anvil.secrets.get_secret("GEMINI_API")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name='gemini-1.5-flash', system_instruction=[
        "You are an expert analyst and knows everything about data analysis",
        "You can interpret data in any form whether it's single data point or a list of data with keys"
        "You are on a mission to provide the best data analysis report when asked",
    ],)

@anvil.server.callable
def generateDataSummary(prompt, data):
  revised_prompt = f'''
  {prompt} + "\n\n" + {data}
  '''
  response = model.generate_content(revised_prompt)
  return response.text
  

