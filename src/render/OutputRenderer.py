class OutputRenderer:
    def __init__(self):
        pass

    def render(self, template: str, destination: str):
        template = Template('Hello {{ name }}!')
        template.render(name='John Doe')
