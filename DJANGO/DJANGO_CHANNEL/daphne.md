Daphne is an HTTP, HTTP2, and WebSocket server for ASGI (Asynchronous Server Gateway Interface) and is commonly used with Django Channels. It acts as a bridge between the web server (like Nginx or Apache) and your Django application, allowing it to handle asynchronous protocols.

### Key Features of Daphne:

1. **ASGI Compatibility**: Daphne is designed to work with ASGI applications, making it suitable for handling asynchronous operations such as WebSockets.

2. **WebSocket Support**: It allows your Django application to manage real-time communications through WebSocket connections, which is essential for applications like chat systems or live notifications.

3. **HTTP/2 Support**: Daphne supports HTTP/2, enabling better performance through multiplexing, header compression, and server push features.

4. **Integration with Django Channels**: It is often used alongside Django Channels to add asynchronous capabilities to Django applications, allowing for features like background tasks and real-time updates.

### Installation

You can install Daphne using pip:

```bash
pip install daphne
```

### Running Daphne

You can run a Django application using Daphne by specifying the ASGI application:

```bash
daphne myproject.asgi:application
```

Here, `myproject.asgi:application` refers to the ASGI application defined in your Django project (usually in `asgi.py`).

### Example Usage

In a Django project, your `asgi.py` might look something like this:

```python
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import myapp.routing  # Import your app's routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            myapp.routing.websocket_urlpatterns  # Your WebSocket routes
        )
    ),
})
```

Daphne would serve this ASGI application, allowing it to handle both HTTP requests and WebSocket connections.

Let me know if you need more information or examples!
