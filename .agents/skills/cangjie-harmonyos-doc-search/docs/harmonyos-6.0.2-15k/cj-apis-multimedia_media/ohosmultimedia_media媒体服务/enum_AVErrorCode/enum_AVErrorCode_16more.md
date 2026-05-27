## enum AVErrorCode

```cangjie
public enum AVErrorCode <: ToString & Equatable<AVErrorCode> {
    |AvErrOk
    |AvErrNoPremission
    |AvErrInvalidParameter
    |AvErrUnsupportCapability
    |AvErrNoMemory
    |AvErrOperateNotPermit
    |AvErrIo
    |AvErrTimeout
    |AvErrServiceDied
    |AvErrUnsupportFormat
    |AvErrAudioInterrupted
    | ...
}
```

**功能：** 媒体类型枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**父类型：**

- ToString
- Equatable\<AVErrorCode>

### AvErrOk

```cangjie
AvErrOk
```

**功能：** 表示操作成功。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

### AvErrNoPremission

```cangjie
AvErrNoPremission
```

**功能：** 表示无权限执行此操作。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

### AvErrInvalidParameter

```cangjie
AvErrInvalidParameter
```

**起始版本：** 20

**功能：** 表示传入入参无效。

### AvErrUnsupportCapability

```cangjie
AvErrUnsupportCapability
```

**功能：** 表示当前版本不支持该API能力。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

### AVERR_AvErrNoMemoryOK

```cangjie
AvErrNoMemory
```

**功能：** 表示系统内存不足或服务数量达到上限。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

### AvErrOperateNotPermit

```cangjie
AvErrOperateNotPermit
```

**功能：** 表示当前状态不允许或无权执行此操作。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

### AvErrIo

```cangjie
AvErrIo
```

**功能：** 表示数据流异常信息。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

### AvErrTimeout

```cangjie
AvErrTimeout
```

**功能：** 表示系统或网络响应超时。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

### AvErrServiceDied

```cangjie
AvErrServiceDied
```

**功能：** 表示服务进程死亡。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

### AvErrUnsupportFormat

```cangjie
AvErrUnsupportFormat
```

**功能：** 表示不支持当前媒体资源的格式。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

### AvErrAudioInterrupted

```cangjie
AvErrAudioInterrupted
```

**功能：** 表示音频焦点被抢占。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

### func !=(AVErrorCode)

```cangjie
public operator func !=(other: AVErrorCode): Bool
```

**功能：** 判断两个AVErrorCode是否不等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVErrorCode](#enum-averrorcode)|是|-|另一AVErrorCode。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个AVErrorCode不等返回false，否则返回true。|

### func ==(AVErrorCode)

```cangjie
public operator func ==(other: AVErrorCode): Bool
```

**功能：** 判断两个AVErrorCode是否相等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVErrorCode](#enum-averrorcode)|是|-|另一AVErrorCode。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个averrorCode相等返回false，否则返回true。|

### func get()

```cangjie
public func get(): Int32
```

**功能：** 返回averrorCode的值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回MediaType的值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回averrorCode的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|返回averrorCode的字符串表示。|