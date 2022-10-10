# syntax=docker/dockerfile:1
FROM --platform=$BUILDPLATFORM golang:1.18 as build

RUN sed -i "s@http://\(deb\|security\).debian.org@https://mirrors.aliyun.com@g" /etc/apt/sources.list && apt-get update && apt-get install -y gcc-aarch64-linux-gnu

ARG TARGETOS TARGETARCH
WORKDIR /opt/app
COPY go.* ./
RUN go mod download

COPY . .

ARG LD_FLAGS='-linkmode external -w -extldflags "-static"'

RUN --mount=type=cache,target=/root/.cache/go-build \
if [ "$TARGETARCH" = "arm64" ]; then CC=aarch64-linux-gnu-gcc && CC_FOR_TARGET=gcc-aarch64-linux-gnu; fi && \
GOOS=$TARGETOS GOARCH=$TARGETARCH CC=$CC CC_FOR_TARGET=$CC_FOR_TARGET go build -ldflags "$LD_FLAGS" -o /opt/app/example .


FROM ubuntu:latest
WORKDIR /opt/app
COPY --from=build /opt/app/example ./example
CMD ["/opt/app/example"]