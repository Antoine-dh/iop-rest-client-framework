from uplink import interfaces
from uplink.clients import exceptions, interfaces, register, io
from io import BytesIO
import iris
from requests.models import Response
import json

class IrisInterface(interfaces.HttpClientAdapter):
    """
    A IRIS client that uses native EnsLib.HTTP.OutboundAdapter for sending requests
    returns :py:class:`requests.Response` responses.

    Args:
        adapter: The IRIS REST outbound adapter
            that should handle sending requests.
    """

    exceptions = exceptions.Exceptions()

    def __init__(self, session=None):
        self.adapter = session

    @staticmethod
    @register.handler
    def with_session(session, *args, **kwargs):
        return IrisInterface(session, *args, **kwargs)

    def send(self, request):
        iris.cls("Ens.Util.Log").LogInfo("IrisInterface", "send", str(request))
        method, url, extras = request
        iris_request = iris.cls("%Net.HttpRequest")._New()
        if 'params' in extras:
            for k,v in extras['params'].items():
                if v is list:
                    for v2 in v:
                        iris_request.InsertParam(k, v2)
                else:
                    iris_request.SetParam(k, v)
        if 'data' in extras:
            iris_request.EntityBody.Write(str(extras['data']))
        elif 'json' in extras:
            iris_request.EntityBody.Write(json.dumps(extras['json']))
        if 'headers' in extras:
            for k,v in extras['headers'].items():
                iris_request.SetHeader(k, v)
        iris_response = iris.ref()
        tsc = self.adapter.SendFormDataArray(iris_response, method, iris_request, None, None, url)
        error = iris.cls('%SYSTEM.Status').GetErrorText(tsc)
        if error:
            iris.cls("Ens.Util.Log").LogError("IrisInterface", "send", error)
            if hasattr(iris_response, "Data"):
                while not iris_response.Data.AtEnd:
                    iris.cls("Ens.Util.Log").LogInfo("IrisInterface", "send", str(iris_response.Data.Read()))
        return iris_response.value

    """
        args:
            callback: uplink callback
            iris_response: %Net.HttpResponse IRIS object
    """
    def apply_callback(self, callback, iris_response):
        headers = {}
        key = ''
        while True:
            key = iris_response.GetNextHeader(key)
            if key == None or key == "":
                break
            headers[key] = iris_response.GetHeader(key)
        encoding = 'utf-8'
        buffer = BytesIO()
        while not iris_response.Data.AtEnd:
            buffer.write(str.encode(iris_response.Data.Read(), encoding=encoding))
        buffer.seek(0)
        response = Response()
        response.status_code=iris_response.StatusCode,
        response.raw=buffer
        response.headers=headers
        if response.status_code not in range(200,299):
            iris.cls("Ens.Util.Log").LogInfo("IrisInterface", "send", buffer.getvalue().decode())
        return callback(response)

    @staticmethod
    def io():
        return io.BlockingStrategy()


# # === Register client exceptions === #
# RequestsClient.exceptions.BaseClientException = requests.RequestException
# RequestsClient.exceptions.ConnectionError = requests.ConnectionError
# RequestsClient.exceptions.ConnectionTimeout = requests.ConnectTimeout
# RequestsClient.exceptions.ServerTimeout = requests.ReadTimeout
# RequestsClient.exceptions.SSLError = requests.exceptions.SSLError
# RequestsClient.exceptions.InvalidURL = requests.exceptions.InvalidURL
