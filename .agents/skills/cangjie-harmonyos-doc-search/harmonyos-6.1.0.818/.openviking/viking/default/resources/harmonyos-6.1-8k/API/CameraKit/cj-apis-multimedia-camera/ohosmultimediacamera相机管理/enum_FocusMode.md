## enum FocusMode

```cangjie
public enum FocusMode {
    | FocusModeManual
    | FocusModeContinuousAuto
    | FocusModeAuto
    | FocusModeLocked
    | ...
}
```

**功能：** 枚举，焦距模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<FocusMode>
- ToString

### FocusModeAuto

```cangjie
FocusModeAuto
```

**功能：** 自动对焦。支持对焦点设置，可以使用[setFocusPoint](#func-setfocuspointpoint)设置对焦点，根据对焦点执行一次自动对焦。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FocusModeContinuousAuto

```cangjie
FocusModeContinuousAuto
```

**功能：** 连续自动对焦。不支持对焦点设置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FocusModeLocked

```cangjie
FocusModeLocked
```

**功能：** 对焦锁定。不支持对焦点设置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FocusModeManual

```cangjie
FocusModeManual
```

**功能：** 手动对焦。通过手动修改相机焦距来改变对焦位置，不支持对焦点设置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(FocusMode)

```cangjie
public operator func !=(other: FocusMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FocusMode](#enum-focusmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(FocusMode)

```cangjie
public operator func ==(other: FocusMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FocusMode](#enum-focusmode)|是|-|另一个枚举值。|

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