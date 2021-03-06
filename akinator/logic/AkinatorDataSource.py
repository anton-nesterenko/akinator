from abc import ABCMeta, abstractmethod


class ANSWERS(object):
    YES = 'yes'
    NO = 'no'
    DO_NOT_KNOW = 'dnn'
    DOES_NOT_MATTER = 'dnm'

    RANGE = (YES, NO, DOES_NOT_MATTER)


class Entity(object):
    """
    Akinator entity to describe entity
    """
    def __init__(self, key, name, description):
        self.key = key
        self.name = name
        self.description = description


class Question(object):
    """
    Akinator entity to describe question
    """
    def __init__(self, key, text):
        self.key = key
        self.text = text


class AkinatorDataSource(object):
    """
    Interface to provide data for akinator
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_entities_list(self):
        pass

    @abstractmethod
    def get_entity(self, key):
        pass

    @abstractmethod
    def get_questions_list(self):
        pass

    @abstractmethod
    def get_question(self, key):
        pass

    @abstractmethod
    def get_answers_count(self, entity_key, question_key):
        pass

    @abstractmethod
    def create_entity(self, name, description):
        pass

    @abstractmethod
    def save_history(self, history, entity, success):
        pass
