## class BorderColor

```cangjie
public class BorderColor {
    public var resourceColor: ResourceColor
    public init(color!: ?ResourceColor = Color.Black)
}
```

**功能：** 定义对话框组件的边框颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var resourceColor

```cangjie
public var resourceColor: ResourceColor
```

**功能：** 边框的颜色资源。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?ResourceColor)

```cangjie
public init(color!: ?ResourceColor = Color.Black)
```

**功能：** BorderColor 构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.Black| **命名参数。** 边框颜色。初始值: Color.Black。|

## enum DialogButtonDirection

```cangjie
public enum DialogButtonDirection <: Equatable<DialogButtonDirection> {
    | Auto
    | Horizontal
    | Vertical
    | ...
}
```

**功能：** 警告弹窗中按钮排列方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[DialogButtonDirection](#enum-dialogbuttondirection)>

### Auto

```cangjie
Auto
```

**功能：** 两个及以下按钮水平排布，两个以上为竖直排布。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Horizontal

```cangjie
Horizontal
```

**功能：** 按钮水平布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Vertical

```cangjie
Vertical
```

**功能：** 按钮竖直布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func !=(DialogButtonDirection)

```cangjie
public operator func !=(other: DialogButtonDirection): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DialogButtonDirection](#enum-dialogbuttondirection)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

### operator func ==(DialogButtonDirection)

```cangjie
public operator func ==(other: DialogButtonDirection): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DialogButtonDirection](#enum-dialogbuttondirection)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|