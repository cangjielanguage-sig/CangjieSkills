## enum GradientDirection

```cangjie
public enum GradientDirection <: Equatable<GradientDirection> {
    | Left
    | Top
    | Right
    | Bottom
    | LeftTop
    | LeftBottom
    | RightTop
    | RightBottom
    | None
    | ...
}
```

**功能：** 梯度方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[GradientDirection](#enum-gradientdirection)>

### Left

```cangjie
Left
```

**功能：** 从右到左。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Top

```cangjie
Top
```

**功能：** 从下到上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Right

```cangjie
Right
```

**功能：** 从左到右。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bottom

```cangjie
Bottom
```

**功能：** 从上到下。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### LeftTop

```cangjie
LeftTop
```

**功能：** 左上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### LeftBottom

```cangjie
LeftBottom
```

**功能：** 左下。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### RightTop

```cangjie
RightTop
```

**功能：** 右上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### RightBottom

```cangjie
RightBottom
```

**功能：** 右下。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### None

```cangjie
None
```

**功能：** 无。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(GradientDirection)

```cangjie
public operator func ==(other: GradientDirection): Bool
```

**功能：** 判断两个GradientDirection枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GradientDirection](#enum-gradientdirection)|是|-|要比较的另一个GradientDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(GradientDirection)

```cangjie
public operator func !=(other: GradientDirection): Bool
```

**功能：** 判断两个GradientDirection枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GradientDirection](#enum-gradientdirection)|是|-|要比较的另一个GradientDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|