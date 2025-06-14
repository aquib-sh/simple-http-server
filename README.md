# Simple HTTP Server

A lightweight HTTP server implementation written from scratch in Python. This project demonstrates the core concepts of web servers and HTTP protocol implementation while providing a functional server that can handle both static and dynamic content.

## Features

- Built from scratch using Python's socket programming
- Handles both GET and POST requests
- Serves static content (files, images, etc.)
- Dynamic routing with controller-based architecture
- JSON response support
- Configurable content types
- Error handling with appropriate HTTP status codes

## Project Structure

```
.
├── server.py                 # Main server implementation
├── request_parser.py         # HTTP request parsing
├── response_builder.py       # HTTP response construction
├── response_dispatcher.py    # Response handling
├── static_content_provider.py # Static file serving
├── http_status.py           # HTTP status codes
├── startup.py               # Server initialization
├── controllers/             # Request handlers
├── static/                  # Static content directory
└── appsettings.json         # Server configuration
```

## Prerequisites

- Python 3.x
- Basic understanding of HTTP protocol

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/simple-http-server.git
cd simple-http-server
```

2. Run the server:
```bash
python server.py
```

The server will start listening on `0.0.0.0:8000` by default.

## Usage

The server supports:
- Static file serving from the `static/` directory
- Dynamic routes through controllers
- JSON responses for API endpoints
- Basic error handling

### Example Requests

#### Static Content
- HTML page: `GET http://localhost:8000/static/home.html`
- Image file: `GET http://localhost:8000/static/mobile_phone.png`

#### API Endpoints
- Get all users: `GET http://localhost:8000/users`
- Add a new user: `POST http://localhost:8000/users`
  ```json
  {
    "name": "John Doe",
    "age": "25",
    "city": "New York"
  }
  ```

## Contributing

Contributions are welcome! This project is open for improvements and new features. Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Future Development

- [ ] Database integration
- [ ] Move configurable parts outside of code into a config file
- [ ] HTTPS support
- [ ] Request validation
- [ ] Authentication and authorization
- [ ] CORS support
- [ ] Rate limiting
- [ ] Documentation improvements
- [ ] Transform this project into a reusable framework and library

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for educational purposes to understand HTTP server implementation
- Inspired by [Joao Ventura's blog](https://joaoventura.net/blog/2017/python-webserver/)
