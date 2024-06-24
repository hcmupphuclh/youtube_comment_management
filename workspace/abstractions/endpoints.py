from workspace.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from abc import ABC

class AbstractionOfEndpoints(ABC):
    
    route: str = None
    endpoint: str = None
    callback_function: str = None
    methods: list = None
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        self.progressOfMainStub = progressOfMainStub
        
    def endpoint_adjustment(self):
        self.progressOfMainStub.progress.add_url_rule(rule = self.route, endpoint = self.endpoint,
                                                      view_func = self.callback_function, methods = self.methods)