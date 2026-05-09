## enum CanvasDirection

```cangjie
public enum CanvasDirection <: Equatable<CanvasDirection> {
    | Inherit
    | Ltr
    | Rtl
    | ...
}
```

**功能：** 设置绘制文字时使用的文字方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[CanvasDirection](#enum-canvasdirection)>

### Inherit

```cangjie
Inherit
```

**功能：** 继承canvas组件通用属性已设定的文本方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Ltr

```cangjie
Ltr
```

**功能：** 从左往右。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Rtl

```cangjie
Rtl
```

**功能：** 从右往左。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(CanvasDirection)

```cangjie
public operator func ==(other: CanvasDirection): Bool
```

**功能：** 判断两个CanvasDirection枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CanvasDirection](#enum-canvasdirection)|是|-|要比较的另一个CanvasDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(CanvasDirection)

```cangjie
public operator func !=(other: CanvasDirection): Bool
```

**功能：** 判断两个CanvasDirection枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CanvasDirection](#enum-canvasdirection)|是|-|要比较的另一个CanvasDirection枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum CanvasFillRule

```cangjie
public enum CanvasFillRule <: Equatable<CanvasFillRule> {
    | EvenOdd
    | NonZero
    | ...
}
```

**功能：** 指定要填充对象的规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[CanvasFillRule](#enum-canvasfillrule)>

### EvenOdd

```cangjie
EvenOdd
```

**功能：** 奇偶规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### NonZero

```cangjie
NonZero
```

**功能：** 非零规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(CanvasFillRule)

```cangjie
public operator func ==(other: CanvasFillRule): Bool
```

**功能：** 判断两个CanvasFillRule枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CanvasFillRule](#enum-canvasfillrule)|是|-|要比较的另一个CanvasFillRule枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(CanvasFillRule)

```cangjie
public operator func !=(other: CanvasFillRule): Bool
```

**功能：** 判断两个CanvasFillRule枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CanvasFillRule](#enum-canvasfillrule)|是|-|要比较的另一个CanvasFillRule枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|