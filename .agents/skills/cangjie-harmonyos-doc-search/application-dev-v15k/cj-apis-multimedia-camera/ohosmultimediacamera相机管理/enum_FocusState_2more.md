## enum FocusState

```cangjie
public enum FocusState <: Equatable<FocusState> & ToString {
    | FOCUS_STATE_SCAN
    | FOCUS_STATE_FOCUSED
    | FOCUS_STATE_UNFOCUSED
    | ...
}
```

**功能：** 焦距状态。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<FocusState>
- ToString

### FOCUS_STATE_FOCUSED

```cangjie
FOCUS_STATE_FOCUSED
```

**功能：** 对焦成功。

**起始版本：** 19

### FOCUS_STATE_SCAN

```cangjie
FOCUS_STATE_SCAN
```

**功能：** 触发对焦。

**起始版本：** 19

### FOCUS_STATE_UNFOCUSED

```cangjie
FOCUS_STATE_UNFOCUSED
```

**功能：** 未完成对焦。

**起始版本：** 19

### func !=(FocusState)

```cangjie
public operator func !=(other: FocusState): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FocusState](#enum-focusstate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(FocusState)

```cangjie
public operator func ==(other: FocusState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FocusState](#enum-focusstate)|是|-|另一个枚举值。|

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

## enum FoldStatus

```cangjie
public enum FoldStatus <: Equatable<FoldStatus> & ToString {
    | NON_FOLDABLE
    | EXPANDED
    | FOLDED
    | ...
}
```

**功能：** 折叠机折叠状态。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<FoldStatus>
- ToString

### EXPANDED

```cangjie
EXPANDED
```

**功能：** 表示当前设备折叠状态为完全展开。

**起始版本：** 19

### FOLDED

```cangjie
FOLDED
```

**功能：** 表示当前设备折叠状态为折叠。

**起始版本：** 19

### NON_FOLDABLE

```cangjie
NON_FOLDABLE
```

**功能：** 表示当前设备不可折叠。

**起始版本：** 19

### func !=(FoldStatus)

```cangjie
public operator func !=(other: FoldStatus): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FoldStatus](#enum-foldstatus)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(FoldStatus)

```cangjie
public operator func ==(other: FoldStatus): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FoldStatus](#enum-foldstatus)|是|-|另一个枚举值。|

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