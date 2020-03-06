from jinja2 import Template
import os
import glob
import re


pages = []


def create_pages_list():
    content_files = glob.glob('content/*.html')

    for file_path in content_files:
        file_name = os.path.basename(file_path)
        name_only, exension = os.path.splitext(file_name)
        title_only = name_only.title()
        output_file = os.path.join('docs', file_name)

        pages.append({
            "file_path": file_path,
            "title": title_only,
            "output": output_file,
            "file_name": file_name
        })

        


def main():
    create_pages_list()
    template_contents = open('templates/base.html', 'r').read()
    apply_template = Template(template_contents)

    for page in pages:
        content = open(page['file_path'], 'r').read()
        results = apply_template.render (
                            title = page['title'],
                            content = content,
                            pages = pages,
                        )
        open(page["output"], 'w+').write(results)
    return results


def new_content():
    new_page_title = input('What would you like to name new file? ')
    cleansed_file_name = re.sub(r'\W', '_', new_page_title)
    content_template = """<div class="new-container">
                            <div class="row">
                            </div>
                          </div>"""
    new_template = f'content/{cleansed_file_name}.html'
    open(new_template, 'w+').write(content_template)
    return 
    
    