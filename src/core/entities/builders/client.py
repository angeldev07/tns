from __future__ import annotations
from src.core.entities.client import Client
from abc import ABC, abstractmethod


class IClientBuilder(ABC):

    @abstractmethod
    def build(self) -> Client:
        pass

    @abstractmethod
    def Id(self) -> IClientBuilder:
        pass

    @abstractmethod
    def cedula(self) -> IClientBuilder:
        pass

    @abstractmethod
    def partial_full_name(self) -> IClientBuilder:
        pass

    @abstractmethod
    def residence_id(self) -> IClientBuilder:
        pass


class ClientBuilder(IClientBuilder):

    def __init__(self) -> None:
        self.__reset__()

    def __reset__(self):
        self._client = Client()

    def build(self) -> Client:
        build_obj = self._client
        self.__reset__()
        return build_obj

    def Id(self, id) -> ClientBuilder:
        self._client.id = id
        return self

    def cedula(self, cedula) -> ClientBuilder:
        self._client.cedula = cedula
        return self

    def partial_full_name(self, name: str) -> ClientBuilder:
        self._client.partial_full_name = name
        return self

    def residence_id(self, residence: str) -> ClientBuilder:
        self._client.residence_id = residence
        return self
