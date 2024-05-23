FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY Makefile .

RUN apt-get update && apt-get install -y make \
     && apt-get clean \
     && rm -rf /var/lib/apt/lists/*

RUN make install

COPY src/ src/
COPY main.py .

ENTRYPOINT ["python"]
CMD ["main.py", "--help"]