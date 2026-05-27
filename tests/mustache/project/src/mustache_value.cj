package mustache

import std.collection.*

// Custom exception for Mustache template errors
public class MustacheException <: Exception {
    public init(message: String) {
        super(message)
    }
}

// Abstract base class for all Mustache values
public abstract class MustacheValue {
    // Type checking methods
    public open func isNone(): Bool { return false }
    public open func isBool(): Bool { return false }
    public open func isString(): Bool { return false }
    public open func isList(): Bool { return false }
    public open func isContext(): Bool { return false }

    // Safe type casting methods (throw MustacheException if type mismatch)
    public open func asBool(): Bool { throw MustacheException("Not a boolean value") }
    public open func asString(): String { throw MustacheException("Not a string value") }
}

// Represents a missing or undefined value
public class MustacheNone <: MustacheValue {
    public init() {}

    public override func isNone(): Bool { return true }
}

// Boolean value
public class MustacheBool <: MustacheValue {
    let _value: Bool

    public init(value: Bool) {
        _value = value
    }

    public override func isBool(): Bool { return true }
    public override func asBool(): Bool { return _value }
}

// String value
public class MustacheStr <: MustacheValue {
    let _value: String

    public init(value: String) {
        _value = value
    }

    public override func isString(): Bool { return true }
    public override func asString(): String { return _value }
}

// List of values (for iteration in sections)
public class MustacheList <: MustacheValue {
    let _items: ArrayList<MustacheValue> = ArrayList<MustacheValue>()

    public init() {}

    public override func isList(): Bool { return true }

    public func size(): Int64 { return _items.size }

    public func add(value: MustacheValue): Unit {
        _items.add(value)
    }

    public func get(index: Int64): MustacheValue {
        return _items[index]
    }
}

// Context (key-value map for template rendering)
public class MustacheContext <: MustacheValue {
    let _keys: ArrayList<String> = ArrayList<String>()
    let _values: ArrayList<MustacheValue> = ArrayList<MustacheValue>()

    public init() {}

    public override func isContext(): Bool { return true }

    public func get(key: String): ?MustacheValue {
        for (i in 0.._keys.size) {
            if (_keys[i] == key) {
                return _values[i]
            }
        }
        return None
    }

    public func put(key: String, value: MustacheValue): Unit {
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
}
