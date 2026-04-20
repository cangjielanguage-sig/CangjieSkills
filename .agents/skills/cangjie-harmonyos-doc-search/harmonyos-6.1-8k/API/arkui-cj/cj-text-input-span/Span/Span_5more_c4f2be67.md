# Span

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

作为[Text](cj-text-input-text.md)组件的子组件，用于显示行内文本的组件。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(?ResourceStr)

```cangjie
public init(value: ?ResourceStr)
```

**功能：** 创建Span组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|文本内容。<br>初始值：""。|

## 通用属性/通用事件

通用属性：不支持。

通用事件：仅支持点击事件[onClick](#func-onclickclickevent---unit)。

> **说明：**
>
> 由于Span组件无尺寸信息，因此点击事件返回的ClickEvent对象的target属性无效。