#!/bin/bash
cd ~/Twitterbot-real-2
docker run -w /usr/workspace -v $(pwd):/usr/workspace twitterbot-python:1 python statistics_poster.py
