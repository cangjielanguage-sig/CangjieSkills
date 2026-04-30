### enum NavigationTitleMode

```cangjie
public enum NavigationTitleMode {
    | Free
    | Full
    | Mini
}
```

**功能：** 路由栈操作模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### Free

```cangjie
Free
```

**功能：** 当内容为满一屏的可滚动组件时，标题随着内容向上滚动而缩小（子标题的大小不变、淡出）。向下滚动内容到顶时则恢复原样。

**起始版本：** 20

> **说明：**
>
> - 标题随着内容滚动大小联动的动效在title设置为ResourceStr和NavigationCommonTitle时生效，设置成其余自定义节点类型时字体样式无法变化，下拉时只影响标题栏偏移。
> - 可滚动组件不满一屏时，如果想使用联动效果，就要使用滚动组件提供的[edgeEffect](./cj-scroll-swipe-list.md#func-edgeeffectedgeeffect)接口将options参数设置为true。未滚动状态，标题栏高度与Full模式一致；滚动时，标题栏的最小高度与Mini模式一致。

#### Full

```cangjie
Full
```

**功能：** 固定为大标题模式。初始值：只有主标题时，标题栏高度为112.vp；同时有主标题和副标题时，标题栏高度为138.vp。

**起始版本：** 20

#### Mini

```cangjie
Mini
```

**功能：** 固定为小标题模式。初始值：只有主标题时，标题栏高度为56.vp；同时有主标题和副标题时，标题栏高度为82.vp。

**起始版本：** 20

### enum BarStyle

```cangjie
public enum BarStyle {
    | Standard
    | Stack
}
```

**功能：** 标题栏与内容栏布局模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### Standard

```cangjie
Standard
```

**功能：** 标题栏与内容区采用上下布局。

**起始版本：** 20

#### Stack

```cangjie
Stack
```

**功能：** 标题栏与内容区采用层叠布局，标题栏布局在内容区上层。

**起始版本：** 20