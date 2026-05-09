## enum Direction

```cangjie
public enum Direction <: Equatable<Direction> {
    | Ltr
    | Rtl
    | Auto
    | ...
}
```

**功能：** 元素布局方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[Direction](#enum-direction)>

### Ltr

```cangjie
Ltr
```

**功能：** 元素从左到右布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Rtl

```cangjie
Rtl
```

**功能：** 元素从右到左布局。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Auto

```cangjie
Auto
```

**功能：** 使用默认布局方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(Direction)

```cangjie
public operator func ==(other: Direction): Bool
```

**功能：** 判断两个Direction枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Direction](#enum-direction)|是|-|要比较的另一个Direction枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(Direction)

```cangjie
public operator func !=(other: Direction): Bool
```

**功能：** 判断两个Direction枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Direction](#enum-direction)|是|-|要比较的另一个Direction枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum ScrollDirection

```cangjie
public enum ScrollDirection <: Equatable<ScrollDirection> {
    | Vertical
    | Horizontal
    | ...
}
```

**功能：** 滚动方向枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ScrollDirection](#enum-scrolldirection)>

### Vertical

```cangjie
Vertical
```

**功能：** 仅支持竖直方向滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Horizontal

```cangjie
Horizontal
```

**功能：** 仅支持水平方向滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ScrollDirection)

```cangjie
public operator func ==(other: ScrollDirection): Bool
```

**功能：** 判断两个ScrollDirection枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScrollDirection](#enum-scrolldirection)|是|-|要比较的另一个ScrollDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ScrollDirection)

```cangjie
public operator func !=(other: ScrollDirection): Bool
```

**功能：** 判断两个ScrollDirection枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScrollDirection](#enum-scrolldirection)|是|-|要比较的另一个ScrollDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|