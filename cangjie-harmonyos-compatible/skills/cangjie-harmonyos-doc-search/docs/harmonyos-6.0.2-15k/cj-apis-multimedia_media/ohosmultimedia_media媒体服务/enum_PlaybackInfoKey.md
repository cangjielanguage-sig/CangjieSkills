## enum PlaybackInfoKey

```cangjie
public enum PlaybackInfoKey <: ToString & Hashable & Equatable<PlaybackInfoKey> {
    | SERVER_IP_ADDRESS
    | AVG_DOWNLOAD_RATE
    | DOWNLOAD_RATE
    | IS_DOWNLOADING
    | BUFFER_DURATION
    | ...
}
```

**功能：** 播放信息描述枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**父类型：**

- ToString
- Hashable
- Equatable\<PlaybackInfoKey>

### AVG_DOWNLOAD_RATE

```cangjie
AVG_DOWNLOAD_RATE
```

**功能：** 表示平均下载速率，其对应键值类型为Int32，单位为比特率（bps）。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### BUFFER_DURATION

```cangjie
BUFFER_DURATION
```

**功能：** 表示缓存数据的可播放时长，其对应键值类型为Int64，单位为秒（s）。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### DOWNLOAD_RATE

```cangjie
DOWNLOAD_RATE
```

**功能：** 表示1s的下载速率，其对应键值类型为Int64，单位为比特率（bps）。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### IS_DOWNLOADING

```cangjie
IS_DOWNLOADING
```

**功能：** 表示下载状态，1表示在下载状态，0表示非下载状态（下载完成），其对应键值类型为Int32。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### SERVER_IP_ADDRESS

```cangjie
SERVER_IP_ADDRESS
```

**功能：** 表示服务器IP地址，其对应键值类型为String。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### func !=(PlaybackInfoKey)

```cangjie
public operator func !=(other: PlaybackInfoKey): Bool
```

**功能：** 判断两个PlaybackInfoKey是否不等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlaybackInfoKey](#enum-playbackinfokey)|是|-|另一PlaybackInfoKey。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个PlaybackInfoKey不等返回true，否则返回false。|

### func ==(PlaybackInfoKey)

```cangjie
public operator func ==(other: PlaybackInfoKey): Bool
```

**功能：** 判断两个PlaybackInfoKey是否相等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlaybackInfoKey](#enum-playbackinfokey)|是|-|另一PlaybackInfoKey。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个PlaybackInfoKey相等返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 返回PlaybackInfoKey哈希值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回PlaybackInfoKey哈希值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回PlaybackInfoKey的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回PlaybackInfoKey的字符串表示。|