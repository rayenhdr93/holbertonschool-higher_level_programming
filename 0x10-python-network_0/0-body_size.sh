#!/bin/bash
# 0
curl --output /dev/null -L --write-out "%{size_download}\n" --silent "$1"
