FROM python:latest
RUN pip install psutil argparse
WORKDIR /usr/local/bin
COPY metrics.py .
