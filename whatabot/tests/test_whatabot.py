from whatabot import __version__
from whatabot.search import wikipedia
from whatabot.ia.text import summarize


def test_version():
    assert __version__ == '0.1.0'

def test_subject_query():
    query_result = wikipedia.query_by_subject('dog')

    assert query_result != None, 'Nothing has returned as result'
    assert type(query_result) == str, 'The returning is not a String'
    assert 'dog' in query_result, 'The subject may be not related to the query'

def test_subject_query_fails():
    query_result = wikipedia.query_by_subject('averyridiculousstring')

    assert query_result != None, 'Nothing has returned as result'
    assert type(query_result) == str, 'The returning is not a String'
    assert 'averyridiculousstring' in query_result, 'The subject may be not \
        related to the query'
    assert 'Not sure what is' in query_result, 'It did not returned what was \
        expected'

def test_summarize_text():
    text = "The dog (Canis familiaris when considered a distinct species or \
        Canis lupus familiaris when considered a subspecies of the wolf) is a \
        domesticated carnivore of the family Canidae. It is part of the \
        wolf-like canids, and is the most widely abundant terrestrial \
        carnivore. The dog and the extant gray wolf are sister taxa as modern \
        wolves are not closely related to the wolves that were first \
        domesticated, which implies that the direct ancestor of the dog is \
        extinct. The dog was the first species to be domesticated, and has \
        been selectively bred over millennia for various behaviors, sensory \
        capabilities, and physical attributes."

    summarized_text = summarize(' '.join(text.split()))

    assert type(summarized_text) == str
    assert len(summarized_text.split()) < len(text.split()), 'The result is not a summary.'
