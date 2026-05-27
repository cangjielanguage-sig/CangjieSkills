## class SubtitleInfo

```cangjie
public class SubtitleInfo <: Equatable<SubtitleInfo> & ToString {
    public SubtitleInfo (
        public var duration!: Int32 = -1,
        public var startTime!: Int32 = -1,
        public var text!: String = ""
    )
}
```

**功能：** 外挂字幕信息，使用场景：订阅外挂字幕事件，回调返回外挂字幕详细信息。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**父类型：**

- Equatable\<SubtitleInfo>
- ToString

### var duration

```cangjie
public var duration: Int32 = -1
```

**功能：** 显示当前字幕文本的持续时间（单位：毫秒）。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var startTime

```cangjie
public var startTime: Int32 = -1
```

**功能：** 显示当前字幕文本的开始时间（单位：毫秒）。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var text

```cangjie
public var text: String = ""
```

**功能：** 字幕文本信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### SubtitleInfo(Int32, Int32, String)

```cangjie
public SubtitleInfo (
    public var duration!: Int32 = -1,
    public var startTime!: Int32 = -1,
    public var text!: String = ""
)
```

**功能：** 构造音视频文件资源描述类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|Int32|否|- 1| **命名参数。** 字幕文本信息。|
|startTime|Int32|否|- 1| **命名参数。** 显示当前字幕文本的开始时间（单位：毫秒）。|
|text|String|否|""| **命名参数。** 显示当前字幕文本的持续时间（单位：毫秒）。|

### func !=(SubtitleInfo)

```cangjie
public operator func !=(other: SubtitleInfo): Bool
```

**功能：** 判断两个SubtitleInfo是否不等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SubtitleInfo](#class-subtitleinfo)|是|-|另一SubtitleInfo。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个SubtitleInfo不等返回true，否则返回false。|

### func ==(SubtitleInfo)

```cangjie
public operator func ==(other: SubtitleInfo): Bool
```

**功能：** 判断两个SubtitleInfo是否相等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SubtitleInfo](#class-subtitleinfo)|是|-|另一SubtitleInfo。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个SubtitleInfo相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回SubtitleInfo的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回SubtitleInfo的字符串表示。|