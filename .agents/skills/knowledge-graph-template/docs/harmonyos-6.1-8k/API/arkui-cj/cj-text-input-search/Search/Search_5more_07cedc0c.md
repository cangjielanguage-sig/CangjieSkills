# Search

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

提供搜索框组件，用于提供用户搜索内容的输入区域。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(?ResourceStr, ?ResourceStr, Option\<AppResource>, Option\<SearchController>)

```cangjie
public init(
    value!: ?ResourceStr = None,
    placeholder!: ?ResourceStr = None,
    icon!: Option<AppResource> = None,
    controller!: Option<SearchController> = None
)
```

**功能：** 创建Search组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 当前显示的搜索文本内容。初始值：""。|
|placeholder|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None|**命名参数。** 无输入时的提示文本。初始值：""。|
|icon|Option\<[AppResource](../LocalizationKit/cj-apis-resource.md#class-appresource)>|否|None|**命名参数。** 搜索图标路径，默认使用系统搜索图标。|
|controller|Option\<[SearchController](#class-searchcontroller)>|否|None|**命名参数。** Search组件控制器。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。