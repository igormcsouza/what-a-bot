import wikipediaapi


wiki_wiki = wikipediaapi.Wikipedia('en')

def query_by_subject(subject: str) -> str:
    page = wiki_wiki.page(subject)

    if page.exists() != True:
        return f'Not sure what is {subject}'

    return page.summary