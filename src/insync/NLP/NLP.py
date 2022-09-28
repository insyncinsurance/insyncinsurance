class TriggerError(Exception):
    pass


class NLP:
    def __init__(self):
        self.__tokens = []
        self.__text = ""
        self.__triggers = []
        self.__sentences = []

    def load_text(self, text):
        self.__text = text.lower()

    def word_tokenize(self):
        self.__tokens = self.__text.lower().split(" ")

        for i in range(0, len(self.__tokens)):
            self.__tokens[i] = self.__tokens[i].strip(".,?!:;")

    def get_tokens(self):
        return self.__tokens

    def load_triggers(self, triggers):
        for i in triggers:
            self.__triggers.append(i.lower())

    def analyse(self):
        triggers = []
        for token in self.__tokens:
            if token in self.__triggers:
                triggers.append(token)
        return triggers

    def cleanse(self):
        self.__text = ""
        self.__triggers = []

    def purge(self):
        self.__text = ""
        self.__tokens = []
        self.__triggers = []
        self.__sentences = []

    def sentence_split(self):
        self.__sentences = self.__text.split(".")
        for i in range(0, len(self.__sentences)):
            self.__sentences[i] = self.__sentences[i].strip(" ")
            if self.__sentences[i] == "":
                self.__sentences.pop(i)

    def get_sentences(self):
        return self.__sentences

    def get_triggers(self):
        return self.__triggers

    def get_text(self):
        return self.__text


nlp = NLP()


def analyse_text(text, triggers, *args):
    nlp.load_text(text)
    nlp.word_tokenize()
    nlp.load_triggers(triggers)
    referrals = nlp.analyse()

    if len(referrals) > 0:
        raise TriggerError(' '.join(map(str, args)))