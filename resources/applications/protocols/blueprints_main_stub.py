from flask import Blueprint
from typing import Protocol

class ProgressOfMainStub(Protocol):
    
    @property
    def progress(self) -> Blueprint: ...