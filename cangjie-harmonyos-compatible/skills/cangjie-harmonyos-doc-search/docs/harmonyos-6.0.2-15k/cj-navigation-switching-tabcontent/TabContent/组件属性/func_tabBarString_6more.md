### func tabBar(String)

```cangjie
public func tabBar(content: String): This
```

**功能：** 设置TabBar上显示内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|String|是|-|TabBar上显示内容。|

### func tabBar(AppResource)

```cangjie
public func tabBar(content: AppResource): This
```

**功能：** 设置TabBar上显示内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12
**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|TabBar上显示内容。|

### func tabBar(String, String)

```cangjie
public func tabBar(icon!: String, text!: String): This
```

**功能：** 设置TabBar上显示内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|String|是|-| **命名参数。** TabBar上显示的图标。<br> **说明：** 如果icon采用svg格式图源，则要求svg图源删除其自有宽高属性值。如采用带有自有宽高属性的svg图源，icon大小则是svg本身内置的宽高属性值大小。|
|text|String|是|-| **命名参数。** TabBar上显示的文字内容。|

### func tabBar(AppResource, String)

```cangjie
public func tabBar(icon!: AppResource, text!: String): This
```

**功能：** 设置TabBar上显示内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 设置TabBar上显示内容。<br> **说明：** 如果icon采用svg格式图源，则要求svg图源删除其自有宽高属性值。如采用带有自有宽高属性的svg图源，icon大小则是svg本身内置的宽高属性值大小。|
|text|String|是|-| **命名参数。** TabBar上显示的文字内容。|

### func tabBar(String, AppResource)

```cangjie
public func tabBar(icon!: String, text!: AppResource): This
```

**功能：** 设置TabBar上显示内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|String|是|-| **命名参数。** 设置TabBar上显示内容。<br> **说明：** 如果icon采用svg格式图源，则要求svg图源删除其自有宽高属性值。如采用带有自有宽高属性的svg图源，icon大小则是svg本身内置的宽高属性值大小。|
|text|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** TabBar上显示的文字内容。|

### func tabBar(AppResource, AppResource)

```cangjie
public func tabBar(icon!: AppResource, text!: AppResource): This
```

**功能：** 设置TabBar上显示内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 设置TabBar上显示内容。<br> **说明：** 如果icon采用svg格式图源，则要求svg图源删除其自有宽高属性值。如采用带有自有宽高属性的svg图源，icon大小则是svg本身内置的宽高属性值大小。|
|text|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** TabBar上显示的文字内容。|