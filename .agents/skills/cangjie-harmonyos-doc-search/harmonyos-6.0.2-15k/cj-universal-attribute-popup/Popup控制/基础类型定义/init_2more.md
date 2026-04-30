### init()

```cangjie
public init()
```

**功能：** 构建一个空的PopupOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### class StateChangeEvent

```cangjie
public class StateChangeEvent {
    public StateChangeEvent(public let isVisible: Bool)
}
```

**功能：** 表示显示状态的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### let isVisible

```cangjie
public let isVisible: Bool
```

**功能：** 当前的显示状态。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

#### StateChangeEvent(Bool)

```cangjie
public StateChangeEvent(public let isVisible: Bool)
```

**功能：** 构建一个StateChangeEvent类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isVisible|  Bool | 是 | - | 当前的显示状态。 |