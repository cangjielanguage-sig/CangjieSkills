## enum VideoCodecType

```cangjie
public enum VideoCodecType {
    | Avc
    | Hevc
    | ...
}
```

**功能：** 枚举，视频编码类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<VideoCodecType>
- ToString

### Avc

```cangjie
Avc
```

**功能：** 视频编码类型AVC。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### Hevc

```cangjie
Hevc
```

**功能：** 视频编码类型HEVC。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(VideoCodecType)

```cangjie
public operator func !=(other: VideoCodecType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[VideoCodecType](#enum-videocodectype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(VideoCodecType)

```cangjie
public operator func ==(other: VideoCodecType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[VideoCodecType](#enum-videocodectype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的字符串值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串值。|