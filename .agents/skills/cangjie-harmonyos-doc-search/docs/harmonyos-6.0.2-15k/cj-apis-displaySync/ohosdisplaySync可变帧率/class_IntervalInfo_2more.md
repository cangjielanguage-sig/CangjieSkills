## class IntervalInfo

```cangjie
public class IntervalInfo {
    public IntervalInfo (
        public var timestamp: Int64,
        public var targetTimestamp: Int64
    )
}
```

**功能：** 开发者可以从订阅函数中获取帧绘制的时间戳信息，包含当前帧到达的时间timestamp和下一帧预期到达的时间targetTimestamp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var targetTimestamp

```cangjie
public var targetTimestamp: Int64
```

**功能：** 下一帧预期到达的时间（单位：纳秒）。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var timestamp

```cangjie
public var timestamp: Int64
```

**功能：** 当前帧到达的时间（单位：纳秒）。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### IntervalInfo(Int64, Int64)

```cangjie
public IntervalInfo (
    public var timestamp: Int64,
    public var targetTimestamp: Int64
)
```

**功能：** IntervalInfo的主构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timestamp|Int64|是|-|当前帧到达的时间（单位：纳秒）。|
|targetTimestamp|Int64|是|-|下一帧预期到达的时间（单位：纳秒）。|

## enum OnOffType

```cangjie
public enum OnOffType {
    | FRAME
    | ...
}
```

**功能：** 表示事件回调类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### FRAME

```cangjie
FRAME
```

**功能：** 表示注册回调的类型是'frame'。

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将枚举值转换为字符串。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后的字符串。|