# ohos.skill

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

skill模块介绍了skill标签对象。

## 导入模块

```cangjie
import kit.AbilityKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](./cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## class Skill

```cangjie
public class Skill {
    public let actions: Array<String>
    public let entities: Array<String>
    public let uris: Array<SkillUri>
    public let domainVerify: Bool
}
```

**功能：** skill标签对象，可以通过[getBundleInfoForSelf](./cj-apis-bundle_manager.md#static-func-getbundleinfoforselfint32)获取skill信息，其中入参bundleFlags至少包含 GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY 和 GET_BUNDLE_INFO_WITH_SKILL。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let actions

```cangjie
public let actions: Array<String>
```

**功能：** Skill接收的Action集合。

**类型：** Array\<String>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let domainVerify

```cangjie
public let domainVerify: Bool
```

**功能：** Skill接收的DomainVerify值，仅在AbilityInfo中存在，表示是否开启域名校验，取值为true表示开启域名校验，取值为false表示未开启域名校验。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let entities

```cangjie
public let entities: Array<String>
```

**功能：** Skill接收的Entity集合。

**类型：** Array\<String>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let uris

```cangjie
public let uris: Array<SkillUri>
```

**功能：** Want匹配的Uri集合。

**类型：** Array\<[SkillUri](#class-skilluri)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22