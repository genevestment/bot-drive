# bot-drive

Python Bot Drive code.

## Feature

*   Supports RC control and autonomous mode
*   Supports mecanum drivetrain


## Dev Guide

To start developing, start a Docker image by first build the Docker image and start the local dev image

```sh
docker build -f Dockerfile -t py-dev-genevestment .

docker run -itd --rm -v /Users/genevestment/dev/public/bot-drive:/src/github.com/genevestment/bot-drive --name genevestment-py py-dev-genevestment

docker exec -it genevestment-py bash
```

Run the `Makefile` to verify and test the code

```sh
make test-all
```