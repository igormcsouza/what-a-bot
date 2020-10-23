import wikipediaapi


wiki_wiki = wikipediaapi.Wikipedia('en')

def query_by_subject(subject: str) -> str:
    page = wiki_wiki.page(subject)

    assert page.exists() == True

    print(page.summary)

    return page.summary