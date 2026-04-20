## enum ImageSpanAlignment

```cangjie
public enum ImageSpanAlignment <: Equatable<ImageSpanAlignment> {
    | Top
    | Center
    | Bottom
    | Baseline
    | ...
}
```

**功能：** 图片基于行高的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ImageSpanAlignment](#enum-imagespanalignment)>

### Top

```cangjie
Top
```

**功能：** 图片上边沿与行上边沿对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Center

```cangjie
Center
```

**功能：** 图片中间与行中间对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bottom

```cangjie
Bottom
```

**功能：** 图片下边沿与行下边沿对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Baseline

```cangjie
Baseline
```

**功能：** 图片下边沿与文本BaseLine对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ImageSpanAlignment)

```cangjie
public operator func ==(other: ImageSpanAlignment): Bool
```

**功能：** 判断两个ImageSpanAlignment枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageSpanAlignment](#enum-imagespanalignment)|是|-|要比较的另一个ImageSpanAlignment枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ImageSpanAlignment)

```cangjie
public operator func !=(other: ImageSpanAlignment): Bool
```

**功能：** 判断两个ImageSpanAlignment枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ImageSpanAlignment](#enum-imagespanalignment)|是|-|要比较的另一个ImageSpanAlignment枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|