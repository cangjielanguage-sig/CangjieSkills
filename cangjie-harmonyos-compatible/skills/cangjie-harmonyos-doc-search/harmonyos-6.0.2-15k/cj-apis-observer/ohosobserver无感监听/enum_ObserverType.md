## enum ObserverType

```cangjie
public enum ObserverType <: ToString {
    | OBSERVER_NAV_DESTINATION_UPDATE
    | OBSERVER_SCROLL_EVENT
    | OBSERVER_ROUTER_PAGE_UPDATE
    | OBSERVER_DENSITY_UPDATE
    | OBSERVER_WILL_DRAW
    | OBSERVER_DID_LAYOUT
    | OBSERVER_NAV_DESTINATION_SWITCH
    | OBSERVER_TAB_CONTENT_UPDATE
}
```

**功能：** 监听事件类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- ToString

### OBSERVER_DENSITY_UPDATE

```cangjie
OBSERVER_DENSITY_UPDATE
```

**功能：** 屏幕像素密度变化事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OBSERVER_DID_LAYOUT

```cangjie
OBSERVER_DID_LAYOUT
```

**功能：** 每一帧布局完成事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OBSERVER_NAV_DESTINATION_SWITCH

```cangjie
OBSERVER_NAV_DESTINATION_SWITCH
```

**功能：** Navigation的页面切换事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OBSERVER_NAV_DESTINATION_UPDATE

```cangjie
OBSERVER_NAV_DESTINATION_UPDATE
```

**功能：** NavDestination组件的状态变化事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OBSERVER_ROUTER_PAGE_UPDATE

```cangjie
OBSERVER_ROUTER_PAGE_UPDATE
```

**功能：** router中page页面的状态变化事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OBSERVER_SCROLL_EVENT

```cangjie
OBSERVER_SCROLL_EVENT
```

**功能：** 滚动事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OBSERVER_TAB_CONTENT_UPDATE

```cangjie
OBSERVER_TAB_CONTENT_UPDATE
```

**功能：** TabContent页面的切换事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OBSERVER_WILL_DRAW

```cangjie
OBSERVER_WILL_DRAW
```

**功能：** 每一帧绘制指令下发事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将事件类型枚举值转换成字符串类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|事件类型。|