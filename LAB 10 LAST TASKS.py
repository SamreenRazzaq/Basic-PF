#%%

blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
{'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5,
'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4,
'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1},
{'Photos': 3, 'Likes': 19, 'Comments': 3}]
total_likes = 0

for post in range(0, len(blog_posts)):
    try:
        total_likes = total_likes +blog_posts[post]['Likes']
    except:
        blog_posts[post]['Likes']=0
        
print('Total Likes:',total_likes)

#%%

food = ["chocolate", "chicken", "corn", "sandwich",
"soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []
for x in food:
    try:
        fifth.append(x[1])
    except IndexError:
        pass
print(fifth)