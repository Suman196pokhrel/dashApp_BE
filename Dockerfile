FROM python:3.9.17-slim-bookworm

WORKDIR /dashapp

COPY requirements.txt /dashapp/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /dashapp/


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]