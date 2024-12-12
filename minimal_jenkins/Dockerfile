FROM python:3.9-slim

WORKDIR /app
COPY minimal_jenkins/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY minimal_jenkins/ .

CMD ["pytest", "--alluredir=allure-results", "tests"]