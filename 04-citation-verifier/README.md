# Citation Verifier

Checks whether quoted text in an AI answer really appears in the document the model was given. Invented quotes are a common hallucination, and this catches them automatically.

Short phrases (fewer than 3 words by default) are skipped, since they match too easily.

**Skills shown:** hallucination detection, grounding checks, text normalisation.

## Run the tests

```
python3 -m unittest -v
```

## Example

```python
from verify_quotes import ungrounded

bad_quotes = ungrounded(model_answer, source_document)
print("Invented quotes:", bad_quotes)
```

## Limits

This only checks exact quotes. It does not catch paraphrases that change the meaning. Pair it with a claim checker for those.
