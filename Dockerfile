FROM python:3.9-alpine
RUN mkdir /vernacular_assignment
WORKDIR /vernacular_assignment
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD validationapi /vernacular_assignment
CMD django-admin runserver --pythonpath=. --settings=settings 0.0.0.0:8000