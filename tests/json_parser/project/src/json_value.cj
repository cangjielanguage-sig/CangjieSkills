package json_parser

import std.collection.*

// Custom exception for JSON parsing errors
public class JsonException <: Exception {
    public init(message: String) {
        super(message)
    }
}

// Abstract base class for all JSON values
public abstract class JsonValue <: ToString {
    // Type checking methods
    public open func isNull(): Bool { return false }
    public open func isBool(): Bool { return false }
    public open func isNumber(): Bool { return false }
    public open func isString(): Bool { return false }
    public open func isArray(): Bool { return false }
    public open func isObject(): Bool { return false }

    // Safe type casting methods (throw JsonException if type mismatch)
    public open func asBool(): Bool { throw JsonException("Not a boolean") }
    public open func asNumber(): Float64 { throw JsonException("Not a number") }
    public open func asString(): String { throw JsonException("Not a string") }

    // Parse a JSON string into a JsonValue
    public static func fromString(input: String): JsonValue {
        let parser = JsonParser(input)
        return parser.parse()
    }
}

// JSON null value
public class JsonNull <: JsonValue {
    public init() {}

    public override func isNull(): Bool { return true }

    public func toString(): String { return "null" }
}

// JSON boolean value
public class JsonBool <: JsonValue {
    let _value: Bool

    public init(value: Bool) {
        _value = value
    }

    public override func isBool(): Bool { return true }
    public override func asBool(): Bool { return _value }

    public func toString(): String {
        if (_value) {
            return "true"
        } else {
            return "false"
        }
    }
}

// JSON number value (stored as Float64)
public class JsonNum <: JsonValue {
    let _value: Float64

    public init(value: Float64) {
        _value = value
    }

    public override func isNumber(): Bool { return true }
    public override func asNumber(): Float64 { return _value }

    public func toString(): String {
        let s = "${_value}"
        // If the value is a whole number, remove trailing ".0" for clean JSON output
        if (s.endsWith(".000000")) {
            return s.removeSuffix(".000000")
        }
        return s
    }
}

// JSON string value
public class JsonStr <: JsonValue {
    let _value: String

    public init(value: String) {
        _value = value
    }

    public override func isString(): Bool { return true }
    public override func asString(): String { return _value }

    public func toString(): String {
        return escapeJsonString(_value)
    }
}

// Helper function: escape a string for JSON output
func escapeJsonString(s: String): String {
    let sb = StringBuilder()
    sb.append("\"")
    for (r in s.runes()) {
        if (r == r'"') {
            sb.append("\\\"")
        } else if (r == r'\\') {
            sb.append("\\\\")
        } else if (r == r'\n') {
            sb.append("\\n")
        } else if (r == r'\r') {
            sb.append("\\r")
        } else if (r == r'\t') {
            sb.append("\\t")
        } else {
            sb.append(r)
        }
    }
    sb.append("\"")
    return sb.toString()
}

// JSON array value
public class JsonArr <: JsonValue {
    let _elements: ArrayList<JsonValue> = ArrayList<JsonValue>()

    public init() {}

    public override func isArray(): Bool { return true }

    public func size(): Int64 { return _elements.size }

    public func add(value: JsonValue): Unit {
        _elements.add(value)
    }

    public func get(index: Int64): JsonValue {
        return _elements[index]
    }

    public func toString(): String {
        let sb = StringBuilder()
        sb.append("[")
        for (i in 0.._elements.size) {
            if (i > 0) {
                sb.append(",")
            }
            sb.append(_elements[i].toString())
        }
        sb.append("]")
        return sb.toString()
    }
}

// JSON object value
public class JsonObj <: JsonValue {
    let _keys: ArrayList<String> = ArrayList<String>()
    let _values: ArrayList<JsonValue> = ArrayList<JsonValue>()

    public init() {}

    public override func isObject(): Bool { return true }

    public func size(): Int64 { return _keys.size }

    public func get(key: String): ?JsonValue {
        for (i in 0.._keys.size) {
            if (_keys[i] == key) {
                return _values[i]
            }
        }
        return None
    }

    public func put(key: String, value: JsonValue): Unit {
        for (i in 0.._keys.size) {
            if (_keys[i] == key) {
                _values[i] = value
                return
            }
        }
        _keys.add(key)
        _values.add(value)
    }

    public func containsKey(key: String): Bool {
        for (i in 0.._keys.size) {
            if (_keys[i] == key) {
                return true
            }
        }
        return false
    }

    public func keys(): ArrayList<String> {
        return _keys
    }

    public func toString(): String {
        let sb = StringBuilder()
        sb.append("{")
        for (i in 0.._keys.size) {
            if (i > 0) {
                sb.append(",")
            }
            sb.append(escapeJsonString(_keys[i]))
            sb.append(":")
            sb.append(_values[i].toString())
        }
        sb.append("}")
        return sb.toString()
    }
}
