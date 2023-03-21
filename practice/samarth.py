import abc
class FormalParserInterface(metaclass=abc.ABCMeta):
    # @classmethod
    # def __subclasshook__(cls, subclass):
    #     return (hasattr(subclass, 'load_data_source') and 
    #             callable(subclass.load_data_source) and 
    #             hasattr(subclass, 'extract_text') and 
    #             callable(subclass.extract_text) or 
    #             NotImplemented)

    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        raise NotImplementedError

class EmlParserNew(FormalParserInterface):
    def load_data_source(self, path: str, file_name: str):
        pass

    def extract_text(self, full_file_path: str):
        pass

class PdfParserNew(FormalParserInterface):
    def load_data_source(self, path: str, file_name: str):
        pass
    def extract_text(self, full_file_path: str):
        pass



pdf_parser = PdfParserNew()
eml_parser = EmlParserNew()