from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

def summarize(text, sentence_count = 2):

    if not text:
        return ""

    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()

    summary_sentences = summarizer(parser.document, sentence_count)
    summary = " ".join(str(sentence) for sentence in summary_sentences)

    return summary





'''
import re

def summarize(text, max_sentences = 3):

    if not text:
        return ""

    sentences = re.split(r'(?<=[.!?]) +', text)
    summary = " ".join(sentences[:max_sentences])

    return summary
''' 