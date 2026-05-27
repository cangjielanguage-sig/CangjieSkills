## enum BufferingInfoType

```cangjie
public enum BufferingInfoType <: Equatable<BufferingInfoType> & ToString {
    | BUFFERING_START
    | BUFFERING_END
    | BUFFERING_PERCENT
    | CACHED_DURATION
    | ...
}
```

**功能：** 缓存事件类型枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**父类型：**

- Equatable\<BufferingInfoType>
- ToString

### BUFFERING_END

```cangjie
BUFFERING_END
```

**功能：** 表示结束缓冲。当上报BUFFERING_END时，播放器会恢复播放。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### BUFFERING_PERCENT

```cangjie
BUFFERING_PERCENT
```

**功能：** 表示缓冲百分比。可参考该事件感知缓冲进度。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### BUFFERING_START

```cangjie
BUFFERING_START
```

**功能：** 表示开始缓冲。当上报BUFFERING_START时，播放器会暂停播放。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### CACHED_DURATION

```cangjie
CACHED_DURATION
```

**功能：** 表示已缓冲数据预估可播放时长，单位为毫秒（ms）。缓冲区中的数据变化量大于500ms，上报一次。可参考该事件做进度条。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### func !=(BufferingInfoType)

```cangjie
public operator func !=(other: BufferingInfoType): Bool
```

**功能：** 判断两个BufferingInfoType是否不等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BufferingInfoType](#enum-bufferinginfotype)|是|-|另一BufferingInfoType。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个BufferingInfoType不等返回true，否则返回false。|

### func ==(BufferingInfoType)

```cangjie
public operator func ==(other: BufferingInfoType): Bool
```

**功能：** 判断两个BufferingInfoType是否相等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BufferingInfoType](#enum-bufferinginfotype)|是|-|另一BufferingInfoType。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个BufferingInfoType相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回BufferingInfoType的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回BufferingInfoType的字符串表示。|