import requests

class Urban:
    """returns back synonyms"""
    def __init__(self, word):
        self.word = str(word).replace(" ", "%20")
        self.json = None
        self.lookup = self.lookup()
        self.synonyms = self.synonyms(self.json)
        self.top = self.top()

    def lookup(self):
        words = requests.get("http://urbanthesaurus.org/api/related?term="+self.word).json()
        self.json = words
        return((self.json if words else quit()))

    def top(self):
        return self.synonyms[0]

    def synonyms(self, words):
        words = [x["word"].encode("utf-8") for x in words]
        return words

"""returns back definition"""
def definition(word):
    result = requests.get("http://api.urbandictionary.com/v0/define?term="+str(word)).json()
    return((result["list"][0]["definition"] if result["result_type"] == "exact" else "Not Valid"))

# word = Urban("meow")
# print(word.top)
# print([definition(x) for x in word.synonyms])
# print(definition(word.word))
