import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_GENERATIVE_API_KEY"])