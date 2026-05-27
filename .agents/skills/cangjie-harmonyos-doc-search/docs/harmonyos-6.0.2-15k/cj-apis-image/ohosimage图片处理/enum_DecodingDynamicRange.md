## enum DecodingDynamicRange

```cangjie
public enum DecodingDynamicRange <: Equatable<DecodingDynamicRange> & ToString {
    | AUTO
    | SDR
    | HDR
    | ...
}
```

**功能：** 描述解码时期望的图像动态范围。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**父类型：**

- Equatable\<DecodingDynamicRange>
- ToString

### AUTO

```cangjie
AUTO
```

**功能：** 自适应，根据图片信息处理。即如果图片本身为HDR图片，则会按照HDR内容解码；反之按照SDR内容解码。通过[CreateIncrementalSource](#func-createincrementalsourcearrayuint8-sourceoptions)创建的imagesource会解码为SDR内容。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### HDR

```cangjie
HDR
```

**功能：** 按照高动态范围处理图片。通过[CreateIncrementalSource](#func-createincrementalsourcearrayuint8-sourceoptions)创建的imagesource会解码为SDR内容。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### SDR

```cangjie
SDR
```

**功能：** 按照标准动态范围处理图片。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### func !=(DecodingDynamicRange)

```cangjie
public operator func !=(other: DecodingDynamicRange): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DecodingDynamicRange](#enum-decodingdynamicrange)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(DecodingDynamicRange)

```cangjie
public operator func ==(other: DecodingDynamicRange): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DecodingDynamicRange](#enum-decodingdynamicrange)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|