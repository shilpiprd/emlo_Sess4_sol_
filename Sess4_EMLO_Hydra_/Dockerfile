FROM python:3.9-slim

WORKDIR /usr/src

COPY requirements.txt requirements.txt

# RUN pip3 install -r requirements.txt 
	# && rm -rf /root/.cache/
# COPY src/demo_scripted.py ./demo_scripted.py
RUN pip3 install -r requirements.txt && rm -rf /root/.cache/

COPY . .

EXPOSE 8080 

ENTRYPOINT ["python3", "src/demo_scripted.py"]


