from functions.preprocess import app
import unittest
import string
import numpy as np
class TestStringMethods(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        stop_words = []
        stop_words += list(string.punctuation)
        stop_words += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        stop_words += ["have","of","the","she","I","They","Her","She","Me","Something"]
        self.stop = set(stop_words)

    def test_remove_urls(self):
        assert app.remove_urls("https://www.google.com/") == ""


    def test_expand_contractions(self):
        assert app.expand_contractions("i've") == "i have"

    def test_remove_mentions_tags_retweets(self):
        assert app.remove_mentions_and_tags("@love") == ""
        assert app.remove_mentions_and_tags("#something") == ""


    def test_standardize_accented_chars(self):
        assert app.standardize_accented_chars("é") == "e"

    def test_lambda_handler(self):
        context = {
            'dir': './output/'
        }
        data = app.lambda_handler("",context)
        assert type(data) == dict
        assert "text" in data['file'].columns
        assert type(data["file"].iloc[0,1]) == np.int64
        for i in ["@","#","http","rt"]:
            assert i not in data["file"].loc[0,"text"]

        