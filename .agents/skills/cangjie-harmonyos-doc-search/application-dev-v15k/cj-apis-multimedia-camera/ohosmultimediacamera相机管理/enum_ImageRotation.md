## enum ImageRotation

```cangjie
public enum ImageRotation <: Equatable<ImageRotation> & ToString {
    | ROTATION_0
    | ROTATION_90
    | ROTATION_180
    | ROTATION_270
    | ...
}
```

**功能：** 图片旋转角度。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<ImageRotation>
- ToString

### ROTATION_0

```cangjie
ROTATION_0
```

**功能：** 图片旋转0度。

**起始版本：** 19

### ROTATION_180

```cangjie
ROTATION_180
```

**功能：** 图片旋转180度。

**起始版本：** 19

### ROTATION_270

```cangjie
ROTATION_270
```

**功能：** 图片旋转270度。

**起始版本：** 19

### ROTATION_90

```cangjie
ROTATION_90
```

**功能：** 图片旋转90度。

**起始版本：** 19

### func !=(ImageRotation)

```cangjie
public operator func !=(other: ImageRotation): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageRotation](#enum-imagerotation)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ImageRotation)

```cangjie
public operator func ==(other: ImageRotation): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageRotation](#enum-imagerotation)|是|-|另一个枚举值。|

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