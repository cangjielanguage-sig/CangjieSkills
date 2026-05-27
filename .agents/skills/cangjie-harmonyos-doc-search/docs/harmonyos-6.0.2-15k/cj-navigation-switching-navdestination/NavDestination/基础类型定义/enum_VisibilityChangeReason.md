### enum VisibilityChangeReason

```cangjie
public enum VisibilityChangeReason {
    | Transition
    | ContentCover
    | AppState
    | ...
}
```

**功能：** NavDestination可见性发生变化的原因。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 21

#### AppState

```cangjie
AppState
```

**功能：** 通过前后台切换使NavDestination可见性发生变化。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 21

#### ContentCover

```cangjie
ContentCover
```

**功能：** 通过全模态的开启和关闭使NavDestination可见性发生变化。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 21

#### Transition

```cangjie
Transition
```

**功能：** 通过页面跳转的方式使NavDestination可见性发生变化。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 21