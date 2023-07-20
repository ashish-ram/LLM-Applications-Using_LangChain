import vertexai
from vertexai.language_models import TextGenerationModel

# from google.oauth2 import service_account

# credentials = service_account.Credentials.from_service_account_file(
#     'one-ai-a826dd60ad96.json')
# vertexai.init(project="one-ai", location="us-central1", credentials=credentials)

vertexai.init(project="one-ai", location="us-central1")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison@001")
response = model.predict(
    """What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?""",
    **parameters
)
print(f"Response from Model: {response.text}")