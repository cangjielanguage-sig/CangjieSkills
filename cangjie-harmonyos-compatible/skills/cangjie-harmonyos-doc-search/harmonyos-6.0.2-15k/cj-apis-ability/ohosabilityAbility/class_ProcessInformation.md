## class ProcessInformation

```cangjie
public class ProcessInformation {
    public ProcessInformation(
        public let pid: Int32,
        public let uid: Int32,
        public let processName: String,
        public let bundleNames: Array<String>,
        public let state: ProcessState,
        public let bundleType: BundleType,
        public let appCloneIndex: Int32
    )
}
```

**功能：** 提供对进程运行信息进行查询的能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### let appCloneIndex

```cangjie
public let appCloneIndex: Int32
```

**功能：** 应用分身索引。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let bundleNames

```cangjie
public let bundleNames: Array<String>
```

**功能：** 进程中所有运行的Bundle名称。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 19

### let bundleType

```cangjie
public let bundleType: BundleType
```

**功能：** 进程中所有运行的Bundle类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [BundleType](./cj-apis-bundle_manager.md#enum-bundletype)

**读写能力：** 只读

**起始版本：** 19

### let pid

```cangjie
public let pid: Int32
```

**功能：** 进程ID。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let processName

```cangjie
public let processName: String
```

**功能：** 进程名称。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let state

```cangjie
public let state: ProcessState
```

**功能：** 当前进程运行状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [ProcessState](#enum-processstate)

**读写能力：** 只读

**起始版本：** 19

### let uid

```cangjie
public let uid: Int32
```

**功能：** 用户ID。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### ProcessInformation(Int32, Int32, String, Array\<String>, ProcessState, BundleType, Int32)

```cangjie
public ProcessInformation(
    public let pid: Int32,
    public let uid: Int32,
    public let processName: String,
    public let bundleNames: Array<String>,
    public let state: ProcessState,
    public let bundleType: BundleType,
    public let appCloneIndex: Int32
)
```

**功能：** ProcessInformation实例构造。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pid|Int32|是|-|进程ID。|
|uid|Int32|是|-|用户ID。|
|processName|String|是|-|进程名称。|
|bundleNames|Array\<String>|是|-|进程中所有运行的Bundle名称。|
|state|[ProcessState](#enum-processstate)|是|-|当前进程运行状态。|
|bundleType|[BundleType](./cj-apis-bundle_manager.md#enum-bundletype)|是|-|进程中所有运行的Bundle类型。|
|appCloneIndex|Int32|是|-|应用分身索引。|