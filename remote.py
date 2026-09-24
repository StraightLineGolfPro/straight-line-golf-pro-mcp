"""Public HTTPS transport. Never imports the private SLGP operator plugin."""
import os
from urllib.parse import urlsplit
from mcp.server.transport_security import TransportSecuritySettings
from starlette.responses import JSONResponse, RedirectResponse
from starlette.routing import Route
from server import server


class AdmissionLimit:
    """Per-process concurrency bound; not a distributed rate limiter."""
    def __init__(self, app):
        self.app, self.active = app, 0

    async def __call__(self, scope, receive, send):
        if scope['type'] != 'http':
            return await self.app(scope, receive, send)
        if self.active >= 4:
            return await JSONResponse({'error': 'Busy; retry later.'}, status_code=429,
                                      headers={'Retry-After': '5'})(scope, receive, send)
        self.active += 1
        try:
            await self.app(scope, receive, send)
        finally:
            self.active -= 1


def create_app():
    origin = os.environ.get('SLGP_MCP_PUBLIC_ORIGIN', 'http://127.0.0.1:8765')
    u = urlsplit(origin)
    if (not u.hostname or u.username or u.password or u.path or u.query or u.fragment or
        (u.scheme != 'https' and not (u.scheme == 'http' and u.hostname in ('localhost', '127.0.0.1')))):
        raise ValueError('SLGP_MCP_PUBLIC_ORIGIN must be an exact HTTPS origin.')
    app = server.streamable_http_app(
        stateless_http=True, json_response=True, max_request_body_size=32768,
        transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=True,
            allowed_hosts=[u.netloc], allowed_origins=[origin]))

    async def health(request):
        return JSONResponse({'service': 'straight-line-golf-pro', 'version': '1.1.0',
            'read_only': True, 'content_readiness': 'validated on each tool call'},
            headers={'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex'})

    async def home(request):
        return RedirectResponse('https://github.com/StraightLineGolfPro/straight-line-golf-pro-mcp', status_code=302)

    app.routes.extend([Route('/health', health), Route('/', home)])
    app.add_middleware(AdmissionLimit)
    return app
