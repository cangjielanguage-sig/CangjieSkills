## enum HdrType

```cangjie
public enum HdrType <: ToString & Equatable<HdrType> {
    | AV_HDR_TYPE_NONE
    | AV_HDR_TYPE_VIVID
    | ...
}
```

**功能：** 表示视频HDR类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<HdrType>

### AV_HDR_TYPE_NONE

```cangjie
AV_HDR_TYPE_NONE
```

**功能：** 表示无HDR类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### AV_HDR_TYPE_VIVID

```cangjie
AV_HDR_TYPE_VIVID
```

**功能：** 表示为HDR VIVID类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回HdrType的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|HdrType的字符串表示。|

### func !=(HdrType)

```cangjie
public operator override func !=(that: HdrType): Bool
```

**功能：** 比较两个HdrType是否不等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[HdrType](#enum-hdrtype)|是|-|另一HdrType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个HdrType不等返回true，否则返回false。|

### func ==(HdrType)

```cangjie
public operator override func ==(that: HdrType): Bool
```

**功能：** 比较两个HdrType是否相等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[HdrType](#enum-hdrtype)|是|-|另一HdrType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个HdrType相等返回true，否则返回false。|