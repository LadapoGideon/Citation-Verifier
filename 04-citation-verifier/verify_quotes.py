"""Check that quotes in an AI response appear word-for-word in the source it was given."""
import re

QUOTE_PATTERN = re.compile(r'"([^"]{1,500})"')


def _normalise(text):
    return " ".join(text.lower().split())


def find_quotes(response):
    return QUOTE_PATTERN.findall(response)


def verify_quotes(response, source, min_words=3):
    """
    Returns one entry per quote with at least min_words words:
    {"quote": ..., "grounded": True/False}.
    Short phrases are skipped because they match too easily.
    """
    source_norm = _normalise(source)
    results = []
    for quote in find_quotes(response):
        if len(quote.split()) < min_words:
            continue
        results.append({"quote": quote, "grounded": _normalise(quote) in source_norm})
    return results


def ungrounded(response, source, min_words=3):
    return [r["quote"] for r in verify_quotes(response, source, min_words) if not r["grounded"]]
