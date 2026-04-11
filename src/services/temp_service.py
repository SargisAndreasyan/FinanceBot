from repositories.template_repo import TemplateRepository

class TemplateService:

    def __init__(self):
        self.repo = TemplateRepository()

    def create_template(self, name: str):
        name = name.strip()

        if not name:
            raise ValueError("Name cannot be empty")

        return self.repo.create(name=name)

    def get_template(self, template_id: int):
        return self.repo.get_by_id(template_id)

    def list_templates(self):
        return self.repo.get_all()

    def delete_template(self, template_id: int):
        return self.repo.delete(template_id)