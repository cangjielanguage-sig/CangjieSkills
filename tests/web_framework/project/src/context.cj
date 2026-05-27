package web

import std.collection.*

// Custom exception for web framework errors
public class WebException <: Exception {
    public init(message: String) {
        super(message)
    }
}

// HTTP method enum with string parsing support
public enum HttpMethod <: Equatable<HttpMethod> & ToString {
    GET | POST | PUT | DELETE | PATCH

    public operator func ==(other: HttpMethod): Bool {
        match ((this, other)) {
            case (GET, GET) => true
            case (POST, POST) => true
            case (PUT, PUT) => true
            case (DELETE, DELETE) => true
            case (PATCH, PATCH) => true
            case _ => false
        }
    }

    public operator func !=(other: HttpMethod): Bool {
        return !(this == other)
    }

    public func toString(): String {
        match (this) {
            case GET => "GET"
            case POST => "POST"
            case PUT => "PUT"
            case DELETE => "DELETE"
            case PATCH => "PATCH"
        }
    }

    // Parse HTTP method from string (case-insensitive)
    public static func fromString(s: String): HttpMethod {
        let upper = s.toAsciiUpper()
        if (upper == "GET") { return GET }
        if (upper == "POST") { return POST }
        if (upper == "PUT") { return PUT }
        if (upper == "DELETE") { return DELETE }
        if (upper == "PATCH") { return PATCH }
        throw WebException("Unknown HTTP method: ${s}")
    }
}

// HTTP request with automatic query string parsing
public class Request {
    public var method: HttpMethod
    public var path: String
    public var headers: HashMap<String, String>
    public var body: String
    public var pathParams: HashMap<String, String>
    public var queryParams: HashMap<String, String>

    public init(method: HttpMethod, path: String) {
        this.method = method
        this.body = ""
        this.headers = HashMap<String, String>()
        this.pathParams = HashMap<String, String>()
        this.queryParams = HashMap<String, String>()
        this.path = extractPath(path, this.queryParams)
    }

    public init(method: HttpMethod, path: String, body: String) {
        this.method = method
        this.body = body
        this.headers = HashMap<String, String>()
        this.pathParams = HashMap<String, String>()
        this.queryParams = HashMap<String, String>()
        this.path = extractPath(path, this.queryParams)
    }

    // Convenience: get path parameter by name
    public func param(name: String): ?String {
        return pathParams.get(name)
    }

    // Convenience: get query parameter by name
    public func query(name: String): ?String {
        return queryParams.get(name)
    }

    // Convenience: get header by name
    public func header(name: String): ?String {
        return headers.get(name)
    }
}

// HTTP response with fluent API and content-type helpers
public class Response {
    public var statusCode: Int64
    public var headers: HashMap<String, String>
    public var body: String

    public init() {
        this.statusCode = 200
        this.headers = HashMap<String, String>()
        this.body = ""
    }

    // Set a response header
    public func setHeader(name: String, value: String): Unit {
        headers[name] = value
    }

    // Fluent: set status code and return self for chaining
    public func status(code: Int64): Response {
        this.statusCode = code
        return this
    }

    // Set JSON response body with Content-Type
    public func json(data: String): Unit {
        headers["Content-Type"] = "application/json"
        this.body = data
    }

    // Set plain text response body with Content-Type
    public func text(data: String): Unit {
        headers["Content-Type"] = "text/plain"
        this.body = data
    }

    // Set HTML response body with Content-Type
    public func html(data: String): Unit {
        headers["Content-Type"] = "text/html"
        this.body = data
    }
}

// HTTP context wrapping request, response, and services
public class HttpContext {
    public let request: Request
    public let response: Response
    public let services: ServiceContainer

    public init(request: Request, response: Response, services: ServiceContainer) {
        this.request = request
        this.response = response
        this.services = services
    }
}

// Parse raw path and extract query parameters into the provided map
// e.g. "/search?q=hello&page=1" -> returns "/search", fills {q: "hello", page: "1"}
func extractPath(rawPath: String, params: HashMap<String, String>): String {
    if (let Some(idx) <- rawPath.indexOf("?")) {
        if (idx + 1 < rawPath.size) {
            parseQueryPairs(rawPath[(idx + 1)..rawPath.size], params)
        }
        return rawPath[0..idx]
    }
    return rawPath
}

// Parse "key1=val1&key2=val2" into the provided map
func parseQueryPairs(queryStr: String, params: HashMap<String, String>): Unit {
    for (pair in queryStr.split("&", removeEmpty: true)) {
        if (let Some(eqIdx) <- pair.indexOf("=")) {
            let key = pair[0..eqIdx]
            var value = ""
            if (eqIdx + 1 < pair.size) {
                value = pair[(eqIdx + 1)..pair.size]
            }
            params[key] = value
        } else {
            params[pair] = ""
        }
    }
}
