FROM python:3.10-alpine

ENV FLASK_APP hello.py
ENV FLASK_CONFIG production

# set working directory to app
WORKDIR /app

# install dependencies
COPY requirements.txt ./
RUN python -m venv venv
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

# copy relevant files into docker directory
COPY hello.py boot.sh ./
COPY templates templates

EXPOSE 5000

ENTRYPOINT ["venv/bin/flask"]
CMD ["run", "--host", "0.0.0.0"]