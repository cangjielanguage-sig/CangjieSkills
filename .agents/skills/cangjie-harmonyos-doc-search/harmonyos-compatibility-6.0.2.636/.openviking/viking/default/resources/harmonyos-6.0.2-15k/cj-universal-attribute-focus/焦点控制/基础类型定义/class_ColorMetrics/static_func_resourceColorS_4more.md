#### static func resourceColor(String)

```cangjie
public static func resourceColor(color: String): ColorMetrics
```

**功能：** 使用rgb或者argb格式颜色实例化 ColorMetrics 类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :---- | :---- | :--- | :----- | :----------- |
| color | String | 是   | \- | rgb或者argb格式颜色。 |

**返回值：**

|类型|说明|
| :-------   | :---------- |
| [ColorMetrics](./cj-universal-attribute-focus.md#class-colormetrics) | ColorMetrics 类的实例。|

#### static func resourceColor(AppResource)

```cangjie
public static func resourceColor(color: AppResource): ColorMetrics
```

**功能：** 使用系统资源或者应用资源中的颜色实例化 ColorMetrics 类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :---- | :---- | :--- | :----- | :----------- |
| color | [AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource) | 是   | \- | 系统资源或者应用资源中的颜色。 |

**返回值：**

|类型|说明|
| :-------   | :---------- |
| [ColorMetrics](./cj-universal-attribute-focus.md#class-colormetrics) | ColorMetrics 类的实例。|

#### func blendColor(ColorMetrics)

```cangjie
public func blendColor(overlayColor: ColorMetrics): ColorMetrics
```

**功能：** 混合颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :---- | :---- | :--- | :----- | :----------- |
| overlayColor | [ColorMetrics](./cj-universal-attribute-focus.md#class-colormetrics) | 是   | \- | 叠加颜色的 ColorMetrics 类的实例。 |

**返回值：**

|类型|说明|
| :-------   | :---------- |
| [ColorMetrics](./cj-universal-attribute-focus.md#class-colormetrics) | ColorMetrics 类的实例。|

#### func toUInt32()

```cangjie
public func toUInt32(): UInt32
```

**功能：** 获取ColorMetrics的颜色的整数格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
| :-------   | :---------- |
| UInt32 | ColorMetrics的颜色的整数格式。|