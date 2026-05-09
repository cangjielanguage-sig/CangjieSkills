## 组件事件

### func onClick(?(ClickEvent) -> Unit)

```cangjie
public func onClick(event: ?(ClickEvent) -> Unit): This
```

**功能：** 点击事件回调函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|?([ClickEvent](./cj-common-types.md#class-clickevent)) -> Unit|是|-|点击事件回调函数，点击事件回调。<br>初始值：{ _ => }。|

## 基础类型定义

### class BaseSpan

```cangjie
public abstract class BaseSpan {}
```

**功能：** Span组件的基类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22