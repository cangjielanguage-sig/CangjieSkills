package notebook

import stdx.net.http.*
import stdx.net.tls.*
import stdx.crypto.x509.X509Certificate
import std.io.*
import std.fs.*

main(): Int64 {
    // Load TLS certificates
    let certPem = String.fromUtf8(readToEnd(File("./certs/server.crt", Read)))
    let keyPem = String.fromUtf8(readToEnd(File("./certs/server.key", Read)))
    let caPem = String.fromUtf8(readToEnd(File("./certs/ca.crt", Read)))

    // Start HTTPS server
    let service = NoteService()
    let server = NoteServer(service)
    server.startTls("127.0.0.1", 0, certPem, keyPem)
    let port = server.getPort()
    let baseUrl = "https://127.0.0.1:${port}"
    println("HTTPS server started on port ${port}")

    // Create HTTPS client (trust our CA)
    var tlsConfig = TlsClientConfig()
    tlsConfig.verifyMode = CustomCA(X509Certificate.decodeFromPem(caPem))
    let client = ClientBuilder().tlsConfig(tlsConfig).build()

    // Create a note
    let createBody = ##"{"title":"Hello Cangjie","content":"Welcome to Cangjie HTTPS web programming!","tags":["cangjie","tutorial"]}"##
    let createResp = client.post("${baseUrl}/api/notes", createBody)
    let createResult = StringReader(createResp.body).readToEnd()
    println("Created: ${createResult}")

    // Create another note
    let createBody2 = ##"{"title":"Learning Notes","content":"Studying stdx.net.http and stdx.encoding.json over TLS","tags":["cangjie","study"]}"##
    let createResp2 = client.post("${baseUrl}/api/notes", createBody2)
    let createResult2 = StringReader(createResp2.body).readToEnd()
    println("Created: ${createResult2}")

    // List all notes
    let listResp = client.get("${baseUrl}/api/notes")
    let listResult = StringReader(listResp.body).readToEnd()
    println("All notes: ${listResult}")

    // Filter by tag
    let filterResp = client.get("${baseUrl}/api/notes?tag=study")
    let filterResult = StringReader(filterResp.body).readToEnd()
    println("Notes with 'study' tag: ${filterResult}")

    // Get statistics
    let statsResp = client.get("${baseUrl}/api/stats")
    let statsResult = StringReader(statsResp.body).readToEnd()
    println("Stats: ${statsResult}")

    client.close()
    server.stop()
    return 0
}