import wikipediaapi


wiki_wiki = wikipediaapi.Wikipedia('en')

def query_by_subject(subject: str) -> str:
    page = wiki_wiki.page(subject)

    if page.exists() != True:
        return f'{subject}'

    return page.summary