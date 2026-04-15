## enum TimeType

```cangjie
public enum TimeType {
    | Startup
    | Active
    | ...
}
```

**功能：** 定义获取时间的枚举类型。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 22

### Active

```cangjie
Active
```

**功能：** 自系统启动以来经过的毫秒数，不包括深度睡眠时间。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 22

### Startup

```cangjie
Startup
```

**功能：** 自系统启动以来经过的毫秒数，包括深度睡眠时间。

**系统能力：** SystemCapability.MiscServices.Time

**起始版本：** 22