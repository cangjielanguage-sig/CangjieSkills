## enum SeekMode

```cangjie
public enum SeekMode <: Equatable<SeekMode> & ToString {
    | SEEK_NEXT_SYNC
    | SEEK_PREV_SYNC
    | SEEK_CLOSEST
    | ...
}
```

**功能：** 视频播放的Seek模式枚举，可通过seek方法作为参数传递下去。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**父类型：**

- Equatable\<SeekMode>
- ToString

### SEEK_CLOSEST

```cangjie
SEEK_CLOSEST
```

**功能：** 表示跳转到距离指定时间点最近的帧，建议精准跳转进度的时候用这个枚举值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### SEEK_NEXT_SYNC

```cangjie
SEEK_NEXT_SYNC
```

**功能：** 表示跳转到指定时间点的下一个关键帧，建议向后快进的时候用这个枚举值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### SEEK_PREV_SYNC

```cangjie
SEEK_PREV_SYNC
```

**功能：** 表示跳转到指定时间点的上一个关键帧，建议向前快进的时候用这个枚举值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### func !=(SeekMode)

```cangjie
public operator func !=(other: SeekMode): Bool
```

**功能：** 判断两个SeekMode是否不等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SeekMode](#enum-seekmode)|是|-|另一SeekMode。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个SeekMode不等返回true，否则返回false。|

### func ==(SeekMode)

```cangjie
public operator func ==(other: SeekMode): Bool
```

**功能：** 判断两个SeekMode是否相等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SeekMode](#enum-seekmode)|是|-|另一SeekMode。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个SeekMode相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回SeekMode的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回SeekMode的字符串表示。|