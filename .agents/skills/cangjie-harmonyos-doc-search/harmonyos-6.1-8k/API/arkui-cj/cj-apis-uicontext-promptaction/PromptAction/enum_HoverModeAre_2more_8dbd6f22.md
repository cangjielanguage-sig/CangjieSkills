## enum HoverModeAreaType

```cangjie
public enum HoverModeAreaType <: Equatable<HoverModeAreaType> {
    | TopScreen
    | BottomScreen
    | ...
}
```

**功能：** 提供悬停模式区域类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[HoverModeAreaType](#enum-hovermodeareatype)>

### TopScreen

```cangjie
TopScreen
```

**功能：** 顶部屏幕悬停模式区域类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BottomScreen

```cangjie
BottomScreen
```

**功能：** 底部屏幕悬停模式区域类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func !=(HoverModeAreaType)

```cangjie
public operator func !=(other: HoverModeAreaType): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[HoverModeAreaType](#enum-hovermodeareatype)|是|-|要比较的另一个HoverModeAreaType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(HoverModeAreaType)

```cangjie
public operator func ==(other: HoverModeAreaType): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[HoverModeAreaType](#enum-hovermodeareatype)|是|-|要比较的另一个HoverModeAreaType实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|

## enum KeyboardAvoidMode

```cangjie
public enum KeyboardAvoidMode <: Equatable<KeyboardAvoidMode> {
    | Default
    | None
    | ...
}
```

**功能：** 提供键盘避免模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[KeyboardAvoidMode](#enum-keyboardavoidmode)>

### Default

```cangjie
Default
```

**功能：** 默认键盘避免模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### None

```cangjie
None
```

**功能：** 无键盘避免模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func !=(KeyboardAvoidMode)

```cangjie
public operator func !=(other: KeyboardAvoidMode): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[KeyboardAvoidMode](#enum-keyboardavoidmode)|是|-|要比较的另一个KeyboardAvoidMode实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(KeyboardAvoidMode)

```cangjie
public operator func ==(other: KeyboardAvoidMode): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[KeyboardAvoidMode](#enum-keyboardavoidmode)|是|-|要比较的另一个KeyboardAvoidMode实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|