### func antiAlias(Bool)

```cangjie
public func antiAlias(antiAlias: Bool): This
```

**功能：** 设置是否开启抗锯齿效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|antiAlias|Bool|是|-|是否开启抗锯齿效果。<br>true：开启抗锯齿；false：关闭抗锯齿。<br>初始值：true。|

### func fill(ResourceColor)

```cangjie
public func fill(color: ResourceColor): This
```

**功能：** 设置填充区域的颜色，异常值按照初始值处理。与通用属性[foregroundColor](./cj-universal-attribute-foregroundcolor.md#func-foregroundcolorcoloringstrategy)同时设置时，后设置的属性生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|填充区域颜色。初始值：Color.BLACK。|

### func fillOpacity(Float64)

```cangjie
public func fillOpacity(value: Float64): This
```

**功能：** 设置填充区域透明度。取值范围是[0.0,1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0，其余异常值按1.0处理。取值为1.0代表不透明，取值为0.0代表完全透明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|填充区域透明度。<br>初始值：1.0。|

### func fillOpacity(Int64)

```cangjie
public func fillOpacity(value: Int64): This
```

**功能：** 设置填充区域透明度。取值范围是[0, 1]，若给定值小于0，则取值为0；若给定值大于1，则取值为1，其余异常值按1处理。取值为1代表不透明，取值为0代表完全透明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|-|填充区域透明度。<br>初始值：1。|

### func fillOpacity(AppResource)

```cangjie
public func fillOpacity(value: AppResource): This
```

**功能：** 设置填充区域透明度。取值范围是[0, 1]，若给定值小于0，则取值为0；若给定值大于1，则取值为1，其余异常值按1处理。取值为1代表不透明，取值为0代表完全透明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|填充区域透明度。|

### func height(Length)

```cangjie
public func height(value: Length): This
```

**功能：** 设置组件高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|组件高度。<br>单位：vp。|

### func size(Length, Length)

```cangjie
  public func size(width!: Length, height!: Length): This
 ```

**功能：** 设置组件宽高。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 组件宽度。<br>单位：vp。|
|height|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 组件高度。<br>单位：vp。|