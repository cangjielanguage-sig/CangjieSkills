### func multiSelectable(Bool)

```cangjie
public func multiSelectable(flag: Bool): This
```

**功能：** 是否开启鼠标框选。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|flag|Bool|是|-|是否开启鼠标框选。<br/>初始值：false，关闭框选。true，开启框选。|

### func scrollSnapAlign(ScrollSnapAlign)

```cangjie
public func scrollSnapAlign(value: ScrollSnapAlign): This
```

**功能：** 设置列表项滚动结束对齐效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ScrollSnapAlign](#enum-scrollsnapalign)|是|-|列表项滚动结束对齐效果。<br/>初始值：ScrollSnapAlign.NONE。|

### func sticky(StickyStyle)

```cangjie
public func sticky(value: StickyStyle): This
```

**功能：** 配合[ListItemGroup](./cj-scroll-swipe-listgroup.md)组件使用，设置ListItemGroup中header和footer是否要吸顶或吸底。sticky属性可以设置为 StickyStyle.Header | StickyStyle.Footer 以同时支持header吸顶和footer吸底。

> **说明：**
>
> 由于浮点数计算精度，设置sticky后，在List滑动过程中小概率产生缝隙，可以通过[pixelRound](./cj-common-types.md#enum-pixelroundcalcpolicy)指定当前组件向下像素取整解决该问题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[StickyStyle](./cj-common-types.md#enum-stickystyle)|是|-|ListItemGroup吸顶或吸底效果。<br/>初始值：StickyStyle.None。|