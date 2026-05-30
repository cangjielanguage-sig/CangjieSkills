## enum AVMimeTypes

```cangjie
public enum AVMimeTypes <: ToString & Equatable<AVMimeTypes> {
    | ApplicationM3U8
    | ...
}
```

**功能：** 媒体MIME类型，通过setMimeType设置。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**父类型：**

- ToString
- Equatable\<AVMimeTypes>

### ApplicationM3U8

```cangjie
ApplicationM3U8
```

**功能：** 表示m3u8本地文件。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 20

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取AVMimeTypes类型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|AVMimeTypes类型枚举值的字符串表示。|

### func !=(AVMimeTypes)

```cangjie
public operator override func !=(that: AVMimeTypes): Bool
```

**功能：** 对AVMimeTypes类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[AVMimeTypes](#enum-avmimetypes)|是|-|AVMimeTypes类型枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果AVMimeTypes类型枚举值不等，返回true，否则返回false。|

### func ==(AVMimeTypes)

```cangjie
public operator override func ==(that: CodecMimeType): Bool
```

**功能：** 对AVMimeTypes类型枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[AVMimeTypes](#enum-avmimetypes)|是|-|AVMimeTypes类型枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果Codec MIME类型枚举值相等，返回true，否则返回false。|