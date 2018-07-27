#!/bin/bash

docker-compose up -d

sleep 3

docker-compose exec nodeosd nodeos --version

docker-compose logs -f

