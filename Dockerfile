FROM python:3 
ENV PYTHONUNBUFFERED=1
WORKDIR /use/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .