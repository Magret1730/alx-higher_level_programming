#!/bin/bash
# Use curl to send a request to the specified URL with a header causing the desired response
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
