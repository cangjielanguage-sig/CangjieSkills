### func strokeMiterLimit(?Float64)

```cangjie
public func strokeMiterLimit(miterLimit: ?Float64): T
```

**功能：** 设置斜接长度与边框宽度比值的极限值。斜接长度表示外边框外边交点到内边交点的距离，边框宽度即strokeWidth属性的值。该属性取值需在strokeLineJoin属性取值LineJoinStyle.Miter时生效。<br>该属性的合法值范围应当大于等于1.0，当取值范围在[0,1)时按1.0处理，其余异常值按初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|miterLimit|?Float64|是|-|斜接长度与边框宽度比值的极限值。<br>初始值：4.0。|

### func strokeOpacity(?Float64)

```cangjie
public func strokeOpacity(value: ?Float64): T
```

**功能：** 设置边框透明度。该属性的取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0，其余异常值按1.0处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float64|是|-|边框透明度。初始值：1.0。|

### func strokeOpacity(?AppResource)

```cangjie
public func strokeOpacity(value: ?AppResource): T
```

**功能：** 设置边框透明度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[AppResource](../LocalizationKit/cj-apis-resource.md#class-appresource)|是|-|边框透明度。初始值：1.0。|

### func strokeWidth(?Length)

```cangjie
public func strokeWidth(value: ?Length): T
```

**功能：** 设置边框宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|边框宽度。初始值：1.vp。|

### func antiAlias(?Bool)

```cangjie
public func antiAlias(value: ?Bool): T
```

**功能：** 设置是否开启抗锯齿。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|是否开启抗锯齿。初始值：true。|