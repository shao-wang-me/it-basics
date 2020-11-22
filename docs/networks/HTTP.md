# HTTP

1. What is HTTP?

    HTTP stands for HyperText Transfer Protocol, specified in RFC 2616, is a simple request-response application layer protocol.

1. Which transport layer protocol does HTTP use?

    It normally uses TCP but can use any suitable protocol. The protocol should be reliable, meaning it doesn't lose messages silently (such as UDP).

1. What encoding is used by HTTP?

    The request and response headers are encoded in ASCII.
    
    TODO: Payload encoding?

1. Which port does HTTP use?

    It can use any port but 80 is the most common port. Web browsers hide the port when it's 80.

1. What are the common methods in HTTP?

    | Method  | Description                             |
    | ------- | --------------------------------------- |
    | GET     | Get a resource.                         |
    | HEAD    | The response will only have the header. |
    | POST    | Send some information.                  |
    | PUT     | Replace a resource.                     |
    | DELETE  | Delete a resource.                      |
    | TRACE   | Echo the incoming request.              |
    | CONNECT | CONNECT through a proxy.                |
    | OPTIONS | Query options for a resource.           |

1. Are methods in HTTP case sensitive?

    Yes.

1. What is the difference between PUT and POST?

1. What is the structure of a HTTP message?

1. How does HTTP connect to the destination machine?

1. Who and what specifies HTTP?

1. What is HTTPS?

1. How does the performance of HTTPS compare to HTTP?

1. How does the performance of HTTP compare to TCP?

1. When I visit a website, why can I see TCP message (segment) in Wireshark?

    Because HTTP normally uses TCP as the transport layer protocol. The HTTP client needs to establish the TCP connection first.

1. What happens when I visit a web page in the browser?