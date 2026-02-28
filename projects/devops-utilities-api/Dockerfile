# Take patila

FROM python:3.14

#ADD ingrediants

WORKDIR /app

COPY . .

# mix / process the item

RUN pip install -r requirements.txt

EXPOSE 8000

# Gas on


CMD ["python","main.py"]
