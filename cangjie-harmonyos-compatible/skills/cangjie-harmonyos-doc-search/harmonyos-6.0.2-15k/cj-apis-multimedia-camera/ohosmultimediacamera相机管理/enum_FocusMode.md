## enum FocusMode

```cangjie
public enum FocusMode <: Equatable<FocusMode> & ToString {
    | FOCOS_MODE_MANUAL
    | FOCOS_MODE_CONTINUOUS_AUTO
    | FOCOS_MODE_AUTO
    | FOCUS_MODE_LOCKED
    | ...
}
```

**功能：** 焦距模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<FocusMode>
- ToString

### FOCOS_MODE_AUTO

```cangjie
FOCOS_MODE_AUTO
```

**功能：** 自动对焦。支持对焦点设置，可以使用[setFocusPoint](#func-setfocuspointpoint)设置对焦点，根据对焦点执行一次自动对焦。

**起始版本：** 19

### FOCOS_MODE_CONTINUOUS_AUTO

```cangjie
FOCOS_MODE_CONTINUOUS_AUTO
```

**功能：** 连续自动对焦。不支持对焦点设置。

**起始版本：** 19

### FOCOS_MODE_MANUAL

```cangjie
FOCOS_MODE_MANUAL
```

**功能：** 手动对焦。通过手动修改相机焦距来改变对焦位置，不支持对焦点设置。

**起始版本：** 19

### FOCUS_MODE_LOCKED

```cangjie
FOCUS_MODE_LOCKED
```

**功能：** 对焦锁定。不支持对焦点设置。

**起始版本：** 19

### func !=(FocusMode)

```cangjie
public operator func !=(other: FocusMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

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

**起始版本：** 19

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

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|