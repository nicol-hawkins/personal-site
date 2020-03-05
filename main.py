def main():
    for page in pages:
        file_name = page["filename"]
        output = page["output"]
        title = page["title"]

        content = open(file_name).read()
        template = page_builder(content, title)
        
        open(page["output"], "w+").write(template)
       


#construct webpage using templating for content and titles.   
def page_builder(content, title):
    template = open("templates/base.html").read()
    template_plus_content = template.replace("{{content}}", content)
    full_page = template_plus_content.replace("{{title}}", title)
    return full_page


pages = [
{
    "filename": "content/about.html",
    "output": "docs/about.html",
    "title": "About Me",
},
    {
    "filename": "content/resume.html",
    "output": "docs/resume.html",
    "title": "Resume",
},
    {
    "filename": "content/projects.html",
    "output": "docs/projects.html",
    "title": "Projects",
},
]
   
if __name__ == "__main__":
    main()