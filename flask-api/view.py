#views.py
from flask import request, jsonify
from app import app, db
from app.models import Vacancy, Candidate
from app.utils import parse_vacancies, parse_candidates

@app.route('/vacancies', methods=['GET'])
def get_vacancies():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Вызов функции парсинга вакансий и сохранение в базу данных
    parse_vacancies(query)

    # Получение списка вакансий из базы данных с пагинацией
    vacancies = Vacancy.query.order_by(Vacancy.created_at.desc()).paginate(page, per_page, False)
    return jsonify({
        'items': [v.as_dict() for v in vacancies.items],
        'total': vacancies.total,
        'page': vacancies.page,
        'pages': vacancies.pages
    })

@app.route('/candidates', methods=['GET'])
def get_candidates():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Вызов функции парсинга кандидатов и сохранение в базу данных
    parse_candidates(query)

    # Получение списка кандидатов из базы данных с пагинацией
    candidates = Candidate.query.order_by(Candidate.created_at.desc()).paginate(page, per_page, False)
    return jsonify({
        'items': [c.as_dict() for c in candidates.items],
        'total': candidates.total,
        'page': candidates.page,
        'pages': candidates.pages
    })

@app.route('/analytics', methods=['GET'])
def get_analytics():
    # Получение количества вакансий и кандидатов из базы данных
    vacancies_count = Vacancy.query.count()
    candidates_count = Candidate.query.count()
    return jsonify({
        'vacancies_count': vacancies_count,
        'candidates_count': candidates_count,
        'candidates_per_vacancy': candidates_count / vacancies_count if vacancies_count else 0
    })
