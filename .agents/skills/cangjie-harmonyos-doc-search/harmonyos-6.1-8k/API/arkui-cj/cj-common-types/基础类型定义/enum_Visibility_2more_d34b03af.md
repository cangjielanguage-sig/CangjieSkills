## enum Visibility

```cangjie
public enum Visibility <: Equatable<Visibility> {
    | Visible
    | Hidden
    | None
    | ...
}
```

**功能：** 当前组件显示或隐藏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[Visibility](#enum-visibility)>

### Visible

```cangjie
Visible
```

**功能：** 显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Hidden

```cangjie
Hidden
```

**功能：** 隐藏，但参与布局进行占位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### None

```cangjie
None
```

**功能：** 隐藏，但不参与布局，不进行占位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(Visibility)

```cangjie
public operator func ==(other: Visibility): Bool
```

**功能：** 判断两个Visibility枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Visibility](#enum-visibility)|是|-|要比较的另一个Visibility枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(Visibility)

```cangjie
public operator func !=(other: Visibility): Bool
```

**功能：** 判断两个Visibility枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Visibility](#enum-visibility)|是|-|要比较的另一个Visibility枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum LineCapStyle

```cangjie
public enum LineCapStyle <: Equatable<LineCapStyle> {
    | Butt
    | Round
    | Square
    | ...
}
```

**功能：** 线条样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[LineCapStyle](#enum-linecapstyle)>

### Butt

```cangjie
Butt
```

**功能：** 线条两端为平行线，不额外扩展

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Round

```cangjie
Round
```

**功能：** 在线条两端延伸半个圆，直径等于线宽

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Square

```cangjie
Square
```

**功能：** 在线条两端延伸半个圆，直径等于线宽

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(LineCapStyle)

```cangjie
public operator func ==(other: LineCapStyle): Bool
```

**功能：** 判断两个LineCapStyle枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LineCapStyle](#enum-linecapstyle)|是|-|要比较的另一个LineCapStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(LineCapStyle)

```cangjie
public operator func !=(other: LineCapStyle): Bool
```

**功能：** 判断两个LineCapStyle枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LineCapStyle](#enum-linecapstyle)|是|-|要比较的另一个LineCapStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|