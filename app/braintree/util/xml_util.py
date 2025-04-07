from app.braintree.util.parser import Parser
from app.braintree.util.generator import Generator

class XmlUtil(object):
    @staticmethod
    def xml_from_dict(dict):
        return Generator(dict).generate()

    @staticmethod
    def dict_from_xml(xml):
        return Parser(xml).parse()
