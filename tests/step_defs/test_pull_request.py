from pytest_bdd import given, when, then, parsers
from pytest_bdd import scenarios
import requests

GUTHUB_API = 'https://api.github.com'

# Below 2 auth are not valid anymore and to be updated as per current user
USER = 'andrey-dmitriev'
TOKEN = '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'

HEADERS = {'Authorization': 'token ' + TOKEN}

scenarios('../features/pull_request.feature')

@given("user logs in to GitHub using basic authentication")
def github_response():
    
    # Basic Auth via name and password is deprecated by Github
    # See 
    # https://developer.github.com/changes/2020-02-14-deprecating-password-auth/
    # https://docs.github.com/en/rest/overview/other-authentication-methods#via-username-and-password
    # So isntead of
    # response = requests.get(GUTHUB_API + '/user', auth=HTTPBasicAuth('user', 'password'))
    # we will use token auth.

    response = requests.get(GUTHUB_API + '/user', headers=HEADERS)
    assert response.status_code == 200
    print('user logs in to GitHub using basic authentication and response is ' + str(response.status_code))

@when(parsers.parse('user creates repository with name "{repo}"'))
def github_create_repo(repo):

    body = {'name': repo, 'auto_init': True}
    print('user creates repository with name ' + repo)
    response = requests.post(GUTHUB_API + '/user/repos', headers=HEADERS, json = body)
    print(' and response is ' + str(response.status_code) + '\n' + str(response.content))

@when(parsers.parse('user creates branch "{branch}"'))
def github_create_branch(branch):
    print('user creates branch ' + branch)

@when(parsers.parse('user commits auto generated file to branch "{branch}"'))
def github_commit_branch(branch):
    print('user commits auto generated file to branch ' + branch)

@then('user creates pull request to main branch')
def github_create_pull_request():
    assert 1 == 1
    print('user creates pull request to main branch')