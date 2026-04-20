## enum BarMode

```cangjie
public enum BarMode <: Equatable<BarMode> {
    | Fixed
    | Scrollable
    | ...
}
```

**功能：** TabBar布局模式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[BarMode](#enum-barmode)>

### Fixed

```cangjie
Fixed
```

**功能：** 所有TabBar均分屏幕宽度，TabBar不可滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Scrollable

```cangjie
Scrollable
```

**功能：** 所有TabBar按照自身尺寸布局，TabBar可滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(BarMode)

```cangjie
public operator func ==(other: BarMode): Bool
```

**功能：** 判断两个BarMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BarMode](#enum-barmode)|是|-|要比较的另一个BarMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(BarMode)

```cangjie
public operator func !=(other: BarMode): Bool
```

**功能：** 判断两个BarMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BarMode](#enum-barmode)|是|-|要比较的另一个BarMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum ShadowType

```cangjie
public enum ShadowType <: Equatable<ShadowType> {
    | Color
    | Blur
    | ...
}
```

**功能：** 阴影类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ShadowType](#enum-shadowtype)>

### Color

```cangjie
Color
```

**功能：** 颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Blur

```cangjie
Blur
```

**功能：** 模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ShadowType)

```cangjie
public operator func ==(other: ShadowType): Bool
```

**功能：** 判断两个ShadowType枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ShadowType](#enum-shadowtype)|是|-|要比较的另一个ShadowType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ShadowType)

```cangjie
public operator func !=(other: ShadowType): Bool
```

**功能：** 判断两个ShadowType枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ShadowType](#enum-shadowtype)|是|-|要比较的另一个ShadowType枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|