#!/usr/bin/python3
import requests

def top_ten(subreddit):
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
            headers = {"User-Agent": "custom-user-agent"}
                params = {"limit": 10}
                    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
                        
                            if response.status_code != 200:
                                        print("None")
                                                return
                                                
                                                data = response.json().get('data', {}).get('children', [])
                                                    
                                                        for post in data:
                                                                    print(post.get('data', {}).get('title'))
