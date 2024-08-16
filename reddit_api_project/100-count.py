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

                                                                                                    def count_words(subreddit, word_list, count_dict={}):
                                                                                                            titles = recurse(subreddit)
                                                                                                                
                                                                                                                    if not titles:
                                                                                                                                return
                                                                                                                                
                                                                                                                                for title in titles:
                                                                                                                                            words = title.lower().split()
                                                                                                                                                    for word in word_list:
                                                                                                                                                                    word_lower = word.lower()
                                                                                                                                                                                count_dict[word_lower] = count_dict.get(word_lower, 0) + words.count(word_lower)
                                                                                                                                                                                    
                                                                                                                                                                                        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
                                                                                                                                                                                            
                                                                                                                                                                                                for word, count in sorted_counts:
                                                                                                                                                                                                            if count > 0:
                                                                                                                                                                                                                            print(f"{word}: {count}")

