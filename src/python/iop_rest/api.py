from uplink import Consumer
from .interface import IrisInterface

class BaseClientREST(Consumer):
    def __init__(
                self,
                iris_adapter,
                *,
                client=None,
                converters=(),
                auth=None,
                hooks=()
            ) -> None:
        if client==None:
            client=IrisInterface(session=iris_adapter)
        scheme = 'https' if iris_adapter.SSLConfig != "" else 'http'
        return super(BaseClientREST, self).__init__(
            base_url=f'{scheme}://{iris_adapter.HTTPServer}:{iris_adapter.HTTPPort}{iris_adapter.URL}',
            client=client,
            converters=converters,
            auth=auth,
            hooks=hooks,
        )
    