
class Candidate:
    """Candidate entity"""

    def __init__(self, candidate_id: int, name: str, avatar: str, position: str, gender: str, age: str, skills: str):
        self.candidate_id = candidate_id
        self.name = name
        self.avatar = avatar
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills

        print(f"Initialization of instance '{self.candidate_id}' complete")

    def __repr__(self):
        return f"ID: {self.candidate_id}\nName: {self.name}\nAvatar: {self.avatar}\nPosition: {self.position}\n" \
               f"Gender: {self.gender}\nAge: {self.age}\nSkills: {self.skills}\n"
