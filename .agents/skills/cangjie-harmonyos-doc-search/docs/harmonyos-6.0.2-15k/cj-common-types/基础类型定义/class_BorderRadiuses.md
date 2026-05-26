## class BorderRadiuses

```cangjie
public class BorderRadiuses {
    public var topLeft: Length
    public var topRight: Length
    public var bottomLeft: Length
    public var bottomRight: Length
    public init(topLeft!: Length = 0.vp, topRight!: Length = 0.vp, bottomLeft!: Length = 0.vp, bottomRight!: Length = 0.vp)
 }
```

**功能：** 圆角类型，用于描述组件边框圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var bottomLeft

```cangjie
public var bottomLeft: Length
```

**功能：** 组件左下角圆角半径。

**类型：** [Length](#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var bottomRight

```cangjie
public var bottomRight: Length
```

**功能：** 组件右下角圆角半径。

**类型：** [Length](#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var topLeft

```cangjie
public var topLeft: Length
```

**功能：** 组件左上角圆角半径。

**类型：** [Length](#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var topRight

```cangjie
public var topRight: Length
```

**功能：** 组件右上角圆角半径。

**类型：** [Length](#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(Length, Length, Length, Length)

```cangjie
public init(topLeft!: Length = 0.vp, topRight!: Length = 0.vp, bottomLeft!: Length = 0.vp, bottomRight!: Length = 0.vp)
```

**功能：** 初始化一个BorderRadiuses对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| topLeft     | [Length](#interface-length) | 否   | 0.vp   | **命名参数。**  组件左上角圆角半径。 |
| topRight    | [Length](#interface-length) | 否   | 0.vp   | **命名参数。**  组件右上角圆角半径。 |
| bottomLeft  | [Length](#interface-length) | 否   | 0.vp   | **命名参数。**  组件左下角圆角半径。 |
| bottomRight | [Length](#interface-length) | 否   | 0.vp   | **命名参数。**  组件右下角圆角半径。 |