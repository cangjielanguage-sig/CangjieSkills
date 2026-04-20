## enum ScaleMode

```cangjie
public enum ScaleMode <: Equatable<ScaleMode> & ToString {
    | FIT_TARGET_SIZE
    | CENTER_CROP
    | ...
}
```

**功能：** 图像的缩放模式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**父类型：**

- Equatable\<ScaleMode>
- ToString

### CENTER_CROP

```cangjie
CENTER_CROP
```

**功能：** 缩放图像以填充目标图像区域并居中裁剪区域外的效果。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### FIT_TARGET_SIZE

```cangjie
FIT_TARGET_SIZE
```

**功能：** 图像适合目标尺寸的效果。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### func !=(ScaleMode)

```cangjie
public operator func !=(other: ScaleMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScaleMode](#enum-scalemode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ScaleMode)

```cangjie
public operator func ==(other: ScaleMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScaleMode](#enum-scalemode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|

## 补充说明

### SVG标签说明

支持SVG标签，使用版本为(SVG) 1.1，当前支持的标签列表有：

- a
- circla
- clipPath
- defs
- ellipse
- feBlend
- feColorMatrix
- feComposite
- feDiffuseLighting
- feDisplacementMap
- feDistantLight
- feFlood
- feGaussianBlur
- feImage
- feMorphology
- feOffset
- fePointLight
- feSpecularLighting
- feSpotLight
- feTurbulence
- filter
- g
- image
- line
- linearGradient
- mask
- path
- pattern
- polygon
- polyline
- radialGradient
- rect
- stop
- svg
- text
- textPath
- tspan
- use