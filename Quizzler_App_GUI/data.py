import requests

def get_questions():
    try:
        r = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
        response = r.json()
    except requests.exceptions.RequestException as e:
        print(f'Error fetching the questions: {e}')
    return response["results"]

question_data = get_questions()
