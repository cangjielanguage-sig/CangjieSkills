package json_parser

main(): Int64 {
    // Demo: parse a JSON string
    let jsonStr = ##"{"name":"Alice","age":30,"active":true,"scores":[90,85,95],"address":null}"##
    let value = JsonValue.fromString(jsonStr)
    println("Parsed JSON:")
    println(value.toString())
    return 0
}