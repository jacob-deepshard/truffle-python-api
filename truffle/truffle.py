from typing import Callable, Dict, List, Optional
import numpy as np


class Truffle:

    start_cbs: Dict[str, Callable[[], None]]
    stop_cbs: Dict[str, Callable[[], None]]

    def __init__(self):
        self.start_cbs = {}
        self.stop_cbs = {}

    def generate(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        top_p: Optional[float] = None,
        stop_strings: Optional[str] = None,
        streaming: Optional[bool] = False,
        on_chunk: Optional[Callable[[str], None]] = None,
        on_start: Optional[Callable[[], None]] = None,
        on_stop: Optional[Callable[[], None]] = None,
        **kwargs,
    ) -> str:
        """Generates a response from the model"""

        kwargs.update(locals())

        if streaming:
            return self._generate_stream(prompt, **kwargs)
        else:
            output = ""
            for chunk in self._generate_stream(prompt, **kwargs):
                output += chunk
            return output

    def _generate_stream(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
        top_p: Optional[float] = None,
        stop_strings: Optional[str] = None,
        streaming: Optional[bool] = False,
        on_chunk: Optional[Callable[[str], None]] = None,
        on_start: Optional[Callable[[], None]] = None,
        on_stop: Optional[Callable[[], None]] = None,
    ) -> str:
        """Generates a stream of responses from the model"""
        pass

    def embed(self, docs: List[str], **kwargs) -> np.ndarray:
        """Returns a numpy array of embeddings for the given documents"""
        pass

    def input(self, prompt: str, **kwargs) -> str:
        """Returns the user's input as a string"""
        pass

    def print(self, message: str, **kwargs):
        """Prints a message to the console"""
        pass

    def error(self, message: str, **kwargs):
        """Prints an error message to the console"""
        pass

    def add_start_callback(self, cb: Callable[[], None]) -> str:
        pass

    def add_stop_callback(self, cb: Callable[[], None]) -> str:
        pass

    def remove_start_callback(self, cb_or_id: Callable[[], None] | str):
        pass

    def remove_stop_callback(self, cb_or_id: Callable[[], None] | str):
        pass
