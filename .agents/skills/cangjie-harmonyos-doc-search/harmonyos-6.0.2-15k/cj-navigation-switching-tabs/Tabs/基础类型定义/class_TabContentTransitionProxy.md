### class TabContentTransitionProxy

```cangjie
public class TabContentTransitionProxy {}
```

**功能：** Tabs自定义切换动画执行过程中，返回给开发者的proxy对象。开发者可通过该对象获取自定义动画的起始和目标页面信息，同时，也可以通过调用该对象的finishTransition接口通知Tabs组件自定义动画已结束。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let from

```cangjie
public let from: Int32
```

**功能：** 自定义动画起始页面对应的index值，索引从0开始。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

#### let to

```cangjie
public let to: Int32
```

**功能：** 自定义动画目标页面对应的index值，索引从0开始。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

#### func finishTransition()

```cangjie
public func finishTransition(): Unit
```

**功能：** 通知Tabs组件，此页面的自定义动画已结束。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19