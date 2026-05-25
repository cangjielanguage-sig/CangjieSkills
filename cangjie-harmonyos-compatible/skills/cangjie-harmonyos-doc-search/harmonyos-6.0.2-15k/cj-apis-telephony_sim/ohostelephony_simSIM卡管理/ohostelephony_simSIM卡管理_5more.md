# ohos.telephony_sim（SIM卡管理）

SIM卡管理模块提供了SIM卡管理的基础能力，包括获取指定卡槽SIM卡的ISO国家码、归属PLMN号、服务提供商名称、SIM卡状态、卡类型、是否插卡、是否激活等。

## 导入模块

```cangjie
import kit.TelephonyKit.*
```

## 权限列表

ohos.permission.GET_TELEPHONY_STATE

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## class IccAccountInfo

```cangjie
public class IccAccountInfo {}
```

**功能：** Icc账户信息。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### let iccId

```cangjie
public let iccId: String
```

**功能：** ICCID号码。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let isActive

```cangjie
public let isActive: Bool
```

**功能：** 卡是否被激活。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isEsim

```cangjie
public let isEsim: Bool
```

**功能：** 标记卡是否是eSIM。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let showName

```cangjie
public let showName: String
```

**功能：** SIM卡显示名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let showNumber

```cangjie
public let showNumber: String
```

**功能：** SIM卡显示号码。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let simId

```cangjie
public let simId: Int32
```

**功能：** SIM卡ID。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let slotIndex

```cangjie
public let slotIndex: Int32
```

**功能：** 卡槽ID。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19