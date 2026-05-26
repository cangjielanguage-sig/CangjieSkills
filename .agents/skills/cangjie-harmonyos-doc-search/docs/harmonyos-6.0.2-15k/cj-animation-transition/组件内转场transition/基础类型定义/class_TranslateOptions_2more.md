### class TranslateOptions

```cangjie
public class TranslateOptions {
    public var x: Length
    public var y: Length
    public var z: Length
    public init(
        x!: Length = 0.0.vp,
        y!: Length = 0.0.vp,
        z!: Length = 0.0.vp
    )
}
```

**功能：** 设置平移参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var x

```cangjie
public var x: Length
```

**功能：** 表示x轴的平移距离。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var y

```cangjie
public var y: Length
```

**功能：** 表示y轴的平移距离。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var z

```cangjie
public var z: Length
```

**功能：** 表示z轴的平移距离。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Length, Length, Length)

```cangjie
public init(
    x!: Length = 0.0.vp,
    y!: Length = 0.0.vp,
    z!: Length = 0.0.vp
)
```

**功能：** TranslateOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](./cj-common-types.md#interface-length)|否|0.0.vp| **命名参数。** x轴的平移距离。<br>单位为vp。<br>取值范围 (-∞, +∞)|
|y|[Length](./cj-common-types.md#interface-length)|否|0.0.vp| **命名参数。** y轴的平移距离。<br>单位为vp。<br>取值范围 (-∞, +∞)|
|z|[Length](./cj-common-types.md#interface-length)|否|0.0.vp| **命名参数。** z轴的平移距离。<br>单位为vp。<br>取值范围 (-∞, +∞)|

### enum TransitionEdge

```cangjie
public enum TransitionEdge {
    | TOP
    | BOTTOM
    | START
    | END
}
```

**功能：** 窗口的边缘信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### BOTTOM

```cangjie
BOTTOM
```

**功能：** 设置窗口的下边缘。

**起始版本：** 12

#### END

```cangjie
END
```

**功能：** 设置窗口的终止边缘，LTR时为右边缘，RTL时为左边缘。

**起始版本：** 12

#### START

```cangjie
START
```

**功能：** 设置窗口的起始边缘，LTR时为左边缘，RTL时为右边缘。

**起始版本：** 12

#### TOP

```cangjie
TOP
```

**功能：** 设置窗口的上边缘。

**起始版本：** 12