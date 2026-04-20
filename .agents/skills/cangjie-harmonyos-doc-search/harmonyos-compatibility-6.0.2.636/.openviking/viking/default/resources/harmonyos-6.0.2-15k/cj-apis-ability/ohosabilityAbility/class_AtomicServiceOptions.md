## class AtomicServiceOptions

```cangjie
public class AtomicServiceOptions <: StartOptions {
    public var flags: Int32 = 0
    public var parameters: String = ""

    public init()
}
```

**功能：** 作为[openAtomicService()](#func-openatomicservicestring-atomicserviceoptions-asynccallbackabilityresult)的入参，用于携带参数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**父类型：**

- [StartOptions](#class-startoptions)

### var flags

```cangjie
public var flags: Int32
```

**功能：** 系统处理该次启动的方式。
例如通过[wantConstant.Flags.FLAG_INSTALL_ON_DEMAND](#enum-flags)表示使用免安装能力。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var parameters

```cangjie
public var parameters: String
```

**功能：** 表示额外参数描述。具体描述参考[Want](#class-want)中[parameters](#prop-parameters)字段描述。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** AtomicServiceOptions的构造函数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19