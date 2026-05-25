## 通用属性/通用事件

通用属性：全部支持

通用事件：全部支持

## 组件属性

### func enableNestedScroll(Bool)

```cangjie
public func enableNestedScroll(value: Bool) : This
```

**功能：** 设置滚动条是否嵌套滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否执行嵌套滚动。设置为true执行嵌套滚动，设置为false不嵌套滚动。<br/>初始值：false。|

> **说明：**
>
> 滚动条使能嵌套滚动时，滚动条的滚动偏移量会先发给绑定的内层滚动组件，内层滚动组件再根据设置的嵌套滚动优先级依次传递给外层父滚动组件。<br/>
> WaterFlow组件的布局模式为移动窗口式（SLIDING_WINDOW）时，不支持嵌套滚动。<br/>
> 设置嵌套滚动模式为PARALLEL时，父子组件同时滚动，需要开发者在onScrollFrameBegin中按照所需逻辑，自行设置父子组件滚动顺序。