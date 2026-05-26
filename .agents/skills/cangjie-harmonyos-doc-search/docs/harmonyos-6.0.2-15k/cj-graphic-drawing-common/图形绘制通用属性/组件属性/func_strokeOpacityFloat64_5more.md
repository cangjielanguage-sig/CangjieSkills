### func strokeOpacity(Float64)

```cangjie
public func strokeOpacity(value: Float64): This
```

**功能：** 设置边框透明度。该属性的取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0，其余异常值按1.0处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|边框透明度。<br>初始值：1.0。|

### func strokeOpacity(Int64)

```cangjie
public func strokeOpacity(value: Int64): This
```

**功能：** 设置边框透明度。该属性的取值范围是[0, 1]，若给定值小于0，则取值为0；若给定值大于1，则取值为1，其余异常值按1处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|-|边框透明度。<br>初始值：1。|

### func strokeOpacity(AppResource)

```cangjie
public func strokeOpacity(value: AppResource): This
```

**功能：** 设置边框透明度，支持attributeModifier动态设置属性方法。该属性的取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|边框透明度。|

### func strokeWidth(Length)

```cangjie
public func strokeWidth(value: Length): This
```

**功能：** 设置边框宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|边框宽度。<br>初始值：1。<br>默认单位：vp。<br>暂不支持百分比，百分比按照1px处理。|

### func width(Length)

```cangjie
public func width(value: Length): This
```

**功能：** 设置组件宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|组件宽度。</br>单位：vp。|