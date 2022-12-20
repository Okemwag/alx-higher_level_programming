#!/bin/bash

response=$(curl -X GET "http://0.0.0.0:5000/catch_me")

echo $response


response=$(curl -X GET "http://0.0.0.0:5000/catch_me")

if [[ $response == *"You got me!"* ]]; then
  echo "The server responded with the expected message!"
else
  echo "The server did not respond with the expected message."
fi
