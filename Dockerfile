FROM ubuntu:24.04
RUN apt update && apt install -y python3
COPY . .
CMD ["python3", "--version"]
