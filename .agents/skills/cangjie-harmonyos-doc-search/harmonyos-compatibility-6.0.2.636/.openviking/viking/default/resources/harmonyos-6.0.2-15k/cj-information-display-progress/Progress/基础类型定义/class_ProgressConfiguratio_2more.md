### class ProgressConfiguration

```cangjie
public class ProgressConfiguration {
    public var value: Float32
    public var total: Float32
    public init(value: Float32, total: Float32)
}
```

**功能：** Progress的进度总长和进度值参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var total

```cangjie
public var total: Float32
```

**功能：** 进度总长。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var value

```cangjie
public var value: Float32
```

**功能：** 当前进度值。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Float32, Float32)

```cangjie
public init(value: Float32, total: Float32)
```

**功能：** 创建一个ProgressConfiguration对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float32|是|-|当前进度值。|
|total|Float32|是|-|进度总长。|

### class ProgressOptions

```cangjie
public class ProgressOptions {
    public var value: Float64
    public var total: Float64
    public var progressType: ProgressType
    public init(value!: Float64, total!: Float64 = 100.0, progressType!: ProgressType = ProgressType.Linear)
}
```

**功能：** 属性的进度条组件参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var progressType

```cangjie
public var progressType: ProgressType
```

**功能：** 指定进度条类型。

**类型：** [ProgressType](./cj-common-types.md#enum-progresstype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var total

```cangjie
public var total: Float64
```

**功能：** 指定进度总长。设置小于等于0的数值时置为100。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var value

```cangjie
public var value: Float64
```

**功能：** 指定当前进度值。设置小于0的数值时置为0，设置大于total的数值时置为total。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Float64, Float64, ProgressType)

```cangjie
public init(value!: Float64, total!: Float64 = 100.0, progressType!: ProgressType = ProgressType.Linear)
```

**功能：** 创建一个ProgressOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-| **命名参数。** 指定当前进度值。设置小于0的数值时置为0.0，设置大于total的数值时置为total。|
|total|Float64|否|100.0| **命名参数。** 指定进度总长。设置小于等于0的数值时置为100.0。|
|progressType|[ProgressType](./cj-common-types.md#enum-progresstype)|否|ProgressType.Linear| **命名参数。** 指定进度条类型。|