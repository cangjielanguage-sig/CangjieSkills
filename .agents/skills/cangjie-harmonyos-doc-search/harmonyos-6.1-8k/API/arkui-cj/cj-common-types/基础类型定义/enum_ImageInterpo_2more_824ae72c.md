## enum ImageInterpolation

```cangjie
public enum ImageInterpolation <: Equatable<ImageInterpolation> {
    | None
    | High
    | Medium
    | Low
    | ...
}
```

**功能：** 图像插值方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ImageInterpolation](#enum-imageinterpolation)>

### None

```cangjie
None
```

**功能：** 无插值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### High

```cangjie
High
```

**功能：** 高质量插值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Medium

```cangjie
Medium
```

**功能：** 中等质量插值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Low

```cangjie
Low
```

**功能：** 低质量插值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ImageInterpolation)

```cangjie
public operator func ==(other: ImageInterpolation): Bool
```

**功能：** 判断两个ImageInterpolation枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageInterpolation](#enum-imageinterpolation)|是|-|要比较的另一个ImageInterpolation枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ImageInterpolation)

```cangjie
public operator func !=(other: ImageInterpolation): Bool
```

**功能：** 判断两个ImageInterpolation枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageInterpolation](#enum-imageinterpolation)|是|-|要比较的另一个ImageInterpolation枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum BarState

```cangjie
public enum BarState <: Equatable<BarState> {
    | Off
    | Auto
    | On
    | ...
}
```

**功能：** 滚动条的显示模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[BarState](#enum-barstate)>

### Off

```cangjie
Off
```

**功能：** 不显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Auto

```cangjie
Auto
```

**功能：** 按需显示（触摸时显示，2秒后消失）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### On

```cangjie
On
```

**功能：** 常驻显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(BarState)

```cangjie
public operator func ==(other: BarState): Bool
```

**功能：** 判断两个BarState枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BarState](#enum-barstate)|是|-|要比较的另一个BarState枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(BarState)

```cangjie
public operator func !=(other: BarState): Bool
```

**功能：** 判断两个BarState枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BarState](#enum-barstate)|是|-|要比较的另一个BarState枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|