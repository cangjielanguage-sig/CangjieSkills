# MenuItem

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

用来展示菜单Menu中具体的item菜单项。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(() -> Unit)

```cangjie
public init(child!: () -> Unit = {=>}) 
```

**功能：** 构造一个有二级菜单的 item 菜单项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|() -> Unit|否|{=>}|**命名参数。** 自定义UI描述。使用时结合[@Builder](../../arkui-cj/paradigm/cj-macro-builder.md)和[bind](cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|

### init(?ResourceStr, ?ResourceStr, ?ResourceStr, ?ResourceStr, Option\<() -> Unit>)

```cangjie
public init(startIcon!: ?ResourceStr, content!: ?ResourceStr, endIcon!: ?ResourceStr, labelInfo!: ?ResourceStr,
    builder!: Option<() -> Unit> = None)
```

**功能：**构造一个有二级菜单的 item 菜单项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|startIcon|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|**命名参数。** item中显示在左侧的图标信息路径。初始值：""。|
|content|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|**命名参数。** item的内容信息。初始值：""。|
|endIcon|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-| **命名参数。** item中显示在右侧的图标信息路径。初始值：""。|
|labelInfo|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|**命名参数。** 定义结束标签信息，如快捷方式Ctrl+C等。初始值：""。|
|builder|Option\<() -> Unit>|否|None|**命名参数。** 自定义UI描述。使用时结合[@Builder](../../arkui-cj/paradigm/cj-macro-builder.md)和[bind](cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。