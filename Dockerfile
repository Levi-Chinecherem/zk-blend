FROM rust:1.88
WORKDIR /usr/src/zk-blend
RUN apt-get update && apt-get install -y libgmp-dev libpari-dev
COPY . .
RUN cargo build
CMD ["cargo", "run"]