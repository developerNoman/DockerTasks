FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    python3 \
    libboost-all-dev \
    git
WORKDIR /app
COPY . /app
CMD ["bash"]