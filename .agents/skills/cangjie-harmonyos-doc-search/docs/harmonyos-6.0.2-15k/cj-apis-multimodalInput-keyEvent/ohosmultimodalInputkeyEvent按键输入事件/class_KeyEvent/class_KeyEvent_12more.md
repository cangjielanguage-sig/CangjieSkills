## class KeyEvent

```cangjie
public class KeyEvent <: InputEvent {
    public var action: Action
    public var key: Key
    public var unicodeChar: UInt32
    public var keys: Array<Key>
    public var ctrlKey: Bool
    public var altKey: Bool
    public var shiftKey: Bool
    public var logoKey: Bool
    public var fnKey: Bool
    public var capsLock: Bool
    public var numLock: Bool
    public var scrollLock: Bool
    public init (
        base: InputEvent,
        action: Action,
        key: Key,
        unicodeChar: UInt32,
        keys: Array<Key>,
        ctrlKey: Bool,
        altKey: Bool,
        shiftKey: Bool,
        logoKey: Bool,
        fnKey: Bool,
        capsLock: Bool,
        numLock: Bool,
        scrollLock: Bool
    )
}
```

**功能：** 按键事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

**父类型：**

- [InputEvent](./cj-apis-multimodalInput-inputEvent.md#class-inputevent)

### var action

```cangjie
public var action: Action
```

**功能：** 按键动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** [Action](#enum-action)

**读写能力：** 可读写

**起始版本：** 19

### var key

```cangjie
public var key: Key
```

**功能：** 当前上报的按键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** [Key](#class-key)

**读写能力：** 可读写

**起始版本：** 19

### var unicodeChar

```cangjie
public var unicodeChar: UInt32
```

**功能：** 按键对应的uniCode字符。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var keys

```cangjie
public var keys: Array<Key>
```

**功能：** 当前处于按下状态的按键列表。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Array\<[Key](#class-key)>

**读写能力：** 可读写

**起始版本：** 19

### var ctrlKey

```cangjie
public var ctrlKey: Bool
```

**功能：** 当前ctrlKey是否处于按下状态。true表示处于按下状态，false表示处于抬起状态。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var altKey

```cangjie
public var altKey: Bool
```

**功能：** 当前altKey是否处于按下状态。true表示处于按下状态，false表示处于抬起状态。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var shiftKey

```cangjie
public var shiftKey: Bool
```

**功能：** 当前shiftKey是否处于按下状态。true表示处于按下状态，false表示处于抬起状态。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var logoKey

```cangjie
public var logoKey: Bool
```

**功能：** 当前logoKey是否处于按下状态。true表示处于按下状态，false表示处于抬起状态。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var fnKey

```cangjie
public var fnKey: Bool
```

**功能：** 当前fnKey是否处于按下状态。true表示处于按下状态，false表示处于抬起状态。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var capsLock

```cangjie
public var capsLock: Bool
```

**功能：** 当前capsLock是否处于激活状态。true表示处于激活状态，false表示处于未激活状态。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var numLock

```cangjie
public var numLock: Bool
```

**功能：** 当前numLock是否处于激活状态。true表示处于激活状态，false表示处于未激活状态。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19