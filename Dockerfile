FROM python:3.10-slim

WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt

# Add these manually for your project
ENV INSTANCE_CONNECTION_NAME=qwiklabs-gcp-03-d95bf0c32565:us-central1:postgres
ENV DB_USER=evolution
ENV DB_PASS=evolution
ENV DB_NAME=product_details

CMD ["python", "main.py"]
