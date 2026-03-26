package mustache

import std.collection.*

// Internal AST node types
abstract class MustacheNode {}

class TextNode <: MustacheNode {
    let _text: String
    init(text: String) {
        _text = text
    }
}

class VariableNode <: MustacheNode {
    let _name: String
    let _escaped: Bool
    init(name: String, escaped: Bool) {
        _name = name
        _escaped = escaped
    }
}

class SectionNode <: MustacheNode {
    let _name: String
    let _inverted: Bool
    let _children: ArrayList<MustacheNode> = ArrayList<MustacheNode>()
    init(name: String, inverted: Bool) {
        _name = name
        _inverted = inverted
    }
}

// HTML escape utility
let SINGLE_QUOTE: Rune = Rune(39)

func htmlEscape(s: String): String {
    let sb = StringBuilder()
    for (r in s.runes()) {
        if (r == r'&') {
            sb.append("&amp;")
        } else if (r == r'<') {
            sb.append("&lt;")
        } else if (r == r'>') {
            sb.append("&gt;")
        } else if (r == r'"') {
            sb.append("&quot;")
        } else if (r == SINGLE_QUOTE) {
            sb.append("&#39;")
        } else {
            sb.append(r)
        }
    }
    return sb.toString()
}

// Template parser (internal)
class TemplateParser {
    let _runes: Array<Rune>
    var _pos: Int64 = 0

    init(template: String) {
        _runes = template.toRuneArray()
    }

    func parse(): ArrayList<MustacheNode> {
        return parseNodes(None)
    }

    func parseNodes(sectionName: ?String): ArrayList<MustacheNode> {
        let nodes = ArrayList<MustacheNode>()
        var textStart = _pos

        while (_pos < _runes.size) {
            if (_pos + 1 < _runes.size && _runes[_pos] == r'{' && _runes[_pos + 1] == r'{') {
                // Flush accumulated text
                if (_pos > textStart) {
                    nodes.add(TextNode(runeSlice(textStart, _pos)))
                }

                _pos += 2

                if (_pos < _runes.size && _runes[_pos] == r'{') {
                    // Triple brace {{{ - unescaped variable
                    _pos++
                    let name = readUntilClose().trimAscii()
                    expectStr("}}}")
                    nodes.add(VariableNode(name, false))
                } else if (_pos < _runes.size && _runes[_pos] == r'!') {
                    // Comment {{! ... }}
                    _pos++
                    readUntilClose()
                    expectStr("}}")
                } else if (_pos < _runes.size && _runes[_pos] == r'#') {
                    // Section start {{# ... }}
                    _pos++
                    let name = readUntilClose().trimAscii()
                    expectStr("}}")
                    let children = parseNodes(name)
                    let section = SectionNode(name, false)
                    section._children.add(all: children)
                    nodes.add(section)
                } else if (_pos < _runes.size && _runes[_pos] == r'^') {
                    // Inverted section {{^ ... }}
                    _pos++
                    let name = readUntilClose().trimAscii()
                    expectStr("}}")
                    let children = parseNodes(name)
                    let section = SectionNode(name, true)
                    section._children.add(all: children)
                    nodes.add(section)
                } else if (_pos < _runes.size && _runes[_pos] == r'/') {
                    // Section end {{/ ... }}
                    _pos++
                    let name = readUntilClose().trimAscii()
                    expectStr("}}")
                    if (let Some(expected) <- sectionName) {
                        if (name != expected) {
                            throw MustacheException("Mismatched section tag: expected '${expected}', found '${name}'")
                        }
                    } else {
                        throw MustacheException("Unexpected closing tag: '${name}'")
                    }
                    return nodes
                } else if (_pos < _runes.size && _runes[_pos] == r'&') {
                    // Unescaped variable {{& ... }}
                    _pos++
                    let name = readUntilClose().trimAscii()
                    expectStr("}}")
                    nodes.add(VariableNode(name, false))
                } else {
                    // Regular escaped variable {{ ... }}
                    let name = readUntilClose().trimAscii()
                    expectStr("}}")
                    nodes.add(VariableNode(name, true))
                }

                textStart = _pos
            } else {
                _pos++
            }
        }

        // Flush remaining text
        if (_pos > textStart) {
            nodes.add(TextNode(runeSlice(textStart, _pos)))
        }

        if (let Some(name) <- sectionName) {
            throw MustacheException("Unclosed section: '${name}'")
        }

        return nodes
    }

    func runeSlice(start: Int64, end: Int64): String {
        let sb = StringBuilder()
        for (i in start..end) {
            sb.append(_runes[i])
        }
        return sb.toString()
    }

