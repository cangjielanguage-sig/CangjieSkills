### class CJImageError

```cangjie
public class CJImageError {
    public var componentWidth: Float64 = 0.0
    public var componentHeight: Float64 = 0.0
    public var message: String = ""

    public init(
        componentWidth: Float64,
        componentHeight: Float64
    )
    public init(
        componentWidth: Float64,
        componentHeight: Float64,
        message: String
    )
    public init()
}
```

**功能：** 图片加载失败类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var componentWidth

```cangjie
public var componentWidth: Float64 = 0.0
```

**功能：** 表示组件的宽度。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var componentHeight

```cangjie
public var componentHeight: Float64 = 0.0
```

**功能：** 表示组件的高度。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var message

```cangjie
public var message: String = ""
```

**功能：** 表示报错信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

#### init(Float64, Float64)

```cangjie
public init(
    componentWidth: Float64,
    componentHeight: Float64
)
```

**功能：** 创建CJImageError。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| componentWidth | Float64 | 是    | -    | 组件的宽度。单位：像素(px)。 |
| componentHeight | Float64  | 是    | -   | 组件的高度。单位：像素(px)。 |

#### init(Float64, Float64, String)

```cangjie
public init(
    componentWidth: Float64,
    componentHeight: Float64,
    message: String
)
```

**功能：** 创建CJImageError。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| componentWidth | Float64 | 是    | -    | 组件的宽度。单位：像素(px)。 |
| componentHeight | Float64  | 是    | -   | 组件的高度。单位：像素(px)。 |
| message | String  | 是    | -   | 报错信息。 |

#### init()

```cangjie
public init()
```

**功能：** 创建CJImageError。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19