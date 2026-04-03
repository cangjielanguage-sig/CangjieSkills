## enum HdrMetadataType

```cangjie
public enum HdrMetadataType <: Equatable<HdrMetadataType> & ToString {
    | NONE
    | BASE
    | GAINMAP
    | ALTERNATE
    | ...
}
```

**功能：** [HdrMetadataKey](#enum-hdrmetadatakey)中HDR_METADATA_TYPE关键字对应的值。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**父类型：**

- Equatable\<HdrMetadataType>
- ToString

### ALTERNATE

```cangjie
ALTERNATE
```

**功能：** 表示用于合成后HDR图的元数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### BASE

```cangjie
BASE
```

**功能：** 表示用于基础图的元数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### GAINMAP

```cangjie
GAINMAP
```

**功能：** 表示用于Gainmap图的元数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### NONE

```cangjie
NONE
```

**功能：** 无元数据内容。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### func !=(HdrMetadataType)

```cangjie
public operator func !=(other: HdrMetadataType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[HdrMetadataType](#enum-hdrmetadatatype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(HdrMetadataType)

```cangjie
public operator func ==(other: HdrMetadataType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[HdrMetadataType](#enum-hdrmetadatatype)|是|-|另一个枚举值。|

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