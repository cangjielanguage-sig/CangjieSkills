### func stroke(ResourceColor)

```cangjie
public func stroke(color: ResourceColor): This
```

**功能：** 设置边框颜色。默认没有边框。异常值不会绘制边框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|边框颜色。|

### func strokeDashArray(Array\<Length>)

```cangjie
public func strokeDashArray(dashArray: Array<Length>): This
```

**功能：** 设置边框间隙。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dashArray|Array\<[Length](./cj-common-types.md#interface-length)>|是|-|边框间隙。初始值：[]，单位：vp。<br>取值范围≥0，异常值按照初始值处理。|

### func strokeDashOffset(Length)

```cangjie
public func strokeDashOffset(dashOffset: Length): This
```

**功能：** 设置边框绘制起点的偏移量。异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dashOffset|[Length](./cj-common-types.md#interface-length)|是|-|边框绘制起点的偏移量。<br>初始值：0。<br>单位：vp。|

### func strokeLineCap(LineCapStyle)

```cangjie
public func strokeLineCap(lineCap: LineCapStyle): This
```

**功能：** 设置边框端点绘制样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|lineCap|[LineCapStyle](./cj-common-types.md#enum-linecapstyle)|是|-|边框端点绘制样式。<br>初始值：LineCapStyle.Butt。|

### func strokeLineJoin(LineJoinStyle)

```cangjie
public func strokeLineJoin(lineJoin: LineJoinStyle): This
```

**功能：** 设置边框拐角绘制样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|lineJoin|[LineJoinStyle](./cj-common-types.md#enum-linejoinstyle)|是|-|边框拐角绘制样式。<br>初始值：LineJoinStyle.Miter。|

### func strokeMiterLimit(Float64)

```cangjie
public func strokeMiterLimit(miterLimit: Float64): This
```

**功能：** 设置斜接长度与边框宽度比值的极限值。斜接长度表示外边框外边交点到内边交点的距离，边框宽度即strokeWidth属性的值。该属性取值需在strokeLineJoin属性取值LineJoinStyle.Miter时生效。<br>该属性的合法值范围应当大于等于1.0，当取值范围在[0,1)时按1.0处理，其余异常值按初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|miterLimit|Float64|是|-|斜接长度与边框宽度比值的极限值。<br>初始值：4.0。|

### func strokeMiterLimit(Int64)

```cangjie
public func strokeMiterLimit(miterLimit: Int64): This
```

**功能：** 设置斜接长度与边框宽度比值的极限值。斜接长度表示外边框外边交点到内边交点的距离，边框宽度即strokeWidth属性的值。该属性取值需在strokeLineJoin属性取值LineJoinStyle.Miter时生效。<br>该属性的合法值范围应当大于等于1，当取值范围在[0,1)时按1处理，其余异常值按初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|miterLimit|Int64|是|-|斜接长度与边框宽度比值的极限值。<br>初始值：4。|