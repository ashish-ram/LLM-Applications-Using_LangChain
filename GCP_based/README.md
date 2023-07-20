# Setting up GCP
    
    - Enable Vertext AI API on Google Cloud Console

    - Service account: 
    Create a service account with a "Vertex AI User" role. This will  ensure you don't provide excess permission to this account


- Online help: https://www.youtube.com/watch?v=Zi-W2pPVmzU

# local conda env for bacis packages and python sdk for gcp

```
conda create -n gcp python=3
pip install google-cloud-aiplatform
```
# env variables: GCP service account
## WSL/Linux
export GOOGLE_APPLICATION_CREDENTIALS="path_to_service_account_file.json"

**major problem**: The time in the wsl is out of sync and eve tho you have set the env var correctly, this will lead to unautorized token or expired token. 
To fix this problem, run the following command 

    sudo hwclock -s

Also you can verify if the json service account key is set properly by running the following

    gcloud auth print-access-token






