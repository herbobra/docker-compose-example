FROM python:3.8.0
WORKDIR /test_api
COPY . /test_api/
RUN pip install -r requirements.txt
EXPOSE 5050
CMD python ./first_api.py