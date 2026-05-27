## class ButtonInfo

```cangjie
public class ButtonInfo {
    public let text: String
    public let color: UInt32
    public let primary: Bool
    public init(text: String, color: UInt32, primary!: Bool = false)
    public init(text: String, color: Color, primary!: Bool = false)
}
```

**功能：** 菜单中的菜单项按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let color

```cangjie
public let color: UInt32
```

**功能：** 表示按钮文本颜色。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let primary

```cangjie
public let primary: Bool
```

**功能：** 表示在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let text

```cangjie
public let text: String
```

**功能：** 表示按钮文本内容。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(String, UInt32, Bool)

```cangjie
public init(text: String, color: UInt32, primary!: Bool = false)
```

**功能：** 构造ButtonInfo对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|按钮文本内容。|
|color|UInt32|是|-|按钮文本颜色。|
|primary|Bool|否|false| **命名参数。** 在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。|

### init(String, Color, Bool)

```cangjie
public init(text: String, color: Color, primary!: Bool = false)
```

**功能：** 构造ButtonInfo对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|按钮文本内容。|
|color|[Color](./cj-common-types.md#class-color)|是|-|按钮文本颜色。|
|primary|Bool|否|false| **命名参数。** 在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。|