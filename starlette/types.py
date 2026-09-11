import sys
import typing

if sys.version_info >= (3, 9):  # pragma: no cover
    from collections.abc import Awaitable, Callable, Mapping, MutableMapping
    from contextlib import AbstractAsyncContextManager
else:  # pragma: no cover
    # `collections.abc` generics are only subscriptable from Python 3.9 onwards.
    from typing import (
        AsyncContextManager as AbstractAsyncContextManager,
        Awaitable,
        Callable,
        Mapping,
        MutableMapping,
    )

if typing.TYPE_CHECKING:
    from starlette.requests import Request
    from starlette.responses import Response
    from starlette.websockets import WebSocket

AppType = typing.TypeVar("AppType")

Scope = MutableMapping[str, typing.Any]
Message = MutableMapping[str, typing.Any]

Receive = Callable[[], Awaitable[Message]]
Send = Callable[[Message], Awaitable[None]]

ASGIApp = Callable[[Scope, Receive, Send], Awaitable[None]]

StatelessLifespan = Callable[[AppType], AbstractAsyncContextManager[None]]
StatefulLifespan = Callable[[AppType], AbstractAsyncContextManager[Mapping[str, typing.Any]]]
Lifespan = typing.Union[StatelessLifespan[AppType], StatefulLifespan[AppType]]

HTTPExceptionHandler = Callable[["Request", Exception], "Response | Awaitable[Response]"]
WebSocketExceptionHandler = Callable[["WebSocket", Exception], Awaitable[None]]
ExceptionHandler = typing.Union[HTTPExceptionHandler, WebSocketExceptionHandler]
