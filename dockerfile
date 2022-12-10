FROM python:3.10
WORKDIR /m-a-i-a
COPY requirements.txt /m-a-i-a/
RUN pip install -r requirements.txt
COPY . /m-a-i-a
CMD python main.py