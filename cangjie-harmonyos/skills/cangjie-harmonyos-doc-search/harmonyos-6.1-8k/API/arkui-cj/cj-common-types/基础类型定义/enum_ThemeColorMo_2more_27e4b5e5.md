## enum ThemeColorMode

```cangjie
public enum ThemeColorMode <: Equatable<ThemeColorMode> {
    | System
    | Light
    | Dark
    | ...
}
```

**功能：** 主题颜色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ThemeColorMode](#enum-themecolormode)>

### System

```cangjie
System
```

**功能：** 跟随系统深浅色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Light

```cangjie
Light
```

**功能：** 固定使用浅色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Dark

```cangjie
Dark
```

**功能：** 固定使用深色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ThemeColorMode)

```cangjie
public operator func ==(other: ThemeColorMode): Bool
```

**功能：** 判断两个ThemeColorMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ThemeColorMode](#enum-themecolormode)|是|-|要比较的另一个ThemeColorMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ThemeColorMode)

```cangjie
public operator func !=(other: ThemeColorMode): Bool
```

**功能：** 判断两个ThemeColorMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ThemeColorMode](#enum-themecolormode)|是|-|要比较的另一个ThemeColorMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum AdaptiveColor

```cangjie
public enum AdaptiveColor <: Equatable<AdaptiveColor> {
    | Default
    | Average
    | ...
}
```

**功能：** 取色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[AdaptiveColor](#enum-adaptivecolor)>

### Default

```cangjie
Default
```

**功能：** 不使用取色模糊。使用默认的颜色作为蒙版颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Average

```cangjie
Average
```

**功能：** 使用取色模糊。将取色区域的颜色平均值作为蒙版颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(AdaptiveColor)

```cangjie
public operator func ==(other: AdaptiveColor): Bool
```

**功能：** 判断两个AdaptiveColor枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AdaptiveColor](#enum-adaptivecolor)|是|-|要比较的另一个AdaptiveColor枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(AdaptiveColor)

```cangjie
public operator func !=(other: AdaptiveColor): Bool
```

**功能：** 判断两个AdaptiveColor枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AdaptiveColor](#enum-adaptivecolor)|是|-|要比较的另一个AdaptiveColor枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|