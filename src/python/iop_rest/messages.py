from iop import Message
from dataclasses import dataclass

@dataclass
class RESTRequest(Message):
    method: str
    args: tuple
    kwargs: dict[str, any]

    @staticmethod
    def create(method, *args, **kwargs):
        """Helper method for creating requests"""
        return RESTRequest(method=method, args=args, kwargs=kwargs)

