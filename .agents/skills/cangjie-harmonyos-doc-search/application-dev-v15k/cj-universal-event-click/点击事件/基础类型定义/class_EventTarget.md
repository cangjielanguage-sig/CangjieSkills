### class EventTarget

```cangjie
public class EventTarget {
    public EventTarget(public var area: Area)
}
```

**功能：** 触发事件的元素对象显示区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var area

```cangjie
public var area: Area
```

**功能：** 定义目标区域。

**类型：** [Area](./cj-common-types.md#class-area)

**读写能力：** 可读写

**起始版本：** 19

#### EventTarget(Area)

```cangjie
public EventTarget(public var area: Area)
```

**功能：** 构造一个EventTarget类型的对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|area|[Area](./cj-common-types.md#class-area)|是|-|目标元素的区域信息。|