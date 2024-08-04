FROM python:3.10
WORKDIR app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

# CMD ["uvicorn", "main:app"]

# to run with host 0.0.0.0 to can be accessed from outside
CMD ["fastapi", "run", "main.py"]