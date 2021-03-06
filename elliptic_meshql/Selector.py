from abc import abstractmethod
from typing import Type, cast

from elliptic.Kernel.Context import ContextDelegate
from elliptic.Kernel.Contract import DSLContract, DSLImplementation
from elliptic.Kernel.Expression import Expression


class SelectorImplementationBase(DSLImplementation):

    @abstractmethod
    def by_ent_delegate(self, dim: int) -> Type[ContextDelegate]:
        raise NotImplementedError

    @abstractmethod
    def by_adj_delegate(self, bridge_dim: int, to_dim: int) -> Type[ContextDelegate]:
        raise NotImplementedError

    @abstractmethod
    def where_delegate(self, conditions):
        raise NotImplementedError


class SelectorContract(DSLContract[SelectorImplementationBase]):

    def ByEnt(self, dim: int) -> 'SelectorContract':
        return self.append_tree(
            Expression(
                self.dsl_impl.by_ent_delegate(dim),
                "ByEnt",
                {'dim': dim}))

    def ByAdj(self, bridge_dim: int, to_dim: int) -> 'SelectorContract':
        return self.append_tree(
            Expression(
                self.dsl_impl.by_adj_delegate(bridge_dim, to_dim),
                "ByAdj",
                {'bridge_dim': bridge_dim, 'to_dim': to_dim}))

    def Where(self, **conditions):
        return self.append_tree(Expression(self.dsl_impl.where_delegate(conditions), "Where"))
