#!/bin/bash
# Displaying the methods only
curl -si $1 | grep "Allo" | cut --delimiter=" " -f 2-
