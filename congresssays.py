#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib2
import urllib
from datetime import date, timedelta
import json
import tweepy

class MakeTweet(webapp2.RequestHandler):
    def get(self):
        day = date.today() - timedelta(1)
        endpoint = 'http://capitolwords.org/api/phrases.json' 
        query_params = {'apikey': 'eea337bef84a4129ba8639825c1b39ac', 'entity_type': 'date', 'entity_value': day, 'n': 1}
        formatted_args = urllib.urlencode(query_params)
        page = urllib2.urlopen(url = endpoint + "?" + formatted_args)
        words = json.loads(page.read())
        msg = 'The top words from Congress yesterday were '
        for i in words[0:3]:
            msg = msg + '"' + i['ngram']  + '", '
        msg = msg + 'and "' + words[3]['ngram'] + '."'
        CONSUMER_KEY = "---"
        CONSUMER_SECRET = "---"
        ACCESS_TOKEN_KEY = "---"
        ACCESS_TOKEN_SECRET = "---"
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        result = api.update_status(msg)

app = webapp2.WSGIApplication([
    ('/congresssays', MakeTweet)
], debug=True)

def main():
    app.run()
