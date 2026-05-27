# FlowItem

[瀑布流组件](./cj-scroll-swipe-waterflow.md)的子组件，用来展示瀑布流具体item。

> **说明：**
>
> 仅支持作为[Waterflow](./cj-scroll-swipe-waterflow.md)组件的子组件使用。

## 子组件

支持单个子组件。

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建瀑布流组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建包含子组件的瀑布流组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|声明容器内的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 示例代码

见[WaterFlow组件示例](./cj-scroll-swipe-waterflow.md#示例代码)。
