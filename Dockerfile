FROM python:3

RUN pip install requests

ADD main.py .

ENTRYPOINT ["python", "/main.py"]