import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

class CARDS_TEMPLATE(object):
    def __init__(self, path_to_template, template_filename):
        self.path_to_template = path_to_template
        self.template_filename = template_filename
        self.template = self._get_template()
        self.rendered_html = None

    def _get_template(self):
        env = Environment(
                    autoescape=select_autoescape(
                        enabled_extensions=('html'),
                        default_for_string=True,
                    ),
                    loader=FileSystemLoader(self.path_to_template)
                )
        return env.get_template(self.template_filename)

    def render(self, paper_details_iterator):
        self.rendered_html = self.template.render(paper_details=paper_details_iterator)

    def save_html(self, output_dir=None, output_htmlfile=None):
        with open(os.path.join(output_dir, output_htmlfile), "w") as f:
            f.write(self.rendered_html)
