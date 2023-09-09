def my():
    from typing import Any, Callable, TypeVar

    T = TypeVar("T")

    def dataclass_transform(
        *,
        eq_default: bool = True,
        order_default: bool = False,
        kw_only_default: bool = False,
        field_specifiers: tuple[type[Any] | Callable[..., Any], ...] = (),
        **kwargs: Any,
    ) -> Callable[[T], T]:
        def decorator(cls_or_fn):
            cls_or_fn.__dataclass_transform__ = {
                "eq_default": eq_default,
                "order_default": order_default,
                "kw_only_default": kw_only_default,
                "field_specifiers": field_specifiers,
                "kwargs": kwargs,
            }
            return cls_or_fn

        return decorator

    @dataclass_transform()
    class NewBaseModel:
        pass

    class A(NewBaseModel):
        a: str

    # type error X - decorator not working
    A()
    # type error O - decorator not working
    A(a="a")


def standard():
    from typing import dataclass_transform

    @dataclass_transform()
    class NewBaseModel:
        pass

    class A(NewBaseModel):
        a: str

    # type error O - decorator working
    A()
    # type error X - decorator working
    A(a="a")
