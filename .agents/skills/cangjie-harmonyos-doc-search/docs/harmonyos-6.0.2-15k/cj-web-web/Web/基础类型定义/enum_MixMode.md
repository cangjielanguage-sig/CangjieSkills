### enum MixMode

```cangjie
public enum MixMode {
    | All
    | Compatible
    | None

    public func getValue(): Int32 {
        match (this) {
            case All => 0
            case None => 1
            case Compatible => 2
        }
    }
}
```

**功能：** 设置是否允许加载超文本传输协议（HTTP）和超文本传输安全协议（HTTPS）混合内容，默认不允许加载HTTP和HTTPS混合内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### All

```cangjie
All
```

**功能：** 允许加载HTTP和HTTPS混合内容。所有不安全的内容都可以被加载。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Compatible

```cangjie
All
```

**功能：** 混合内容兼容性模式，部分不安全的内容可能被加载。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### None

```cangjie
All
```

**功能：** 不允许加载HTTP和HTTPS混合内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12