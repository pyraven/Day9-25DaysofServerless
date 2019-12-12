from google.cloud import storage
import json, random, requests, os

def post_comment(user, url):
    token = os.environ['TOKEN']
    headers = {"Authorization": f"token {token}"}
    message = f"Thanks for the issue @{user}. Happy Holidays and Merry Christmas you filthy animal."
    data = json.dumps({"body": message})
    complete_url = url + "/comments"
    response = requests.post(complete_url, headers=headers, data=data)
    print(response)

def main(request):
    request_json = request.get_json()
    try:
        if request_json['action'] == "opened":
            user = request_json['issue']['user']['login']
            issue = request_json['issue']['url']
            repo_owner = request_json['issue']['url'].split('/')[4]
            post_comment(user, issue)
        else:
            pass
    except Exception as e:
        print(e)
        