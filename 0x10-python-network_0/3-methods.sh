#!/bin/bash
# 3
curl -sX OPTIONS "$1" -i | grep Allow | cut -d " " -f2-
