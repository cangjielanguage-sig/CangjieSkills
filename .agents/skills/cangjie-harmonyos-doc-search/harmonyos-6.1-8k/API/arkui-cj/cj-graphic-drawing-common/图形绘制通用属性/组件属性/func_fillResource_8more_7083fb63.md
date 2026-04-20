### func fill(?ResourceColor)

```cangjie
public func fill(value: ?ResourceColor): T
```

**功能：** 设置填充区域的颜色，异常值按照初始值处理。与通用属性[foregroundColor](./cj-universal-attribute-foregroundcolor.md#func-foregroundcolorcoloringstrategy)同时设置时，后设置的属性生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|填充颜色。初始值：Color.Black。|

### func fillOpacity(?Float64)

```cangjie
public func fillOpacity(value: ?Float64): T
```

**功能：** 设置填充区域透明度。取值范围是[0.0,1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0，其余异常值按1.0处理。取值为1.0代表不透明，取值为0.0代表完全透明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float64|是|-|填充透明度。初始值：1.0。|

### func fillOpacity(?AppResource)

```cangjie
public func fillOpacity(value: ?AppResource): T
```

**功能：** 设置填充区域透明度。取值范围是[0, 1]，若给定值小于0，则取值为0；若给定值大于1，则取值为1，其余异常值按1处理。取值为1代表不透明，取值为0代表完全透明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[AppResource](../LocalizationKit/cj-apis-resource.md#class-appresource)|是|-|填充透明度。初始值：1.0。|

### func stroke(?ResourceColor)

```cangjie
public func stroke(value: ?ResourceColor): T
```

**功能：** 设置边框颜色。默认没有边框。异常值不会绘制边框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|边框颜色。初始值：Color.Transparent。|

### func strokeDashArray(?Array\<Length>)

```cangjie
public func strokeDashArray(value: ?Array<Length>): T
```

**功能：** 设置边框间隙。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Array\<[Length](./cj-common-types.md#interface-length)>|是|-|边框虚线数组。初始值：[]。|

### func strokeDashOffset(?Length)

```cangjie
public func strokeDashOffset(value: ?Length): T
```

**功能：** 设置边框绘制起点的偏移量。异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|边框虚线偏移量。初始值：0.vp。|

### func strokeLineCap(?LineCapStyle)

```cangjie
public func strokeLineCap(value: ?LineCapStyle): T
```

**功能：** 设置边框端点绘制样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[LineCapStyle](./cj-common-types.md#enum-linecapstyle)|是|-|边框线帽样式。初始值：LineCapStyle.Butt。|

### func strokeLineJoin(?LineJoinStyle)

```cangjie
public func strokeLineJoin(value: ?LineJoinStyle): T
```

**功能：** 设置边框拐角绘制样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[LineJoinStyle](./cj-common-types.md#enum-linejoinstyle)|是|-|边框连接点样式。初始值：LineJoinStyle.Miter。|