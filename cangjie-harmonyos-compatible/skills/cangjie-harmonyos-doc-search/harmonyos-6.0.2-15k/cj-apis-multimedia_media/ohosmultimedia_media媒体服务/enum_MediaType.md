## enum MediaType

```cangjie
public enum MediaType <: ToString & Equatable<MediaType> {
    | MEDIA_TYPE_AUD
    | MEDIA_TYPE_VID
    | MEDIA_TYPE_SUBTITLE
    | ...
}
```

**功能：** 媒体类型枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<MediaType>

### MEDIA_TYPE_AUD

```cangjie
MEDIA_TYPE_AUD
```

**功能：** 表示音频。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### MEDIA_TYPE_SUBTITLE

```cangjie
MEDIA_TYPE_SUBTITLE
```

**功能：** 表示字幕。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### MEDIA_TYPE_VID

```cangjie
MEDIA_TYPE_VID
```

**功能：** 表示视频。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### func !=(MediaType)

```cangjie
public operator func !=(other: MediaType): Bool
```

**功能：** 判断两个MediaType是否不等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MediaType](#enum-mediatype)|是|-|另一MediaType。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个MediaType不等返回false，否则返回true。|

### func ==(MediaType)

```cangjie
public operator func ==(other: MediaType): Bool
```

**功能：** 判断两个MediaType是否相等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MediaType](#enum-mediatype)|是|-|另一MediaType。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个MediaType相等返回false，否则返回true。|

### func get()

```cangjie
public func get(): Int32
```

**功能：** 返回MediaType的值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回MediaType的值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回MediaType的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回MediaType的字符串表示。|