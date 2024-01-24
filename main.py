import os
import PIL
import google.generativeai as genai

api_key = os.getenv("GOOGLE_API_KEY")

vision_model = genai.GenerativeModel("gemini-pro-vision")
image = PIL.Image.open("dog.jpg")
response = vision_model.generate_content(
    ["Explain the image", image],
         generation_config=genai.types.GenerationConfig(
         candidate_count=1,
         stop_sequences=["."],
         max_output_tokens=150,
         top_p=0.6,
         top_k=5,
         temperature=0)
)
print(response.text)

