import anvil.secrets
import anvil.server
import google.generativeai as genai

GOOGLE_API_KEY = anvil.secrets.get_secret("GEMINI_API")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name='gemini-1.5-flash')

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def generateDataSummary(prompt, data):
  revised_prompt = f'''
  {prompt} + "\n\n" + {data}
  '''
  response = model.generate_content(revised_prompt)
  return response.text
  

