#### init(String, AppResource, String)

```cangjie
public init(shown!: String, hidden!: AppResource, switching!: String = "")
```

**功能：** 构造图标对象。

> **说明：**
>
> 资源获取错误时，使用默认图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|shown|String|是|-| **命名参数。** 侧边栏显示时控制按钮的图标。|
|hidden|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 侧边栏隐藏时控制按钮的图标。|
|switching|String|否|""| **命名参数。** 侧边栏显示和隐藏状态切换时控制按钮的图标。|

#### init(String, AppResource, AppResource)

```cangjie
public init(shown!: String, hidden!: AppResource, switching!: AppResource)
```

**功能：** 构造图标对象。

> **说明：**
>
> 资源获取错误时，使用默认图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|shown|String|是|-| **命名参数。** 侧边栏显示时控制按钮的图标。|
|hidden|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 侧边栏隐藏时控制按钮的图标。|
|switching|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 侧边栏显示和隐藏状态切换时控制按钮的图标。|

#### init(AppResource, AppResource, String)

```cangjie
public init(shown!: AppResource, hidden!: AppResource, switching!: String = "")
```

**功能：** 构造图标对象。

> **说明：**
>
> 资源获取错误时，使用默认图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|shown|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 侧边栏显示时控制按钮的图标。|
|hidden|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 侧边栏隐藏时控制按钮的图标。|
|switching|String|否|""| **命名参数。** 侧边栏显示和隐藏状态切换时控制按钮的图标。|

#### init(AppResource, AppResource, AppResource)

```cangjie
public init(shown!: AppResource, hidden!: AppResource, switching!: AppResource)
```

**功能：** 构造图标对象。

> **说明：**
>
> 资源获取错误时，使用默认图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|shown|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 侧边栏显示时控制按钮的图标。|
|hidden|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 侧边栏隐藏时控制按钮的图标。|
|switching|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 侧边栏显示和隐藏状态切换时控制按钮的图标。|