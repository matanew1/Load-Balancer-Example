FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# Install python-dotenv
RUN pip install python-dotenv

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
