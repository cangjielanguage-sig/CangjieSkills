## enum FaultType

```cangjie
public enum FaultType {
    | NO_SPECIFIC
    | CPP_CRASH
    | JS_CRASH
    | APP_FREEZE
    | ...
}
```

**功能：** 故障类型枚举。

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**起始版本：** 19

### APP_FREEZE

```cangjie
APP_FREEZE
```

**功能：** 应用程序卡死故障类型。

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**起始版本：** 19

### CPP_CRASH

```cangjie
CPP_CRASH
```

**功能：** C++程序故障类型。

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**起始版本：** 19

### JS_CRASH

```cangjie
JS_CRASH
```

**功能：** JS程序故障类型。

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**起始版本：** 19

### NO_SPECIFIC

```cangjie
NO_SPECIFIC
```

**功能：** 不区分故障类型。

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**起始版本：** 19

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.HiviewDFX.Hiview.FaultLogger

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|枚举的值。|