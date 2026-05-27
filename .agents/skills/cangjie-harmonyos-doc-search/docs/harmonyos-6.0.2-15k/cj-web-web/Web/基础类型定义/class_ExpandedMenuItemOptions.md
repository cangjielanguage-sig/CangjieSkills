### class ExpandedMenuItemOptions

```cangjie
public class ExpandedMenuItemOptions {
    public var content: String
    public var startIcon:?String = None
    public var action:(String) -> Unit
    public init(content!: String, startIcon!: ?String = None, action!: (String) -> Unit)
    public init(content!: AppResource, startIcon!: ?AppResource = None, action!: (String) -> Unit)
}
```

**功能：** 描述自定义菜单扩展项的参数结构。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### var action

```cangjie
public var action:(String) -> Unit
```

**功能：** 选中的文本信息。

**类型：** (String)->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### var content

```cangjie
public var content: String
```

**功能：** 显示内容。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### var startIcon

```cangjie
public var startIcon: ?String = None
```

**功能：** 显示图标。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### init(String, ?String, (String) -> Unit)

```cangjie
public init(content!: String, startIcon!: ?String = None, action!: (String) -> Unit)
```

**功能：** 创建自定义菜单扩展项。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|String|是|-| **命名参数。** 显示内容。|
|startIcon|?String|否|None| **命名参数。** 显示图标。|
|action|(String)->Unit|是|-| **命名参数。** 选中的文本信息。|

#### init(AppResource, ?AppResource, (String) -> Unit)

```cangjie
public init(content!: AppResource, startIcon!: ?AppResource = None, action!: (String) -> Unit)
```

**功能：** 创建自定义菜单扩展项。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 显示内容。|
|startIcon|?[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|否|None| **命名参数。** 显示图标。|
|action|(String)->Unit|是|-| **命名参数。** 选中的文本信息。|