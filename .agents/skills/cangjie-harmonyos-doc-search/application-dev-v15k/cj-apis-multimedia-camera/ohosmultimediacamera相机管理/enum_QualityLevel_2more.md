## enum QualityLevel

```cangjie
public enum QualityLevel <: Equatable<QualityLevel> & ToString {
    | QUALITY_LEVEL_HIGH
    | QUALITY_LEVEL_MEDIUM
    | QUALITY_LEVEL_LOW
    | ...
}
```

**功能：** 图片质量。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<QualityLevel>
- ToString

### QUALITY_LEVEL_HIGH

```cangjie
QUALITY_LEVEL_HIGH
```

**功能：** 图片质量高。

**起始版本：** 19

### QUALITY_LEVEL_LOW

```cangjie
QUALITY_LEVEL_LOW
```

**功能：** 图片质量差。

**起始版本：** 19

### QUALITY_LEVEL_MEDIUM

```cangjie
QUALITY_LEVEL_MEDIUM
```

**功能：** 图片质量中等。

**起始版本：** 19

### func !=(QualityLevel)

```cangjie
public operator func !=(other: QualityLevel): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[QualityLevel](#enum-qualitylevel)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(QualityLevel)

```cangjie
public operator func ==(other: QualityLevel): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[QualityLevel](#enum-qualitylevel)|是|-|另一个枚举值。|

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

## enum SceneMode

```cangjie
public enum SceneMode <: Equatable<SceneMode> & ToString {
    | NORMAL_PHOTO
    | NORMAL_VIDEO
    | SECURE_PHOTO
    | ...
}
```

**功能：** 相机支持模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<SceneMode>
- ToString

### NORMAL_PHOTO

```cangjie
NORMAL_PHOTO
```

**功能：** 普通拍照模式。详情见[PhotoSession](#class-photosession)。

**起始版本：** 19

### NORMAL_VIDEO

```cangjie
NORMAL_VIDEO
```

**功能：** 普通录像模式。详情见[VideoSession](#class-videosession)。

**起始版本：** 19

### SECURE_PHOTO

```cangjie
SECURE_PHOTO
```

**功能：** 安全相机模式。详情见[SecureSession](#class-securesession)。

**起始版本：** 19

### func !=(SceneMode)

```cangjie
public operator func !=(other: SceneMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SceneMode](#enum-scenemode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(SceneMode)

```cangjie
public operator func ==(other: SceneMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SceneMode](#enum-scenemode)|是|-|另一个枚举值。|

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