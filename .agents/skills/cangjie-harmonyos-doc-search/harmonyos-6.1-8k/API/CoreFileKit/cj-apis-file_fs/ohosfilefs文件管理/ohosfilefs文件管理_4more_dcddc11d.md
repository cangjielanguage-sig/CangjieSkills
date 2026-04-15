# ohos.file.fs（文件管理）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

fs模块提供基础文件操作能力，包括文件基本管理、文件目录管理、文件信息统计、文件流式读写等常用功能。

## 导入模块

```cangjie
import kit.CoreFileKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。
- 获取当前应用沙箱所在路径可通过UIAbilityContext.[filesDir](../AbilityKit/cj-apis-app-ability-ui_ability.md#prop-filesdir)获取。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## class ConflictFiles

```cangjie
public class ConflictFiles {
    public var srcFile: String
    public var destFile: String
}
```

**功能：** 冲突文件信息，支持copyDir及moveDir接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var destFile

```cangjie
public var destFile: String
```

**功能：** 目标冲突文件路径。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var srcFile

```cangjie
public var srcFile: String
```

**功能：** 源冲突文件路径。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22