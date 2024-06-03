FROM python:3.11.3
WORKDIR /SalonSync/
COPY requirements.txt req.txt
RUN pip3 install -r req.txt
COPY . .
CMD ["flask", "run", "--host=0.0.0.0"]
