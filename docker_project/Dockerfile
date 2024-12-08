FROM python:3.10-slim-bullseye

# Install Java
RUN apt-get update && \
    apt-get install -y openjdk-11-jre && \
    apt-get clean

# Set JAVA_HOME
ENV JAVA_HOME=/usr
ENV PATH="$JAVA_HOME/bin:$PATH"

# Install Allure
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://github.com/allure-framework/allure2/releases/download/2.22.0/allure-2.22.0.tgz -o allure.tgz && \
    tar -xzf allure.tgz && \
    mv allure-2.22.0 /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure && \
    apt-get clean

# Install system dependencies
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    apt-get clean

# Set working directory
WORKDIR /app

# Set Python path
ENV PYTHONPATH=/app

# Copy application files
COPY app/ /app/
COPY tests/ /app/tests/
COPY requirements.txt /app/requirements.txt

# Upgrade pip and install Python dependencies
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose application port
EXPOSE 5001

# Default command
CMD ["python", "app.py"]