from iop import BusinessOperation
from .api import BaseClientREST
from .messages import RESTRequest
import traceback

class BaseRESTOperation(BusinessOperation):
    client: BaseClientREST

    @staticmethod
    def get_adapter_type():
        return "EnsLib.HTTP.OutboundAdapter"

    def init_client(self, adapter) -> BaseClientREST: pass

    def on_init(self):
        self.client = self.init_client(self.adapter)
        return super().on_init()

    def on_request(self, request: RESTRequest):
        try:
            if hasattr(self.client, request.method) and callable(func := getattr(self.client, request.method)):
                data = func(*request.args, **request.kwargs)
                # https://github.com/grongierisc/interoperability-embedded-python/issues/25
                if isinstance(data, list):
                    raise NotImplementedError("List messages not supported")
                return data
            else:
                raise Exception(f"Method '{request.method}' does not exist")
        except Exception as e:
                self.log_error("".join(traceback.format_exception(e)))
