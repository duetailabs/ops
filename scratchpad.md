# docs link
https://cloud.google.com/gemini/docs/codeassist/code-customization#create_an_index

# Define project id
export PROJECT_ID=code-customization-go

# Check indexes in the project
gcloud gemini code-repository-indexes list --location=us-central1 --project=$PROJECT_ID

# Describe index (same output as above)
gcloud gemini code-repository-indexes describe assist --location=us-central1 --project=$PROJECT_ID

# Connect to Github docs
https://cloud.google.com/developer-connect/docs/connect-github-repo

# Give SA secretmanager admin role
export SERVICE_ACCOUNT_EMAIL=service-668476910205@gcp-sa-devconnect.iam.gserviceaccount.com
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
  --role="roles/secretmanager.admin"


# Create a connection (role: Owner)
gcloud beta developer-connect connections create shipping \
    --location=us-central1 \
    --github-config-app=DEVELOPER-CONNECT \
    --project=$PROJECT_ID

# Click on the Github link and authorize the Github Organization via web oauth flow

# Describe connection (should say COMPLETE)
gcloud beta developer-connect connections describe shipping \
    --location=us-central1 \
    --project=$PROJECT_ID

# Add repo to the index (dont forget .git at the end of the REPO URI)
gcloud beta developer-connect connections git-repository-links create shipping \
    --clone-uri=https://github.com/duetailabs/shipping.git \
    --connection=shipping \
    --location=us-central1 \
    --project=$PROJECT_ID

# Optional
# See repo groups
gcloud gemini code-repository-indexes repository-groups list --location=us-central1 --project=$PROJECT_ID --code-repository-index=assist


# Optional
# Create a new repo group and add repo
gcloud gemini code-repository-indexes repository-groups create shipping \
    --project=code-customization-go \
    --location=us-central1 \
    --code-repository-index=assist \
    --repositories='[{"resource": "projects/code-customization-go/locations/us-central1/connections/shipping/gitRepositoryLinks/shipping", "branchPattern": "main"}]'


# Update index
gcloud gemini code-repository-indexes update assist \
    --location=us-central1 \
    --project=$PROJECT_ID \
    --update-mask=git_config.refresh_interval,git_config.repository_groups 