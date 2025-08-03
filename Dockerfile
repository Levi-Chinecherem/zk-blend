FROM rust:1.88
WORKDIR /usr/src/zk-blend
COPY . .
RUN apt-get update && apt-get install -y libgmp-dev
RUN cargo build
CMD ["cargo", "run"]