import json
from classes import Candidate


def load_data(path: str) -> list:
    """
    JSON Data loader

    :param path: data-file path
    :return: data
    """
    with open(path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
        return data


def build_candidate_instances(data: list) -> tuple[list, list]:
    """
    Object instance initializer (class Candidate)

    :param data: list of dictionaries
    :return: list of objects and list of skills
    """
    candidate_list = []
    skill_list = []

    for i in range(len(data)):
        candidate = Candidate(candidate_id=data[i]["id"], name=data[i]["name"], avatar=data[i]["picture"],
                              position=data[i]["position"], gender=data[i]["gender"], age=data[i]["age"],
                              skills=data[i]["skills"].lower().split(", "))
        skill_list.extend(candidate.skills)
        candidate_list.append(candidate)

    skill_list = list(set(skill_list))

    return candidate_list, skill_list


def build_root_page_data(candidates: list) -> str:
    """
    Root page builder with candidates

    :param candidates: list of instances of class Candidate
    :return: string
    """
    string = ""

    for i in candidates:
        candidate_string = f"<b>Имя кандидата</b> - {i.name}<br>" \
                           f"<b>Позиция</b> - {i.position}<br>" \
                           f"<b>Навыки</b> - {', '.join(i.skills)}<br>" \
                           f"<a href='/candidate/{i.candidate_id}'>Перейти на страницу кандидата</a><br><br><br>"
        string += candidate_string

    return string


def build_skills_page_data(skill_list: list) -> str:
    """
    Page with all candidate skills builder

    :param skill_list: list of skills
    :return: string
    """
    string = ""

    for i in skill_list:
        skill_string = f"<a href='/skill/{i}'>{i.capitalize()}</a><br>"
        string += skill_string

    return string


def build_skill_id_page_data(candidate_list: list, skill_id: str) -> str:
    """
    Skill page builder. Generates candidate list who has skill_id

    :param skill_id: skill for resolve
    :param candidate_list: list of Candidate instances
    :return: string
    """
    string = ""

    for i in candidate_list:
        if skill_id in i.skills:
            candidate_string = f"<b>Имя кандидата</b> - {i.name}<br>" \
                               f"<b>Позиция</b> - {i.position}<br>" \
                               f"<b>Навыки</b> - {', '.join(i.skills)}<br>" \
                               f"<a href='/candidate/{i.candidate_id}'>Перейти на страницу кандидата</a><br><br><br>"
            string += candidate_string

    return string
