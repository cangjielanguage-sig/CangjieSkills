## 组件事件

### func onChange(?(TimePickerResult) -> Unit)

```cangjie
public func onChange(callback: ?(TimePickerResult) -> Unit): This
```

**功能：** 滑动TimePicker后，时间选项归位至选中项位置时，触发该回调。

**系统能力：**  SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?([TimePickerResult](#class-timepickerresult))->Unit|是|-| 24小时制时间。|

## 基础类型定义

### class TimePickerResult

```cangjie
public class TimePickerResult {
    public var hour: Int64
    public var minute: Int64
    public var second: Int64
    public init(hour: Int64, minute: Int64, second: Int64)
}
```

**功能：** 设置24小时制时间。

**系统能力：**  SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var hour

```cangjie
public var hour: Int64
```

**功能：** 设置选中时间的时。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 20

#### var minute

```cangjie
public var minute: Int64
```

**功能：** 设置选中时间的分。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 20

#### var second

```cangjie
public var second: Int64
```

**功能：** 设置选中时间的秒。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 20

#### init(Int64, Int64, Int64)

```cangjie
public init(hour: Int64, minute: Int64, second: Int64)
```

**功能：** 创建一个TimePickerResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hour|Int64|是|-|选中时间的时。<br>取值范围：[0-23]。|
|minute|Int64|是|-| 选中时间的分。<br>取值范围：[0-59]。|
|second|Int64|是|-| 选中时间的秒。<br>取值范围：[0-59]。|

### enum TimePickerFormat

```cangjie
public enum TimePickerFormat {
    HourMinute |
    HourMinuteSecond |
}
```

**功能：** 设置需要显示的时间选择器的格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### HourMinute

```cangjie
HourMinute
```

**功能：** 按照小时和分钟显示。

**起始版本：** 20

#### HourMinuteSecond

```cangjie
HourMinuteSecond
```

**功能：** 按照小时、分钟和秒显示。

**起始版本：** 20