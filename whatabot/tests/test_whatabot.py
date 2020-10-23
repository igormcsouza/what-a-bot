from whatabot import __version__
from whatabot.search import wikipedia


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
