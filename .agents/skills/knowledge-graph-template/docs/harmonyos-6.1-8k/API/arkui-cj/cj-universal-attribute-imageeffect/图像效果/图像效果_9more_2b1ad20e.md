# 图像效果

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

设置组件的模糊、阴影、球面效果以及设置图片的图像效果。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## func blur(?Float64)

```cangjie
func blur(value: ?Float64): T
```

**功能：** 为当前组件添加内容模糊效果。输入参数为模糊半径，半径越大内容越模糊，为0时不模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float64|是|-|模糊半径。初始值：0.0|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|

## func colorBlend(?ResourceColor)

```cangjie
func colorBlend(value: ?ResourceColor): T
```

**功能：** 为组件添加颜色混合效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|颜色混合值。初始值：Color.Transparent|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|

## func backdropBlur(?Float64)

```cangjie
func backdropBlur(value: ?Float64): T
```

**功能：** 为组件添加背景模糊效果，可以自定义模糊半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float64|是|-|模糊半径。初始值：0.0|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|

## func shadow(?Float64, ?ResourceColor, ?Float64, ?Float64)

```cangjie
func shadow(radius!: ?Float64, color!: ?ResourceColor, offsetX!: ?Float64, offsetY!: ?Float64): T
```

**功能：** 为组件添加阴影效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|?Float64|是|-|**命名参数。** 阴影模糊半径。初始值：0.0|
|color|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|**命名参数。** 阴影颜色。初始值：Color(0x666666)|
|offsetX|?Float64|是|-|**命名参数。** 阴影X轴偏移量。初始值：0.0|
|offsetY|?Float64|是|-|**命名参数。** 阴影Y轴偏移量。初始值：0.0|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|

## func grayscale(?Float64)

```cangjie
func grayscale(value: ?Float64): T
```

**功能：** 为组件添加灰度效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float64|是|-|灰度值。值定义为灰度转换的比例，入参1.0则完全转为灰度图像，入参0.0则图像无变化，入参在0.0和1.0之间时，效果呈线性变化。取值范围：[0.0, 1.0]。初始值：0.0|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|

## func brightness(?Float64)

```cangjie
func brightness(value: ?Float64): T
```

**功能：** 为组件添加亮度效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float64|是|-|亮度值。初始值：1.0|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|

## func saturate(?Float64)

```cangjie
func saturate(value: ?Float64): T
```

**功能：** 为组件添加饱和度效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float64|是|-|饱和度值。初始值：1.0|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回调用此接口的组件实例本身。|