#!/bin/bash
# 0
 curl --output /dev/null --write-out "%{size_download}\n" --silent "$1"
