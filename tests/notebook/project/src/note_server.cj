package notebook

import stdx.net.http.*
import stdx.net.tls.*
import stdx.encoding.json.*
import stdx.crypto.x509.{X509Certificate, PrivateKey}
import std.collection.*
import std.convert.*
import std.io.{StringReader}
import std.sync.*

public class NoteServer {
    private var service: NoteService
    private var server: ?Server = None

    public init(service: NoteService) {
        this.service = service
    }

    public func start(addr: String, port: UInt16): Unit {
        let svr = ServerBuilder()
            .addr(addr)
            .port(port)
            .build()
        registerRoutes(svr)
        startServer(svr)
    }

    public func startTls(addr: String, port: UInt16, certPem: String, keyPem: String): Unit {
        var tlsConfig = TlsServerConfig(
            X509Certificate.decodeFromPem(certPem),
            PrivateKey.decodeFromPem(keyPem)
        )
        tlsConfig.supportedAlpnProtocols = ["http/1.1"]
        let svr = ServerBuilder()
            .addr(addr)
            .port(port)
            .tlsConfig(tlsConfig)
            .build()
        registerRoutes(svr)
        startServer(svr)
    }

    private func registerRoutes(svr: Server): Unit {
        svr.distributor.register("/api/notes", FuncHandler({ ctx =>
            this.handleNotes(ctx)
        }))
        svr.distributor.register("/api/note", FuncHandler({ ctx =>
            this.handleNote(ctx)
        }))
        svr.distributor.register("/api/stats", FuncHandler({ ctx =>
            this.handleStats(ctx)
        }))
    }

    private func startServer(svr: Server): Unit {
        let ready = SyncCounter(1)
        svr.afterBind({ => ready.dec() })
        server = svr
        spawn { svr.serve() }
        ready.waitUntilZero()
    }

    public func stop(): Unit {
        if (let Some(svr) <- server) {
            svr.close()
        }
    }

    public func getPort(): UInt16 {
        if (let Some(svr) <- server) {
            return svr.port
        }
        return 0
    }

    // --- Route Dispatchers ---

    private func handleNotes(ctx: HttpContext): Unit {
        let method = ctx.request.method
        if (method == "POST") {
            handleCreateNote(ctx)
        } else if (method == "GET") {
            handleListNotes(ctx)
        } else {
            respondError(ctx, 405, "Method not allowed")
        }
    }

    private func handleNote(ctx: HttpContext): Unit {
        let method = ctx.request.method
        if (method == "GET") {
            handleGetNote(ctx)
        } else if (method == "PUT") {
            handleUpdateNote(ctx)
        } else if (method == "DELETE") {
            handleDeleteNote(ctx)
        } else {
            respondError(ctx, 405, "Method not allowed")
        }
    }

    private func handleStats(ctx: HttpContext): Unit {
        respondJson(ctx, 200, service.getStats().toString())
    }

    // --- Individual Handlers ---

    private func handleCreateNote(ctx: HttpContext): Unit {
        try {
            let body = StringReader(ctx.request.body).readToEnd()
            let jv = JsonValue.fromStr(body)
            let obj = jv.asObject()
            let title = obj["title"].asString().getValue()
            let content = obj["content"].asString().getValue()
            let tags = parseTagsArray(obj["tags"].asArray())
            let note = service.createNote(title, content, tags)
            respondJson(ctx, 200, note.toJsonValue().toString())
        } catch (e: Exception) {
            respondError(ctx, 400, "Invalid request body")
        }
    }

    private func handleListNotes(ctx: HttpContext): Unit {
        let query = ctx.request.url.rawQuery ?? ""
        let tagParam = getQueryParam(query, "tag")
        var notesList: ArrayList<Note>
        if (let Some(tag) <- tagParam) {
            notesList = service.getNotesByTag(tag)
        } else {
            notesList = service.getAllNotes()
        }
        let result = JsonObject()
        let arr = JsonArray()
        for (note in notesList) {
            arr.add(note.toJsonValue())
        }
        result.put("notes", arr)
        result.put("total", JsonInt(notesList.size))
        respondJson(ctx, 200, result.toString())
    }

    private func handleGetNote(ctx: HttpContext): Unit {
        let query = ctx.request.url.rawQuery ?? ""
        let idStr = getQueryParam(query, "id")
        if (let Some(s) <- idStr) {
            handleGetNoteById(ctx, s)
        } else {
            respondError(ctx, 400, "Missing id parameter")
        }
    }

    private func handleGetNoteById(ctx: HttpContext, idStr: String): Unit {
        try {
            let id = Int64.parse(idStr)
            if (let Some(note) <- service.getNote(id)) {
                respondJson(ctx, 200, note.toJsonValue().toString())
            } else {
                respondError(ctx, 404, "Note not found")
            }
        } catch (e: Exception) {
            respondError(ctx, 400, "Invalid id parameter")
        }
    }

    private func handleUpdateNote(ctx: HttpContext): Unit {
        try {
            let body = StringReader(ctx.request.body).readToEnd()
            let jv = JsonValue.fromStr(body)
            let obj = jv.asObject()
            let id = obj["id"].asInt().getValue()
            let title = obj["title"].asString().getValue()
            let content = obj["content"].asString().getValue()
            let tags = parseTagsArray(obj["tags"].asArray())
            if (let Some(note) <- service.updateNote(id, title, content, tags)) {
                respondJson(ctx, 200, note.toJsonValue().toString())
            } else {
                respondError(ctx, 404, "Note not found")
            }
        } catch (e: Exception) {
            respondError(ctx, 400, "Invalid request body")
        }
    }

    private func handleDeleteNote(ctx: HttpContext): Unit {
        let query = ctx.request.url.rawQuery ?? ""
        let idStr = getQueryParam(query, "id")
        if (let Some(s) <- idStr) {
            handleDeleteNoteById(ctx, s)
        } else {
            respondError(ctx, 400, "Missing id parameter")
        }
    }

    private func handleDeleteNoteById(ctx: HttpContext, idStr: String): Unit {
        try {
            let id = Int64.parse(idStr)
            if (service.deleteNote(id)) {
                respondJson(ctx, 200, ##"{"success":true}"##)
            } else {
                respondError(ctx, 404, "Note not found")
            }
        } catch (e: Exception) {
            respondError(ctx, 400, "Invalid id parameter")
        }
    }

    // --- Response Helpers ---

    private func respondJson(ctx: HttpContext, status: UInt16, body: String): Unit {
        ctx.responseBuilder
            .status(status)
            .header("Content-Type", "application/json")
            .body(body)
    }

    private func respondError(ctx: HttpContext, status: UInt16, message: String): Unit {
        let errObj = JsonObject()
        errObj.put("error", JsonString(message))
        respondJson(ctx, status, errObj.toString())
    }
}

func getQueryParam(rawQuery: String, name: String): ?String {
    if (rawQuery.isEmpty()) {
        return None
    }
    let pairs = rawQuery.split("&")
    for (pair in pairs) {
        let parts = pair.split("=")
        if (parts.size >= 2 && parts[0] == name) {
            return parts[1]
        }
    }
    return None
}

func parseTagsArray(jsonTags: JsonArray): ArrayList<String> {
    let tags = ArrayList<String>()
    for (i in 0..jsonTags.size()) {
        tags.add(jsonTags[i].asString().getValue())
    }
    return tags
}
