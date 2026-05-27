### class TextClockConfiguration

```cangjie
public class TextClockConfiguration {
    public var timeZoneOffset: Float32
    public var started: Bool
    public var timeValue: Int64
    public init(timeZoneOffset!: Float32, started!: Bool, timeValue!: Int64)
}
```

**功能：** 文本时钟定制类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var started

```cangjie
public var started: Bool
```

**功能：** 指示文本时钟是否启动。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var timeValue

```cangjie
public var timeValue: Int64
```

**功能：** 当前文本时钟时区的UTC秒数。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var timeZoneOffset

```cangjie
public var timeZoneOffset: Float32
```

**功能：** 当前文本时钟时区偏移量。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Float32, Bool, Int64)

```cangjie
public init(timeZoneOffset!: Float32, started!: Bool, timeValue!: Int64)
```

**功能：** 构造一个TextClockConfiguration对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeZoneOffset|Float32|是|-| **命名参数。** 当前文本时钟时区偏移量。|
|started|Bool|是|-| **命名参数。** 指示文本时钟是否启动。<br/>初始值：true，true表示启动文本时钟，false表示关闭文本时钟。|
|timeValue|Int64|是|-| **命名参数。** 当前文本时钟时区的UTC秒数。|

### class TextClockOptions

```cangjie
public class TextClockOptions {
    public var timeZoneOffset: Float32
    public var controller: TextClockController
    public init(timeZoneOffset!: Float32, controller!: TextClockController)
}
```

**功能：** 通过文本显示当前系统时间的组件参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var controller

```cangjie
public var controller: TextClockController
```

**功能：** 绑定一个控制器，用来控制文本时钟的状态。

**类型：** [TextClockController](#class-textclockcontroller)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var timeZoneOffset

```cangjie
public var timeZoneOffset: Float32
```

**功能：** 当前文本时钟时区偏移量。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Float32, TextClockController)

```cangjie
public init(timeZoneOffset!: Float32, controller!: TextClockController)
```

**功能：** 构造一个TextClockOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeZoneOffset|Float32|是|-| **命名参数。** 当前文本时钟时区偏移量。|
|controller|[TextClockController](#class-textclockcontroller)|是|-| **命名参数。** 绑定一个控制器，用来控制文本时钟的状态。|