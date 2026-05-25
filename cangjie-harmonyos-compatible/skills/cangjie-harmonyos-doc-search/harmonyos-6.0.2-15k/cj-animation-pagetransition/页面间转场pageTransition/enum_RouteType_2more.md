## enum RouteType

```cangjie
public enum RouteType {
    | None
    | Push
    | Pop
}
```

**功能：** 页面路由类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### None

```cangjie
None
```

**功能：** 设置页面未重定向。

> **说明：**
>
> 如Push和Pop描述中RouteType为None的情形，即页面进场时PageTransitionEnter的转场效果生效；退场时PageTransitionExit的转场效果生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Pop

```cangjie
Pop
```

**功能：** 设置重定向指定页面。

> **说明：**
>
> 从PageB回退到之前的页面PageA。对于PageB，指定RouteType为None或者Pop的PageTransitionExit组件样式生效，对于PageA，指定RouteType为None或者Pop的PageTransitionEnter组件样式生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Push

```cangjie
Push
```

**功能：** 设置跳转到下一页面。

> **说明：**
>
> PageA跳转到下一个新的界面PageB。对于PageA，指定RouteType为None或者Push的PageTransitionExit组件样式生效，对于PageB，指定RouteType为None或者Push的PageTransitionEnter组件样式生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum SlideEffect

```cangjie
public enum SlideEffect {
    | Left
    | Right
    | Top
    | Bottom
    | START
    | END
}
```

**功能：** 页面滑动效果类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Bottom

```cangjie
Bottom
```

**功能：** 设置到入场时表示从下边滑入，出场时表示滑出到下边。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### END

```cangjie
END
```

**功能：** 设置LTR入场时表示从右边滑入，出场时表示滑出到右边。RTL入场时表示从左边滑入，出场时表示滑出到左边。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Left

```cangjie
Left
```

**功能：** 设置到入场时表示从左边滑入，出场时表示滑出到左边。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Right

```cangjie
Right
```

**功能：** 设置到入场时表示从右边滑入，出场时表示滑出到右边。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### START

```cangjie
START
```

**功能：** 设置LTR入场时表示从左边滑入，出场时表示滑出到左边。RTL入场时表示从右边滑入，出场时表示滑出到右边。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Top

```cangjie
Top
```

**功能：** 设置到入场时表示从上边滑入，出场时表示滑出到上边。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12