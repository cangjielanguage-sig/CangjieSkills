## enum CameraPosition

```cangjie
public enum CameraPosition {
    | CameraPositionUnspecified
    | CameraPositionBack
    | CameraPositionFront
    | ...
}
```

**功能：** 枚举，相机位置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<CameraPosition>
- ToString

### CameraPositionBack

```cangjie
CameraPositionBack
```

**功能：** 后置相机。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraPositionFront

```cangjie
CameraPositionFront
```

**功能：** 前置相机。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraPositionUnspecified

```cangjie
CameraPositionUnspecified
```

**功能：** 相对于设备屏幕没有固定的朝向的相机

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(CameraPosition)

```cangjie
public operator func !=(other: CameraPosition): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

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

**起始版本：** 22

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

**功能：** 获取枚举的字符串值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串值。|