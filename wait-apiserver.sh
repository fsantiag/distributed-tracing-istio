#!/bin/bash

set -e

until curl localhost:8080; do
  >&2 echo "ApiServer is not available"
  sleep 1
done

>&2 echo "ApiServer is up!"
