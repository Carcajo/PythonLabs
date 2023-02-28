FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBITECODE 1

RUN apt-get update

WORKDIR /app

RUN pip3 install --upgrade pip
# RUN pip3 install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY . .

RUN pip install -r requirements.txt
#
# COPY Pipfile Pipfile.lock ./
# RUN pipenv install --system --deploy



#CMD ["python3", "TASK2.py"]
CMD ["python3", "TASK3.py"]