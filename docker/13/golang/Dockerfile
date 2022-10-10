# syntax=docker/dockerfile:1
FROM golang:1.17 as builder
WORKDIR /opt/app
COPY . .
RUN go build -o example


FROM ubuntu:latest
WORKDIR /opt/app
COPY --from=builder /opt/app/example /opt/app/example
EXPOSE 8080
CMD ["/opt/app/example"]