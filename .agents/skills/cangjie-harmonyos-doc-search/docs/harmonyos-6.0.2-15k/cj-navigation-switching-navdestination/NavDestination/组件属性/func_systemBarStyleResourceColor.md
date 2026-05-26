### func systemBarStyle(ResourceColor)

```cangjie
public func systemBarStyle(style: ResourceColor): This
```

**功能：** 当Navigation中显示Navigation首页时，设置对应系统状态栏的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|系统状态栏样式。|

> **说明：**
>
> - 必须配合Navigation使用，作为其Navigation目的页面的根节点时才能生效。
> - 其他使用限制请参考Navigation对应的[systemBarStyle](./cj-navigation-switching-navigation.md#func-systembarstyle)属性说明。