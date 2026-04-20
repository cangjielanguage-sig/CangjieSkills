## enum MouseButton

```cangjie
public enum MouseButton <: Equatable<MouseButton> {
    | None
    | Left
    | Right
    | Middle
    | Back
    | Forward
    | ...
}
```

**功能：** 鼠标按键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[MouseButton](#enum-mousebutton)>

### None

```cangjie
None
```

**功能：** 无按键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Left

```cangjie
Left
```

**功能：** 鼠标左键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Right

```cangjie
Right
```

**功能：** 鼠标右键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Middle

```cangjie
Middle
```

**功能：** 鼠标中键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Back

```cangjie
Back
```

**功能：** 鼠标后退键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Forward

```cangjie
Forward
```

**功能：** 鼠标前进键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(MouseButton)

```cangjie
public operator func ==(other: MouseButton): Bool
```

**功能：** 判断两个MouseButton枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MouseButton](#enum-mousebutton)|是|-|要比较的另一个MouseButton枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(MouseButton)

```cangjie
public operator func !=(other: MouseButton): Bool
```

**功能：** 判断两个MouseButton枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MouseButton](#enum-mousebutton)|是|-|要比较的另一个MouseButton枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|