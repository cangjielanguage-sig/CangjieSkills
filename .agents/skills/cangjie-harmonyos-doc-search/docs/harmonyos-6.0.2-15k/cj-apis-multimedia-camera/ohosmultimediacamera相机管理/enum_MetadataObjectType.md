## enum MetadataObjectType

```cangjie
public enum MetadataObjectType <: Equatable<MetadataObjectType> & ToString {
    | FACE_DETECTION
    | UNKNOWN
    | ...
}
```

**功能：** metadata流。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<MetadataObjectType>
- ToString

### FACE_DETECTION

```cangjie
FACE_DETECTION
```

**功能：** metadata对象类型，用于人脸检测。检测点应在0-1坐标系内，该坐标系左上角为(0.0，0.0)，右下角为(1.0，1.0)。此坐标系以设备充电口在右侧时的横向设备方向为基准。例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为(w，h)， 返回点为(x，y)，则转换后的坐标点为(1.0-y，x)。

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知类型。

**起始版本：** 19

### func !=(MetadataObjectType)

```cangjie
public operator func !=(other: MetadataObjectType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MetadataObjectType](#enum-metadataobjecttype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(MetadataObjectType)

```cangjie
public operator func ==(other: MetadataObjectType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MetadataObjectType](#enum-metadataobjecttype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|