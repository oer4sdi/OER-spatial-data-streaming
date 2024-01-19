## Set Python Environment To 3.9
FROM python:3.9.5

## Set Working Directory
WORKDIR /home

## Install required packages for OER
ADD ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Clean up build scripts
RUN rm -f ./requirements.txt

ENTRYPOINT [ "jupyter","notebook","--allow-root","--ip=0.0.0.0"]