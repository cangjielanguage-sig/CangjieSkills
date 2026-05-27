# Panel

可滑动面板，提供一种轻量的内容展示窗口，方便在不同尺寸中切换。

## 子组件

可以包含子组件。

## 创建组件

### init(Bool, () -> Unit)

```cangjie
public init(show: Bool, content: () -> Unit)
```

**功能：** 创建一个可滑动面板组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|show|Bool|是|-|控制Panel显示或隐藏。<br/>**说明：**<br/>如果设置为false时，则不占位隐藏。[Visible.None](./cj-universal-attribute-visibility.md)或者show之间有一个生效时，都会生效不占位隐藏。|
|content|()->Unit|是|-|声明容器子组件。|

## 通用属性/通用事件

通用属性：除文本样式外，其余全部支持。

通用事件：全部支持。