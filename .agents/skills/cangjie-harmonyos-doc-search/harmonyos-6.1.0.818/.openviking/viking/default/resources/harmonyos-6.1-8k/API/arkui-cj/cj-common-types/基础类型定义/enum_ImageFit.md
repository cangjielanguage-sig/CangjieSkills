## enum ImageFit

```cangjie
public enum ImageFit <: Equatable<ImageFit> {
    | Fill
    | Contain
    | Cover
    | Auto
    | None
    | ScaleDown
    | ...
}
```

**功能：** 图片的显示适配方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ImageFit](#enum-imagefit)>

### Fill

```cangjie
Fill
```

**功能：** 不保持宽高比进行缩放，图片会被拉伸以填满整个显示边界。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Contain

```cangjie
Contain
```

**功能：** 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Cover

```cangjie
Cover
```

**功能：** 保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Auto

```cangjie
Auto
```

**功能：** 默认值，保持原图的比例不变。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### None

```cangjie
None
```

**功能：** 图片不进行任何缩放，保持原始尺寸显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ScaleDown

```cangjie
ScaleDown
```

**功能：** 图片会按照比例缩小，但不会放大，保持宽高比。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ImageFit)

```cangjie
public operator func ==(other: ImageFit): Bool
```

**功能：** 判断两个ImageFit枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageFit](#enum-imagefit)|是|-|要比较的另一个ImageFit枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ImageFit)

```cangjie
public operator func !=(other: ImageFit): Bool
```

**功能：** 判断两个ImageFit枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageFit](#enum-imagefit)|是|-|要比较的另一个ImageFit枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|