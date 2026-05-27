package json_parser

import std.convert.*

// Recursive descent JSON parser
public class JsonParser {
    let _input: Array<Rune>
    var _pos: Int64 = 0
    let _length: Int64

    public init(text: String) {
        _input = text.toRuneArray()
        _length = _input.size
    }

    // Parse the input string into a JsonValue
    public func parse(): JsonValue {
        let value = parseValue()
        skipWhitespace()
        if (_pos < _length) {
            throw JsonException("Unexpected character at position ${_pos}")
        }
        return value
    }

    // Skip whitespace characters (space, tab, newline, carriage return)
    func skipWhitespace(): Unit {
        while (_pos < _length) {
            let c = _input[_pos]
            if (c == r' ' || c == r'\t' || c == r'\n' || c == r'\r') {
                _pos++
            } else {
                break
            }
        }
    }

    // Peek at the current character without advancing
    func peek(): Rune {
        if (_pos >= _length) {
            throw JsonException("Unexpected end of input")
        }
        return _input[_pos]
    }

    // Advance and return the current character
    func advance(): Rune {
        let c = peek()
        _pos++
        return c
    }

    // Expect a specific character, throw if not found
    func expect(expected: Rune): Unit {
        let actual = advance()
        if (actual != expected) {
            throw JsonException("Expected '${expected}' but found '${actual}' at position ${_pos - 1}")
        }
    }

    // Parse a JSON value (dispatch to specific parsers)
    func parseValue(): JsonValue {
        skipWhitespace()
        if (_pos >= _length) {
            throw JsonException("Unexpected end of input")
        }
        let c = _input[_pos]
        if (c == r'"') {
            return parseString()
        } else if (c == r'{') {
            return parseObject()
        } else if (c == r'[') {
            return parseArray()
        } else if (c == r't') {
            return parseTrue()
        } else if (c == r'f') {
            return parseFalse()
        } else if (c == r'n') {
            return parseNull()
        } else if (c == r'-' || (c >= r'0' && c <= r'9')) {
            return parseNumber()
        } else {
            throw JsonException("Unexpected character '${c}' at position ${_pos}")
        }
    }

    // Parse a JSON string value
    func parseString(): JsonStr {
        expect(r'"')
        let sb = StringBuilder()
        while (_pos < _length) {
            let c = _input[_pos]
            _pos++
            if (c == r'"') {
                return JsonStr(sb.toString())
            } else if (c == r'\\') {
                if (_pos >= _length) {
                    throw JsonException("Unterminated string escape")
                }
                let escaped = _input[_pos]
                _pos++
                if (escaped == r'"') {
                    sb.append(r'"')
                } else if (escaped == r'\\') {
                    sb.append(r'\\')
                } else if (escaped == r'/') {
                    sb.append(r'/')
                } else if (escaped == r'n') {
                    sb.append(r'\n')
                } else if (escaped == r'r') {
                    sb.append(r'\r')
                } else if (escaped == r't') {
                    sb.append(r'\t')
                } else if (escaped == r'b') {
                    sb.append(Rune(8))
                } else if (escaped == r'f') {
                    sb.append(Rune(12))
                } else if (escaped == r'u') {
                    let cp = parseUnicodeEscape()
                    sb.append(cp)
                } else {
                    throw JsonException("Invalid escape sequence '\\${escaped}'")
                }
            } else {
                sb.append(c)
            }
        }
        throw JsonException("Unterminated string")
    }

    // Parse a 4-digit unicode escape sequence (\uXXXX)
    func parseUnicodeEscape(): Rune {
        if (_pos + 4 > _length) {
            throw JsonException("Incomplete unicode escape at position ${_pos}")
        }
        var codePoint: UInt32 = 0
        for (_ in 0..4) {
            let c = _input[_pos]
            _pos++
            let digit: UInt32 = if (c >= r'0' && c <= r'9') {
                UInt32(c) - UInt32(r'0')
            } else if (c >= r'a' && c <= r'f') {
                UInt32(c) - UInt32(r'a') + 10
            } else if (c >= r'A' && c <= r'F') {
                UInt32(c) - UInt32(r'A') + 10
            } else {
                throw JsonException("Invalid hex digit '${c}' in unicode escape at position ${_pos - 1}")
            }
            codePoint = codePoint * 16 + digit
        }
        return Rune(codePoint)
    }

