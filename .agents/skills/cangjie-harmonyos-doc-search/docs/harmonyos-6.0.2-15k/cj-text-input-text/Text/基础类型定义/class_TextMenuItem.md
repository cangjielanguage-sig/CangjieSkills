### class TextMenuItem

```cangjie
public class TextMenuItem {
    public var content: String
    public var icon: String
    public var id: TextMenuItemId
    public init(content!: String, icon!: String = '', id!: TextMenuItemId)
    public init(content!: String, icon!: AppResource, id!: TextMenuItemId)
    public init(content!: AppResource, icon!: AppResource, id!: TextMenuItemId)
}
```

**功能：** 文本菜单项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var content

```cangjie
public var content: String
```

**功能：** 表示菜单名称。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var icon

```cangjie
public var icon: String
```

**功能：** 表示菜单图标。不支持网络图片。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var id

```cangjie
public var id: TextMenuItemId
```

**功能：** 表示菜单id。

**类型：** [TextMenuItemId](#class-textmenuitemid)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(AppResource, AppResource, TextMenuItemId)

```cangjie
public init(content!: AppResource, icon!: AppResource, id!: TextMenuItemId)
```

**功能：** 创建TextMenuItem类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 菜单参数名。|
|icon|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 菜单图标。不支持网络图片。|
|id|[TextMenuItemId](#class-textmenuitemid)|是|-| **命名参数。** 菜单id。|

#### init(String, AppResource, TextMenuItemId)

```cangjie
public init(content!: String, icon!: AppResource, id!: TextMenuItemId)
```

**功能：** 创建TextMenuItem类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|String|是|-| **命名参数。** 菜单名称。|
|icon|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 菜单图标。不支持网络图片。|
|id|[TextMenuItemId](#class-textmenuitemid)|是|-| **命名参数。** 菜单id。|

#### init(String, String, TextMenuItemId)

```cangjie
public init(content!: String, icon!: String = '', id!: TextMenuItemId)
```

**功能：** 创建TextMenuItem类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|String|是|-| **命名参数。** 菜单名称。|
|icon|String|否|""| **命名参数。** 菜单图标。不支持网络图片。|
|id|[TextMenuItemId](#class-textmenuitemid)|是|-| **命名参数。** 菜单id。|