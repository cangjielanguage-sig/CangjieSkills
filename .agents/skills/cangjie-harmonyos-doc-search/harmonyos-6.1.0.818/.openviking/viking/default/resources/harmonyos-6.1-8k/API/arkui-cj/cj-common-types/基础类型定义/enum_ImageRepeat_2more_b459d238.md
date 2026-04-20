## enum ImageRepeat

```cangjie
public enum ImageRepeat <: Equatable<ImageRepeat> {
    | NoRepeat
    | X
    | Y
    | XY
    | ...
}
```

**功能：** 图片重复方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ImageRepeat](#enum-imagerepeat)>

### NoRepeat

```cangjie
NoRepeat
```

**功能：** 不重复绘制图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### X

```cangjie
X
```

**功能：** 只在水平轴上重复绘制图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Y

```cangjie
Y
```

**功能：** 只在竖直轴上重复绘制图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### XY

```cangjie
XY
```

**功能：** 在两个轴上重复绘制图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ImageRepeat)

```cangjie
public operator func ==(other: ImageRepeat): Bool
```

**功能：** 判断两个ImageRepeat枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageRepeat](#enum-imagerepeat)|是|-|要比较的另一个ImageRepeat枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ImageRepeat)

```cangjie
public operator func !=(other: ImageRepeat): Bool
```

**功能：** 判断两个ImageRepeat枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageRepeat](#enum-imagerepeat)|是|-|要比较的另一个ImageRepeat枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum ImageSize

```cangjie
public enum ImageSize <: Equatable<ImageSize> {
    | Contain
    | Cover
    | Auto
    | ...
}
```

**功能：** 图片尺寸显示设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ImageSize](#enum-imagesize)>

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

**功能：** 使用Flex容器中默认配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ImageSize)

```cangjie
public operator func ==(other: ImageSize): Bool
```

**功能：** 判断两个ImageSize枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageSize](#enum-imagesize)|是|-|要比较的另一个ImageSize枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ImageSize)

```cangjie
public operator func !=(other: ImageSize): Bool
```

**功能：** 判断两个ImageSize枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageSize](#enum-imagesize)|是|-|要比较的另一个ImageSize枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|