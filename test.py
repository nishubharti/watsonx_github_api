#!/usr/bin/env python3
import requests
import json
import urllib.parse

from flask import Flask, request

app = Flask(__name__)

# Endpoint to create a new task
@app.route('/create_issue', methods=['POST'])
def create_task():
    data = request.get_json()
    
    body = {"title":"action required for the assigned trainig","body": data["description"]}
    token = data["token"]
    git_url = data["git_url"]
    
    headers = {"Authorization" : "token {}".format(token)}

    """
    Step 2:
    Generate your target repository's URL using Github API
    """
    parsed_url = urllib.parse.urlparse(git_url)
    hostname = parsed_url.netloc
    git_repo = git_url.split(hostname + '/')[1]
        
    url = "https://api.github.com/repos/{}/issues".format(git_repo)

    """
    Step 3:
    Post your issue message using requests and json
    """

    x=requests.post(url,data=json.dumps(body),headers=headers)
    if (x.status_code != 201):
        print("error here is:"+x.text+"status code recieved is"+x.status_code)
        return "error during created",400
    
    return "successfully created issue", 201


if __name__ == '__main__':
    app.run(debug=True)
