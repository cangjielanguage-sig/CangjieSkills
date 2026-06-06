### enum FocusPriority

```cangjie
public enum FocusPriority {
    | AUTO
    | PRIOR
    | PREVIOUS
}
```

**功能：** 获焦优先级。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### AUTO

```cangjie
AUTO
```

**功能：** 默认的优先级，缺省时组件的获焦优先级。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PRIOR

```cangjie
PRIOR
```

**功能：** 容器内优先获焦的优先级。优先级高于AUTO。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PREVIOUS

```cangjie
PREVIOUS
```

**功能：** 上一次容器整体失焦时获焦节点的优先级。优先级高于PRIOR。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19