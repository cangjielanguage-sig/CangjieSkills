## enum SceneMode

```cangjie
public enum SceneMode {
    | NormalPhoto
    | NormalVideo
    | SecurePhoto
    | ...
}
```

**功能：** 枚举，相机模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<SceneMode>
- ToString

### NormalPhoto

```cangjie
NormalPhoto
```

**功能：** 普通拍照模式。详情见[PhotoSession](#class-photosession)。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### NormalVideo

```cangjie
NormalVideo
```

**功能：** 普通录像模式。详情见[VideoSession](#class-videosession)。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### SecurePhoto

```cangjie
SecurePhoto
```

**功能：** 安全相机模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(SceneMode)

```cangjie
public operator func !=(other: SceneMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

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

**起始版本：** 22

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

**功能：** 获取枚举的字符串值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串值。|