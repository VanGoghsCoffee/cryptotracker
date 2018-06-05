FROM python:3.6

WORKDIR /usr/src/app

COPY app.py ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]
