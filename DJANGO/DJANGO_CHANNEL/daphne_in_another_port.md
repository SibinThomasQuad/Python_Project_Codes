Yes, you can run Daphne on a different port by specifying the desired port when starting the server. 

### Running Daphne on a Different Port

When you run Daphne, you can use the `-p` option followed by the port number. For example, to run Daphne on port 8001, you would use the following command:

```bash
daphne -p 8001 myproject.asgi:application
```

### Example Usage

If your project is structured as follows:

```
myproject/
    ├── myapp/
    ├── myproject/
    │   ├── asgi.py
    │   ├── settings.py
    └── manage.py
```

You can navigate to your project directory and run:

```bash
daphne -p 8001 myproject.asgi:application
```

### Additional Considerations

- **Firewall Rules**: Ensure that the chosen port is open in your firewall settings if you're running it on a server.
- **Reverse Proxy Configuration**: If you’re using a reverse proxy (like Nginx), update its configuration to point to the new port where Daphne is running.

Let me know if you need any more assistance!
