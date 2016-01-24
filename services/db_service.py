from firebase import firebase


firebase = firebase.FirebaseApplication(
    'https://flasquiz.firebaseio.com/', None)



def get_titles():
    result = firebase.get('/questions', None)
    titles = [item['title'] for item in result.values()]
    return titles


def get_question(title):
    result = firebase.get('/questions', None)
    question = [i for i in result.values() if i['title'] == title]
    if question:
        return question[0]
    return None

def post_question(question):
    result = firebase.post('/questions', question)
    return result
