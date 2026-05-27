package web

import std.collection.*
import std.convert.*

// ===== Domain Model =====

class Todo {
    public var id: Int64
    public var title: String
    public var completed: Bool

    public init(id: Int64, title: String) {
        this.id = id
        this.title = title
        this.completed = false
    }

    public func toJson(): String {
        var status = "false"
        if (completed) {
            status = "true"
        }
        return "{\"id\":${id},\"title\":\"${title}\",\"completed\":${status}}"
    }
}

// ===== Service Layer =====

class TodoService {
    let _todos = ArrayList<Todo>()
    var _nextId: Int64 = 1

    public func findAll(): ArrayList<Todo> {
        return _todos
    }

    public func findById(id: Int64): ?Todo {
        for (t in _todos) {
            if (t.id == id) {
                return t
            }
        }
        return None
    }

    public func create(title: String): Todo {
        let todo = Todo(_nextId, title)
        _nextId++
        _todos.add(todo)
        return todo
    }

    public func deleteById(id: Int64): Bool {
        for (i in 0.._todos.size) {
            if (_todos[i].id == id) {
                _todos.remove(i..(i + 1))
                return true
            }
        }
        return false
    }
}

// ===== Application =====

main(): Int64 {
    let app = WebApp()

    // Register services (IoC)
    app.services.register("todoService", { => TodoService() }, lifetime: Singleton)

    // Logging middleware
    app.use({ ctx: HttpContext, next: () -> Unit =>
        println("[${ctx.request.method}] ${ctx.request.path}")
        next()
        println("  -> ${ctx.response.statusCode}")
    })

    // Error handling middleware
    app.use({ ctx: HttpContext, next: () -> Unit =>
        try {
            next()
        } catch (_: Exception) {
            ctx.response.statusCode = 500
            ctx.response.json("{\"error\":\"Internal Server Error\"}")
        }
    })

    // REST API routes using route group
    let api = app.group("/api")

    api.get("/todos", { ctx: HttpContext =>
        let svc = (ctx.services.resolve("todoService") as TodoService).getOrThrow()
        let todos = svc.findAll()
        let sb = StringBuilder()
        sb.append("[")
        for (i in 0..todos.size) {
            if (i > 0) { sb.append(",") }
            sb.append(todos[i].toJson())
        }
        sb.append("]")
        ctx.response.json(sb.toString())
    })

    api.get("/todos/:id", { ctx: HttpContext =>
        let svc = (ctx.services.resolve("todoService") as TodoService).getOrThrow()
        let idStr = ctx.request.param("id").getOrThrow()
        let id = Int64.parse(idStr)
        if (let Some(todo) <- svc.findById(id)) {
            ctx.response.json(todo.toJson())
        } else {
            ctx.response.status(404).json("{\"error\":\"Todo not found\"}")
        }
    })

    api.post("/todos", { ctx: HttpContext =>
        let svc = (ctx.services.resolve("todoService") as TodoService).getOrThrow()
        let title = ctx.request.body
        let todo = svc.create(title)
        ctx.response.status(201).json(todo.toJson())
    })

    api.delete("/todos/:id", { ctx: HttpContext =>
        let svc = (ctx.services.resolve("todoService") as TodoService).getOrThrow()
        let idStr = ctx.request.param("id").getOrThrow()
        let id = Int64.parse(idStr)
        if (svc.deleteById(id)) {
            ctx.response.status(204).text("")
        } else {
            ctx.response.status(404).json("{\"error\":\"Todo not found\"}")
        }
    })

    // Health check
    app.get("/health", { ctx: HttpContext =>
        ctx.response.json("{\"status\":\"ok\"}")
    })

    // Simulate API requests
    println("=== Todo REST API Demo ===")
    println()

    simulate(app, HttpMethod.POST, "/api/todos", body: "Buy groceries")
    simulate(app, HttpMethod.POST, "/api/todos", body: "Read a book")
    simulate(app, HttpMethod.GET, "/api/todos")
    simulate(app, HttpMethod.GET, "/api/todos/1")
    simulate(app, HttpMethod.DELETE, "/api/todos/1")
    simulate(app, HttpMethod.GET, "/api/todos")
    simulate(app, HttpMethod.GET, "/api/todos/999")
    simulate(app, HttpMethod.GET, "/health")

    return 0
}

func simulate(app: WebApp, method: HttpMethod, path: String, body!: String = ""): Unit {
    var req = Request(method, path)
    if (!body.isEmpty()) {
        req = Request(method, path, body)
    }
    let ctx = HttpContext(req, Response(), app.services)
    app.handleRequest(ctx)
    println("  Body: ${ctx.response.body}")
    println()
}
