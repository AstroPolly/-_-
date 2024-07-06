#utils.py
import requests
from datetime import datetime
from app import db
from app.models import Vacancy, Candidate

def parse_vacancies(query):

    url = f'https://api.hh.ru/vacancies?text={query}'
    response = requests.get(url)
    data = response.json()

    for item in data['items']:
        vacancy = Vacancy(
            title=item['name'],
            description=item['description'],
            salary_from=item['salary']['from'],
            salary_to=item['salary']['to'],
            employment_format=item['employment']['name'],
            created_at=datetime.strptime(item['created_at'], '%Y-%m-%dT%H:%M:%S%z')
        )
        db.session.add(vacancy)
    db.session.commit()

def parse_candidates(query):
    url = f'https://api.hh.ru/resumes?text={query}'
    response = requests.get(url)
    data = response.json()

    for item in data['items']:
        candidate = Candidate(
            full_name=item['full_name'],
            position=item['title'],
            skills=', '.join(item['skills']),
            employment_format=item['employment']['description'],
            created_at=datetime.strptime(item['created_at'], '%Y-%m-%dT%H:%M:%S%z')
        )
        db.session.add(candidate)
    db.session.commit()
