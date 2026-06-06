## enum HdrMetadataKey

```cangjie
public enum HdrMetadataKey <: Equatable<HdrMetadataKey> & ToString {
    | HDR_METADATA_TYPE
    | HDR_STATIC_METADATA
    | HDR_DYNAMIC_METADATA
    | HDR_GAINMAP_METADATA
    | ...
}
```

**功能：** [pixelmap](#class-pixelmap)使用的HDR相关元数据信息的关键字。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**父类型：**

- Equatable\<HdrMetadataKey>
- ToString

### HDR_DYNAMIC_METADATA

```cangjie
HDR_DYNAMIC_METADATA
```

**功能：** 动态元数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### HDR_GAINMAP_METADATA

```cangjie
HDR_GAINMAP_METADATA
```

**功能：** Gainmap使用的元数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### HDR_METADATA_TYPE

```cangjie
HDR_METADATA_TYPE
```

**功能：** [pixelmap](#class-pixelmap)使用的元数据类型。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### HDR_STATIC_METADATA

```cangjie
HDR_STATIC_METADATA
```

**功能：** 静态元数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### func !=(HdrMetadataKey)

```cangjie
public operator func !=(other: HdrMetadataKey): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[HdrMetadataKey](#enum-hdrmetadatakey)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(HdrMetadataKey)

```cangjie
public operator func ==(other: HdrMetadataKey): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[HdrMetadataKey](#enum-hdrmetadatakey)|是|-| 另一个枚举值。|

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