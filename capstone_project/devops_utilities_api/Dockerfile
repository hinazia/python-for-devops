## Take Pateela
FROM python:3.14

## ADD ingredients
WORKDIR /app

COPY . /app

## Mix / process the items
RUN pip install -r requirements.txt

EXPOSE 8000

## Gas on
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]