### var scrollLock

```cangjie
public var scrollLock: Bool
```

**功能：** 当前scrollLock是否处于激活状态。true表示处于激活状态，false表示处于未激活状态。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### init(InputEvent, Action, Key, UInt32, Array\<Key>, Bool, Bool, Bool, Bool, Bool, Bool, Bool, Bool)

```cangjie
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
```

**功能：** KeyEvent的构造函数。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|base|[InputEvent](./cj-apis-multimodalInput-inputEvent.md#class-inputevent)|是|-|父类构造信息。|
|action|[Action](../BasicServicesKit/cj-apis-request-agent.md#enum-action)|是|-|按键动作。|
|key|[Key](#class-key)|是|-|当前上报的按键。|
|unicodeChar|UInt32|是|-|按键对应的uniCode字符。|
|keys|Array\<[Key](#class-key)>|是|-|当前处于按下状态的按键列表。|
|ctrlKey|Bool|是|-|当前ctrlKey是否处于按下状态。true表示处于按下状态，false表示处于抬起状态。|
|altKey|Bool|是|-|当前altKey是否处于按下状态。true表示处于按下状态，false表示处于抬起状态。|
|shiftKey|Bool|是|-|当前shiftKey是否处于按下状态。true表示处于按下状态，false表示处于抬起状态。|
|logoKey|Bool|是|-|当前logoKey是否处于按下状态。true表示处于按下状态，false表示处于抬起状态。|
|fnKey|Bool|是|-|当前fnKey是否处于按下状态。true表示处于按下状态，false表示处于抬起状态。|
|capsLock|Bool|是|-|当前capsLock是否处于激活状态。true表示处于激活状态，false表示处于未激活状态。|
|numLock|Bool|是|-|当前numLock是否处于激活状态。true表示处于激活状态，false表示处于未激活状态。|
|scrollLock|Bool|是|-|当前scrollLock是否处于激活状态。true表示处于激活状态，false表示处于未激活状态。|