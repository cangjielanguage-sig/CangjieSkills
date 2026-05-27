# Path

路径绘制组件，根据绘制路径生成封闭的自定义形状。

## 子组件

无

## 创建组件

### init(String)

```cangjie
public init(commands!: String = "")
```

**功能：** 根据绘制路径命令字符串创建一个路径绘制组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|commands|String|否|""| **命名参数。** 路径绘制的命令字符串。|

### init(Length, Length, String)

```cangjie
public init(width!: Length, height!: Length, commands!: String = "")
```

**功能：** 根据路径所在的矩形宽度、高度创建一个路径绘制组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 路径所在矩形的宽度，取值范围≥0。<br>默认单位：vp。<br>值为异常值或缺省时按照自身内容需要的宽度处理。|
|height|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 路径所在矩形的高度，取值范围≥0。<br>默认单位：vp。<br>值为异常值或缺省时按照自身内容需要的高度处理。|
|commands|String|否|""| **命名参数。** 路径绘制的命令字符串。|

## 通用属性/通用事件

通用属性：除了支持通用属性外，还支持[图形绘制通用属性](./cj-graphic-drawing-common.md)。

通用事件：全部支持。

## 组件属性

### func commands(String)

```cangjie
public func commands(commands: String): This
```

**功能：** 设置符合[SVG路径描述规范](#svg路径描述规范)的命令字符串，单位为px。像素单位转换方法请参考[像素单位转换](./cj-common-pixelunits.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|commands|String|是|-|路径绘制的命令字符串。初始值：""，异常值按照初始值处理。|