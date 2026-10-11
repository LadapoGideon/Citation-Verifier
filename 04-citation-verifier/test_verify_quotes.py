import unittest

from verify_quotes import find_quotes, ungrounded, verify_quotes


SOURCE = """
The central bank said inflation fell to 24.5 percent in the last quarter.
Officials expect further easing if oil prices stay stable.
"""


class VerifyQuotesTests(unittest.TestCase):
    def test_finds_quoted_text(self):
        self.assertEqual(find_quotes('He said "hello there" today.'), ["hello there"])

    def test_grounded_quote_passes(self):
        response = 'The bank said "inflation fell to 24.5 percent" recently.'
        self.assertTrue(verify_quotes(response, SOURCE)[0]["grounded"])

    def test_invented_quote_is_flagged(self):
        response = 'The bank said "inflation rose to 30 percent" recently.'
        self.assertEqual(ungrounded(response, SOURCE), ["inflation rose to 30 percent"])

    def test_match_ignores_case_and_extra_spaces(self):
        response = 'It said "INFLATION   fell to 24.5 percent".'
        self.assertEqual(ungrounded(response, SOURCE), [])

    def test_short_quotes_are_skipped(self):
        response = 'The report calls it "bad".'
        self.assertEqual(verify_quotes(response, SOURCE), [])


if __name__ == "__main__":
    unittest.main()