    // Parse a JSON number
    func parseNumber(): JsonNum {
        let start = _pos

        // Optional negative sign
        if (_pos < _length && _input[_pos] == r'-') {
            _pos++
        }

        // Integer part
        if (_pos < _length && _input[_pos] == r'0') {
            _pos++
        } else if (_pos < _length && _input[_pos] >= r'1' && _input[_pos] <= r'9') {
            while (_pos < _length && _input[_pos] >= r'0' && _input[_pos] <= r'9') {
                _pos++
            }
        } else {
            throw JsonException("Invalid number at position ${_pos}")
        }

        // Fractional part
        if (_pos < _length && _input[_pos] == r'.') {
            _pos++
            if (_pos >= _length || _input[_pos] < r'0' || _input[_pos] > r'9') {
                throw JsonException("Invalid number: expected digit after decimal point at position ${_pos}")
            }
            while (_pos < _length && _input[_pos] >= r'0' && _input[_pos] <= r'9') {
                _pos++
            }
        }

        // Exponent part
        if (_pos < _length && (_input[_pos] == r'e' || _input[_pos] == r'E')) {
            _pos++
            if (_pos < _length && (_input[_pos] == r'+' || _input[_pos] == r'-')) {
                _pos++
            }
            if (_pos >= _length || _input[_pos] < r'0' || _input[_pos] > r'9') {
                throw JsonException("Invalid number: expected digit in exponent at position ${_pos}")
            }
            while (_pos < _length && _input[_pos] >= r'0' && _input[_pos] <= r'9') {
                _pos++
            }
        }

        // Build the number string from rune array slice
        let numSb = StringBuilder()
        for (i in start.._pos) {
            numSb.append(_input[i])
        }
        let numStr = numSb.toString()
        let value = Float64.parse(numStr)
        return JsonNum(value)
    }

    // Parse JSON true
    func parseTrue(): JsonBool {
        expectKeyword("true")
        return JsonBool(true)
    }

    // Parse JSON false
    func parseFalse(): JsonBool {
        expectKeyword("false")
        return JsonBool(false)
    }

    // Parse JSON null
    func parseNull(): JsonNull {
        expectKeyword("null")
        return JsonNull()
    }

    // Expect a specific keyword
    func expectKeyword(keyword: String): Unit {
        let keyRunes = keyword.toRuneArray()
        for (i in 0..keyRunes.size) {
            if (_pos >= _length) {
                throw JsonException("Unexpected end of input, expected '${keyword}'")
            }
            if (_input[_pos] != keyRunes[i]) {
                throw JsonException("Expected '${keyword}' at position ${_pos}")
            }
            _pos++
        }
    }

    // Parse a JSON array
    func parseArray(): JsonArr {
        expect(r'[')
        let arr = JsonArr()
        skipWhitespace()

        // Check for empty array
        if (_pos < _length && _input[_pos] == r']') {
            _pos++
            return arr
        }

        // Parse elements
        while (true) {
            let value = parseValue()
            arr.add(value)
            skipWhitespace()
            if (_pos >= _length) {
                throw JsonException("Unterminated array")
            }
            if (_input[_pos] == r']') {
                _pos++
                return arr
            }
            expect(r',')
        }
        throw JsonException("Unterminated array")
    }

    // Parse a JSON object
    func parseObject(): JsonObj {
        expect(r'{')
        let obj = JsonObj()
        skipWhitespace()

        // Check for empty object
        if (_pos < _length && _input[_pos] == r'}') {
            _pos++
            return obj
        }

        // Parse key-value pairs
        while (true) {
            skipWhitespace()
            if (_pos >= _length || _input[_pos] != r'"') {
                throw JsonException("Expected string key at position ${_pos}")
            }
            let key = parseString()
            skipWhitespace()
            expect(r':')
            let value = parseValue()
            obj.put(key.asString(), value)
            skipWhitespace()
            if (_pos >= _length) {
                throw JsonException("Unterminated object")
            }
            if (_input[_pos] == r'}') {
                _pos++
                return obj
            }
            expect(r',')
        }
        throw JsonException("Unterminated object")
    }
}
