## class PopupButton

```cangjie
public class PopupButton {
    public var value: ?String
    public var action: () -> Unit
    public init(value!: ?String, action!: () -> Unit)
}
```

**功能：** 构建弹窗按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var value

```cangjie
public var value: ?String
```

**功能：** 按钮的文本内容。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var action

```cangjie
public var action: () -> Unit
```

**功能：** 按钮的点击事件。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?String, () -> Unit)

```cangjie
public init(value!: ?String, action!: () -> Unit)
```

**功能：** 构建弹窗按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?String|是|-|**命名参数。** 按钮的文本内容。|
|action|() -> Unit|是|-|**命名参数。** 按钮的点击事件。|

## class PopupStateChangeParam

```cangjie
public class PopupStateChangeParam {
    public var isVisible: Bool
    public init(value: Bool)
}
```

**功能：** 按钮的点击事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var isVisible

```cangjie
public var isVisible: Bool
```

**功能：** 弹窗是否可见。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(Bool)

```cangjie
public init(value: Bool)
```

**功能：** 设置弹窗状态参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|弹窗是否可见。|