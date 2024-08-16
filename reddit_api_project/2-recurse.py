#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
            headers = {"User-Agent": "custom-user-agent"}
                params = {"after": after, "limit": 100}
                    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
                        
                            if response.status_code != 200:
                                        return None
                                        
                                        data = response.json().get('data', {})
                                            children = data.get('children', [])
                                                
                                                    if not children:
                                                                return hot_list
                                                                
                                                                for post in children:
                                                                            hot_list.append(post.get('data', {}).get('title'))
                                                                                
                                                                                    after = data.get('after')
                                                                                        
                                                                                            if after is None:
                                                                                                        return hot_list
                                                                                                        
                                                                                                        return recurse(subreddit, hot_list, after)
