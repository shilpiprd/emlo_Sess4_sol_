FROM python:3.9-slim

WORKDIR /app/src

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt \
	&& rm -rf /root/.cache/
# COPY src/demo_scripted.py ./demo_scripted.py

COPY . .

EXPOSE 8080 

ENTRYPOINT ["python3", "demo_scripted.py"]


