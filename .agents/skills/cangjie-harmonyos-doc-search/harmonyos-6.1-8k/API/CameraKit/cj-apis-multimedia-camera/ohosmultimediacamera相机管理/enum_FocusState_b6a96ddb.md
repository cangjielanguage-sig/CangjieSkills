## enum FocusState

```cangjie
public enum FocusState {
    | FocusStateScan
    | FocusStateFocused
    | FocusStateUnfocused
    | ...
}
```

**功能：** 枚举，焦距状态。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<FocusState>
- ToString

### FocusStateFocused

```cangjie
FocusStateFocused
```

**功能：** 对焦成功。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FocusStateScan

```cangjie
FocusStateScan
```

**功能：** 触发对焦。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FocusStateUnfocused

```cangjie
FocusStateUnfocused
```

**功能：** 未完成对焦。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(FocusState)

```cangjie
public operator func !=(other: FocusState): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

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

**起始版本：** 22

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

**功能：** 获取枚举的字符串值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串值。|