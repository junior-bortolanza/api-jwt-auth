class HttpRequest:
    def __init__(
            self, 
            body: dict = None,
            headers: dict = None,
            params: dict = None,
            tokens_infos: dict = None
            ) -> None:
        self.body = body
        self.headers = headers
        self.param = params
        self.tokens_info = tokens_infos

http_request = HttpRequest(body={"Olã": "MUndo"})

