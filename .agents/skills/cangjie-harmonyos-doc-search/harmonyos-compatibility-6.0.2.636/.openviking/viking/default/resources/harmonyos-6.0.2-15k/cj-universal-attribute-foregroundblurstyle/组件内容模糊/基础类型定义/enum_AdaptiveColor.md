### enum AdaptiveColor

```cangjie
public enum AdaptiveColor {
    | DEFAULT
    | AVERAGE
}
```

**功能：** 取色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### DEFAULT

```cangjie
DEFAULT
```

**功能：** 不使用取色模糊。使用默认的颜色作为蒙版颜色。采用非DEFAULT方式较耗时。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### AVERAGE

```cangjie
AVERAGE
```

**功能：** 使用取色模糊。将取色区域的颜色平均值作为蒙版颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12