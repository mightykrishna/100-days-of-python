facebook_posts=[{'likes':21,'comments':2},{'likes':33,'comments':2},{'likes':4,'comments':8}]
total_likes=0
for post in facebook_posts:
    try:
        total_likes=total_likes+post['likes']
    except KeyError:
        total_likes=0

print(total_likes)