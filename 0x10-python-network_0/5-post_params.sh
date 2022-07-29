#!/bin/bash
# This script posts parameters to the server
curl -s -X POST -F "email=test@gmail.com" -F "subject=I will always be here for PLD" $1
