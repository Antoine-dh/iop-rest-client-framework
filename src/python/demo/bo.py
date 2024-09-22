from iop_rest.bo import BaseRESTOperation
from generated.api import PetstoreClient

class PetstoreOperation(BaseRESTOperation):
    client: PetstoreClient

    def init_client(self, adapter):
        return PetstoreClient(adapter)
