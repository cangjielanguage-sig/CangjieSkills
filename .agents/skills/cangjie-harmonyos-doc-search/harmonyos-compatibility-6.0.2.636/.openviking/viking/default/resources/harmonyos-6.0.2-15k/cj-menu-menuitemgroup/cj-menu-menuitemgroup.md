# MenuItemGroup

该组件用来展示菜单MenuItem的分组。

## 子组件

包含[MenuItem](./cj-menu-menuitem.md)子组件。

## 创建组件

### init(String, String, () -> Unit)

```cangjie
public init(header!: String, footer!: String, child!: () -> Unit = { => })
```

**功能：** 创建一个用来展示菜单MenuItem的分组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|header|String|是|-| **命名参数。** 设置对应group的标题显示信息。|
|footer|String|是|-| **命名参数。** 设置对应group的尾部显示信息。|
|child|()->Unit|否|{ => }| **命名参数。** 声明容器内的子组件。|

### init(AppResource, AppResource, () -> Unit)

```cangjie
public init(header!: AppResource, footer!: AppResource, child!: () -> Unit = { => })
```

**功能：** 创建一个用来展示菜单MenuItem的分组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|header|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 设置对应group的标题显示信息。|
|footer|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 设置对应group的尾部显示信息。|
|child|()->Unit|否|{ => }| **命名参数。** 声明容器内的子组件。|

### init(() -> Unit, () -> Unit, () -> Unit)

```cangjie
public init(header!: () -> Unit, footer!: () -> Unit, child!: () -> Unit = { => })
```

**功能：** 创建一个用来展示菜单MenuItem的分组。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|header|()->Unit|是|-| **命名参数。** 设置对应group的标题显示信息。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|
|footer|()->Unit|是|-| **命名参数。** 设置对应group的尾部显示信息。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|
|child|()->Unit|否|{ => }| **命名参数。** 声明容器内的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 示例代码

详见[Menu](cj-menu-menu.md#示例代码)组件示例。
