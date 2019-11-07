from abc import ABC

import requests
from social_core.backends.oauth import BaseOAuth2


def get_role(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    accessToken = auth0user.extra_data['access_token']
    url = "http://isis2503-miguelmunoz2019.auth0.com"
    headers = {'authorization': 'Bearer ' + accessToken}
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()
    role = userinfo['http://isis2503-miguelmunoz2019.auth0.com']
    return (role)

