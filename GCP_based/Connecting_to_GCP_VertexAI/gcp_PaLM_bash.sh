API_ENDPOINT="us-central1-aiplatform.googleapis.com"
PROJECT_ID="one-ai"
MODEL_ID="text-bison@001"

curl \
-X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/us-central1/publishers/google/models/${MODEL_ID}:predict" -d \
$'{
    "instances": [
        {
            "content": "what are the best places to visit in india?"
        }
    ],
    "parameters": {
        "temperature": 0.2,
        "maxOutputTokens": 256,
        "topP": 0.8,
        "topK": 40
    }
}'