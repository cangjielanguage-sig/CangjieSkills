## enum CameraPosition

```cangjie
public enum CameraPosition <: Equatable<CameraPosition> & ToString {
    | CAMERA_POSITION_UNSPECIFIED
    | CAMERA_POSITION_BACK
    | CAMERA_POSITION_FRONT
    | ...
}
```

**功能：** 相机位置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<CameraPosition>
- ToString

### CAMERA_POSITION_BACK

```cangjie
CAMERA_POSITION_BACK
```

**功能：** 后置相机。

**起始版本：** 19

### CAMERA_POSITION_FRONT

```cangjie
CAMERA_POSITION_FRONT
```

**功能：** 前置相机。

**起始版本：** 19

### CAMERA_POSITION_UNSPECIFIED

```cangjie
CAMERA_POSITION_UNSPECIFIED
```

**功能：** 相机位置未指定。

**起始版本：** 19

### func !=(CameraPosition)

```cangjie
public operator func !=(other: CameraPosition): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraPosition](#enum-cameraposition)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CameraPosition)

```cangjie
public operator func ==(other: CameraPosition): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraPosition](#enum-cameraposition)|是|-|另一个枚举值。|

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