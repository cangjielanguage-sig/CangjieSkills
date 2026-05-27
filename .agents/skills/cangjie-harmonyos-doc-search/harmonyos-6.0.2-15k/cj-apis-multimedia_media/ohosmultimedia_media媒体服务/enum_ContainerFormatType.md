## enum ContainerFormatType

```cangjie
public enum ContainerFormatType <: ToString & Equatable<ContainerFormatType> {
    | CFT_MPEG_4
    | CFT_MPEG_4A
    | CFT_MP3
    | CFT_WAV
    | CFT_UNKNOWN
    | ...
}
```

**功能：** 表示容器格式类型的枚举，缩写为CFT。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<ContainerFormatType>

### CFT_MP3

```cangjie
CFT_MP3
```

**功能：** 音频的容器格式，MP3。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### CFT_MPEG_4

```cangjie
CFT_MPEG_4
```

**功能：** 视频的容器格式，MP4。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### CFT_MPEG_4A

```cangjie
CFT_MPEG_4A
```

**功能：** 音频的容器格式，M4A。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### CFT_UNKNOWN

```cangjie
CFT_UNKNOWN
```

**功能：** 未知格式类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### CFT_WAV

```cangjie
CFT_WAV
```

**功能：** 音频的容器格式，WAV。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取容器格式类型的枚举的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|容器格式类型的枚举的字符串表示。|

### func !=(ContainerFormatType)

```cangjie
public operator override func !=(that: ContainerFormatType): Bool
```

**功能：** 对容器格式类型进行判不等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[ContainerFormatType](#enum-containerformattype)|是|-|容器格式类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果容器格式类型不等，返回true，否则返回false。|

### func ==(ContainerFormatType)

```cangjie
public operator override func ==(that: ContainerFormatType): Bool
```

**功能：** 对容器格式类型进行判等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[ContainerFormatType](#enum-containerformattype)|是|-|容器格式类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果容器格式类型相等，返回true，否则返回false。|