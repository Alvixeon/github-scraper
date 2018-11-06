import requests,getpass
from lxml import html

def get_repos(session_requests):
    url = 'https://github.com/Alvixeon?tab=repositories'
    result = session_requests.get(
        url, 
        headers = dict(referer = url),
    )
    print (result.status_code)
    tree = html.fromstring(result.text)
    repo_counter = tree.xpath('//*[@id="js-pjax-container"]/div/div[2]/div[2]/nav/a[2]/span')
    finstr = ''.join(repo_counter)
    print (finstr)

def login(login_url,session_requests,_username,_password,_auth_token):
    payload = {
        "login": _username, 
        "password": _password,
        "authenticity_token": _auth_token
        }
    result = session_requests.post(
        login_url, 
        data = payload, 
        headers = dict(referer=login_url)
        )
    url = "https://github.com/Alvixeon/btc-py/community"
    
    result = session_requests.get(
        url, 
        headers = dict(referer = url),
        )

    tree = html.fromstring(result.text)
    test_login = tree.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div/div[2]/div[1]/h2//text()')
    print (test_login)
    
    get_repos(session_requests,)
session_requests = requests.session()
login_url = "https://github.com/session"
result = session_requests.get(login_url)
tree = html.fromstring(result.text)

auth_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]
print ("CSRF Token: " + auth_token)

username = input ("Enter a username:")
password = getpass.getpass ("Enter a password:")

login(login_url,session_requests,username,password,auth_token)