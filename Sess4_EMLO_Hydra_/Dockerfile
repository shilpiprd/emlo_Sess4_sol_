FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt \
	&& rm -rf /root/.cache/

COPY . .

EXPOSE 7860 

ENTRYPOINT ["python3", "demo_scripted.py"]


