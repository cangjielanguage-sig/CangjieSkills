## enum ImageRotation

```cangjie
public enum ImageRotation {
    | Rotation0
    | Rotation90
    | Rotation180
    | Rotation270
    | ...
}
```

**功能：** 枚举，图片旋转角度。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<ImageRotation>
- ToString

### Rotation0

```cangjie
Rotation0
```

**功能：** 图片旋转0度。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### Rotation180

```cangjie
Rotation180
```

**功能：** 图片旋转180度。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### Rotation270

```cangjie
Rotation270
```

**功能：** 图片旋转270度。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### Rotation90

```cangjie
Rotation90
```

**功能：** 图片旋转90度。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(ImageRotation)

```cangjie
public operator func !=(other: ImageRotation): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

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

**起始版本：** 22

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

**功能：** 获取枚举的字符串值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串值。|