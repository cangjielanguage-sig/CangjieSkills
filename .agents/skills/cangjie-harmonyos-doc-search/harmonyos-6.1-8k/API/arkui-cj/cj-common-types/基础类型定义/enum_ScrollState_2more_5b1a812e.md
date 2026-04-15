## enum ScrollState

```cangjie
public enum ScrollState <: Equatable<ScrollState> {
    | Idle
    | Scroll
    | Fling
    | ...
}
```

**功能：** 设置当前滑动状态

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ScrollState](#enum-scrollstate)>

### Idle

```cangjie
Idle
```

**功能：** 未滑动状态

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Scroll

```cangjie
Scroll
```

**功能：** 手指拖动状态

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Fling

```cangjie
Fling
```

**功能：** 拖拽结束之后的惯性滑动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ScrollState)

```cangjie
public operator func ==(other: ScrollState): Bool
```

**功能：** 判断两个ScrollState枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScrollState](#enum-scrollstate)|是|-|要比较的另一个ScrollState枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ScrollState)

```cangjie
public operator func !=(other: ScrollState): Bool
```

**功能：** 判断两个ScrollState枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScrollState](#enum-scrollstate)|是|-|要比较的另一个ScrollState枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum ImageSmoothingQuality

```cangjie
public enum ImageSmoothingQuality <: Equatable<ImageSmoothingQuality> {
    | Low
    | Medium
    | High
    | ...
}
```

**功能：** 设置图像平滑度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ImageSmoothingQuality](#enum-imagesmoothingquality)>

### Low

```cangjie
Low
```

**功能：** 低画质。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Medium

```cangjie
Medium
```

**功能：** 中画质。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### High

```cangjie
High
```

**功能：** 高画质。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ImageSmoothingQuality)

```cangjie
public operator func ==(other: ImageSmoothingQuality): Bool
```

**功能：** 判断两个ImageSmoothingQuality枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageSmoothingQuality](#enum-imagesmoothingquality)|是|-|要比较的另一个ImageSmoothingQuality枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ImageSmoothingQuality)

```cangjie
public operator func !=(other: ImageSmoothingQuality): Bool
```

**功能：** 判断两个ImageSmoothingQuality枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageSmoothingQuality](#enum-imagesmoothingquality)|是|-|要比较的另一个ImageSmoothingQuality枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|