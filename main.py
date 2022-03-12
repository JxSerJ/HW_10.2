from flask import Flask

from utils import load_data, build_candidate_instances, build_root_page_data, build_skills_page_data, \
    build_skill_id_page_data
from config import DATA_FILE_PATH

data = load_data(DATA_FILE_PATH)
candidate_list, skill_list = build_candidate_instances(data)

application = Flask(__name__)


@application.route("/")
def page_index():
    return "<H1>Главная страница</H1><br>" \
           "<H2>Список кандидатов</H2><br>" \
           f"{build_root_page_data(candidate_list)}<br>" \
           f"<br><a href='../skill/'>Перейти на страницу навыков</a>"


@application.route("/candidate/<candidate_id>")
def page_candidate(candidate_id):

    candidate_id = int(candidate_id) - 1

    string = f'''
<img src="{candidate_list[candidate_id].avatar}">
<pre>
  Имя кандидата - <b>{candidate_list[candidate_id].name}</b>
  Позиция кандидата - <b>{candidate_list[candidate_id].position}</b>
  Навыки: <b>{', '.join(candidate_list[candidate_id].skills)}</b><br>
  Пол: <b>{candidate_list[candidate_id].gender}</b>
  Возраст: <b>{candidate_list[candidate_id].age}</b>

<br><a href='../'>Перейти на главную</a>
</pre>
'''
    return string


@application.route("/skill/")
def page_skill():
    return "<H1>Список навыков</H1><br>" \
           "<H2>Выберете навык</H2><br>" \
           f"{build_skills_page_data(skill_list)}" \
           f"<br><a href='../'>Перейти на главную</a>"


@application.route("/skill/<skill_id>")
def page_skill_id(skill_id):

    string = f'''<H1>Список кандидатов с навыком "{skill_id.capitalize()}"</H1><br>
    <pre>{build_skill_id_page_data(candidate_list, skill_id)}
    <br><a href='../'>Перейти на главную</a>
    <br><a href='../skill/'>Перейти на страницу навыков</a>
    </pre>
    '''
    return string


application.run(debug=True)
