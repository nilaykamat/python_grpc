global articles
articles = [
    {
        'user_id' : 1,
        'article' : 'hello world'
    },
    {
        'user_id' : 2,
        'article' : 'hgellow user 2'
    }
]

def get_article(user_id):
    for i in articles :
        if i['user_id'] == user_id :
            return i['article']