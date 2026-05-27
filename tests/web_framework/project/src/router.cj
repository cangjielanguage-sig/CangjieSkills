package web

import std.collection.*

// Result of a route match
public class RouteMatch {
    public let handler: (HttpContext) -> Unit
    public let params: HashMap<String, String>

    public init(handler: (HttpContext) -> Unit, params: HashMap<String, String>) {
        this.handler = handler
        this.params = params
    }
}

// Internal route entry
class RouteEntry {
    let method: HttpMethod
    let segments: ArrayList<String>
    let handler: (HttpContext) -> Unit

    init(method: HttpMethod, pattern: String, handler: (HttpContext) -> Unit) {
        this.method = method
        this.handler = handler
        this.segments = ArrayList<String>()
        for (s in pattern.split("/", removeEmpty: true)) {
            segments.add(s)
        }
    }
}

// Router with path parameter support
public class Router {
    let _routes = ArrayList<RouteEntry>()

    public init() {}

    // Register a route
    public func addRoute(method: HttpMethod, pattern: String, handler: (HttpContext) -> Unit): Unit {
        _routes.add(RouteEntry(method, pattern, handler))
    }

    // Find a matching route for the given method and path
    public func findRoute(method: HttpMethod, path: String): ?RouteMatch {
        let pathSegments = ArrayList<String>()
        for (s in path.split("/", removeEmpty: true)) {
            pathSegments.add(s)
        }

        for (route in _routes) {
            if (route.method != method) {
                continue
            }
            if (let Some(params) <- matchSegments(route.segments, pathSegments)) {
                return RouteMatch(route.handler, params)
            }
        }
        return None
    }

    // Match route segments against path segments, extracting :param values
    func matchSegments(routeSegs: ArrayList<String>, pathSegs: ArrayList<String>): ?HashMap<String, String> {
        if (routeSegs.size != pathSegs.size) {
            return None
        }
        let params = HashMap<String, String>()
        for (i in 0..routeSegs.size) {
            let rs = routeSegs[i]
            let ps = pathSegs[i]
            if (rs.startsWith(":")) {
                params[rs[1..rs.size]] = ps
            } else if (rs != ps) {
                return None
            }
        }
        return params
    }
}

// Route group with a shared path prefix
public class RouteGroup {
    let _router: Router
    let _prefix: String

    init(router: Router, prefix: String) {
        _router = router
        _prefix = prefix
    }

    public func get(pattern: String, handler: (HttpContext) -> Unit): Unit {
        _router.addRoute(HttpMethod.GET, _prefix + pattern, handler)
    }

    public func post(pattern: String, handler: (HttpContext) -> Unit): Unit {
        _router.addRoute(HttpMethod.POST, _prefix + pattern, handler)
    }

    public func put(pattern: String, handler: (HttpContext) -> Unit): Unit {
        _router.addRoute(HttpMethod.PUT, _prefix + pattern, handler)
    }

    public func delete(pattern: String, handler: (HttpContext) -> Unit): Unit {
        _router.addRoute(HttpMethod.DELETE, _prefix + pattern, handler)
    }
}
