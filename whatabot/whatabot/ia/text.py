from gensim import summarization


def summarize(text: str) -> str:
    return summarization.summarize(text, word_count=50)