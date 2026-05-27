### class BadgeParams

```cangjie
public class BadgeParams {
    public init(count!: Int32, style!: BadgeStyle, position!: BadgePosition = BadgePosition.RightTop,maxCount!: Int32 = 99)
    public init(value!: String, style!: BadgeStyle, position!: BadgePosition = BadgePosition.RightTop)
}
```

**功能：** 包含创建Badge组件的基础参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Int32, BadgeStyle, BadgePosition, Int32)

```cangjie
public init(count!: Int32, style!: BadgeStyle, position!: BadgePosition = BadgePosition.RightTop,
    maxCount!: Int32 = 99)
```

**功能：** 创建一个BadgeParams对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|count|Int32|是|-| **命名参数。** 设置提醒消息数。小于等于0时不显示信息标记。|
|style|[BadgeStyle](#class-badgestyle)|是|-| **命名参数。** Badge组件可设置的样式，支持设置文本颜色、尺寸、圆点颜色和尺寸。|
|position|[BadgePosition](#enum-badgeposition)|否|BadgePosition.RightTop| **命名参数。** 提示点显示位置。|
|maxCount|Int32|否|99| **命名参数。** 最大消息数，超过最大消息时仅显示 maxCount+。|

#### init(String, BadgeStyle, BadgePosition)

```cangjie
public init(value!: String, style!: BadgeStyle, position!: BadgePosition = BadgePosition.RightTop)
```

**功能：** 创建一个BadgeParams对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-| **命名参数。** 提示内容的文本字符串。|
|style|[BadgeStyle](#class-badgestyle)|是|-| **命名参数。** Badge组件可设置的样式，支持设置文本颜色、尺寸、圆点颜色和尺寸。|
|position|[BadgePosition](#enum-badgeposition)|否|BadgePosition.RightTop| **命名参数。** 提示点显示位置。|