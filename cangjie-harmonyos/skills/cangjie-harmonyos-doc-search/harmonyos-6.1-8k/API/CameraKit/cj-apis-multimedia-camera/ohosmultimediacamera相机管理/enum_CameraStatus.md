## enum CameraStatus

```cangjie
public enum CameraStatus {
    | CameraStatusAppear
    | CameraStatusDisappear
    | CameraStatusAvailable
    | CameraStatusUnavailable
    | ...
}
```

**功能：** 枚举，相机状态。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<CameraStatus>
- ToString

### CameraStatusAppear

```cangjie
CameraStatusAppear
```

**功能：** 新的相机出现。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraStatusAvailable

```cangjie
CameraStatusAvailable
```

**功能：** 相机可用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraStatusDisappear

```cangjie
CameraStatusDisappear
```

**功能：** 相机被移除。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraStatusUnavailable

```cangjie
CameraStatusUnavailable
```

**功能：** 相机不可用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(CameraStatus)

```cangjie
public operator func !=(other: CameraStatus): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraStatus](#enum-camerastatus)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CameraStatus)

```cangjie
public operator func ==(other: CameraStatus): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraStatus](#enum-camerastatus)|是|-|另一个枚举值。|

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