    func readUntilClose(): String {
        let sb = StringBuilder()
        while (_pos < _runes.size && _runes[_pos] != r'}') {
            sb.append(_runes[_pos])
            _pos++
        }
        return sb.toString()
    }

    func expectStr(s: String): Unit {
        let runes = s.toRuneArray()
        for (r in runes) {
            if (_pos >= _runes.size || _runes[_pos] != r) {
                throw MustacheException("Expected '${s}'")
            }
            _pos++
        }
    }
}

// Public template class
public class MustacheTemplate {
    let _nodes: ArrayList<MustacheNode>

    init(nodes: ArrayList<MustacheNode>) {
        _nodes = nodes
    }

    public static func fromString(template: String): MustacheTemplate {
        let parser = TemplateParser(template)
        let nodes = parser.parse()
        return MustacheTemplate(nodes)
    }

    public func render(context: MustacheContext): String {
        let sb = StringBuilder()
        let stack = ArrayList<MustacheContext>()
        stack.add(context)
        renderNodes(_nodes, stack, None, sb)
        return sb.toString()
    }

    func renderNodes(nodes: ArrayList<MustacheNode>, stack: ArrayList<MustacheContext>,
                     currentValue: ?MustacheValue, sb: StringBuilder): Unit {
        for (node in nodes) {
            if (let Some(textNode) <- (node as TextNode)) {
                sb.append(textNode._text)
            } else if (let Some(varNode) <- (node as VariableNode)) {
                renderVariable(varNode, stack, currentValue, sb)
            } else if (let Some(secNode) <- (node as SectionNode)) {
                renderSection(secNode, stack, currentValue, sb)
            }
        }
    }

    func renderVariable(node: VariableNode, stack: ArrayList<MustacheContext>,
                        currentValue: ?MustacheValue, sb: StringBuilder): Unit {
        let value: MustacheValue = if (node._name == ".") {
            currentValue ?? MustacheNone()
        } else {
            lookupValue(node._name, stack)
        }

        let text = valueToString(value)
        if (node._escaped) {
            sb.append(htmlEscape(text))
        } else {
            sb.append(text)
        }
    }

    func renderSection(node: SectionNode, stack: ArrayList<MustacheContext>,
                       currentValue: ?MustacheValue, sb: StringBuilder): Unit {
        let value = lookupValue(node._name, stack)
        let falsy = isFalsy(value)

        if (node._inverted) {
            if (falsy) {
                renderNodes(node._children, stack, currentValue, sb)
            }
        } else {
            if (falsy) {
                return
            }

            if (value.isList()) {
                let list = (value as MustacheList).getOrThrow()
                for (i in 0..list.size()) {
                    let item = list.get(i)
                    if (item.isContext()) {
                        let itemCtx = (item as MustacheContext).getOrThrow()
                        stack.add(itemCtx)
                        renderNodes(node._children, stack, item, sb)
                        stack.remove(at: stack.size - 1)
                    } else {
                        renderNodes(node._children, stack, item, sb)
                    }
                }
            } else if (value.isContext()) {
                let ctx = (value as MustacheContext).getOrThrow()
                stack.add(ctx)
                renderNodes(node._children, stack, value, sb)
                stack.remove(at: stack.size - 1)
            } else {
                renderNodes(node._children, stack, value, sb)
            }
        }
    }

    func lookupValue(name: String, stack: ArrayList<MustacheContext>): MustacheValue {
        let parts = name.split(".")
        if (parts.size == 0) {
            return MustacheNone()
        }

        // Find first part in context stack (top to bottom)
        var current: MustacheValue = MustacheNone()
        var found = false
        var i = stack.size - 1
        while (i >= 0) {
            if (let Some(v) <- stack[i].get(parts[0])) {
                current = v
                found = true
                break
            }
            i = i - 1
        }

        if (!found) {
            return MustacheNone()
        }

        // Navigate remaining parts through nested contexts
        for (j in 1..parts.size) {
            if (current.isContext()) {
                let ctx = (current as MustacheContext).getOrThrow()
                if (let Some(v) <- ctx.get(parts[j])) {
                    current = v
                } else {
                    return MustacheNone()
                }
            } else {
                return MustacheNone()
            }
        }

        return current
    }

    func valueToString(value: MustacheValue): String {
        if (value.isString()) {
            return value.asString()
        } else if (value.isBool()) {
            if (value.asBool()) {
                return "true"
            } else {
                return "false"
            }
        } else {
            return ""
        }
    }

    func isFalsy(value: MustacheValue): Bool {
        if (value.isNone()) { return true }
        if (value.isBool() && !value.asBool()) { return true }
        if (value.isList()) {
            let list = (value as MustacheList).getOrThrow()
            return list.size() == 0
        }
        return false
    }
}
