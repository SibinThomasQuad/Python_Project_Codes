To run your FastAPI application on a public IP, you need to ensure a few things:

1. **Use `0.0.0.0` as the host:**
   Update the `uvicorn` command to bind the application to `0.0.0.0` instead of the default `127.0.0.1`. This allows the application to be accessible externally.

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```

2. **Open Firewall Ports:**
   Ensure that the firewall on your server allows incoming traffic on the specified port (default is `8000`). You might need to configure your cloud provider's firewall settings or any other firewall software running on the server.

3. **External IP Address:**
   Replace `127.0.0.1` with the public IP address of your server. You can find this IP address by checking the details of your server instance on your cloud provider's dashboard.

   ```javascript
   const socket = new WebSocket('ws://<your_public_ip>:8000/ws/1');
   ```

   Also, use the public IP address when accessing your FastAPI application from a web browser:

   ```http
   http://<your_public_ip>:8000/
   ```

4. **Security Considerations:**
   - Make sure your application is properly secured, especially when running it on a public IP. Use HTTPS, handle user authentication securely, and consider deploying the application behind a reverse proxy (e.g., Nginx or Apache) with proper security configurations.

Here is a summary of the `uvicorn` command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Replace `<your_public_ip>` with the actual public IP address of your server. After running the application with the updated command, you should be able to access it using the public IP address and WebSocket connections should work as expected.

Keep in mind that running applications on public IPs requires proper security measures to protect your application and server. Use HTTPS for secure communication and follow best practices for securing your server and application.
