## enum CameraType

```cangjie
public enum CameraType {
    | CameraTypeDefault
    | CameraTypeWideAngle
    | CameraTypeUltraWide
    | CameraTypeTelephoto
    | CameraTypeTrueDepth
    | ...
}
```

**功能：** 枚举，相机类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<CameraType>
- ToString

### CameraTypeDefault

```cangjie
CameraTypeDefault
```

**功能：** 默认相机类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraTypeTelephoto

```cangjie
CameraTypeTelephoto
```

**功能：** 长焦相机。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraTypeTrueDepth

```cangjie
CameraTypeTrueDepth
```

**功能：** 带景深信息的相机。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraTypeUltraWide

```cangjie
CameraTypeUltraWide
```

**功能：** 超广角相机。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraTypeWideAngle

```cangjie
CameraTypeWideAngle
```

**功能：** 广角相机。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(CameraType)

```cangjie
public operator func !=(other: CameraType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraType](#enum-cameratype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CameraType)

```cangjie
public operator func ==(other: CameraType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraType](#enum-cameratype)|是|-|另一个枚举值。|

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