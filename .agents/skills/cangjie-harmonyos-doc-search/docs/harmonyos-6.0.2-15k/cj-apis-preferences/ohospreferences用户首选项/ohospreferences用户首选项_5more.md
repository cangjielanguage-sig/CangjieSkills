# ohos.preferences（用户首选项）

用户首选项为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。

数据存储形式为键值对，键的类型为字符串型，值的存储数据类型包括数字型、字符型、布尔型以及这3种类型的数组类型。

## 导入模块

```cangjie
import kit.ArkData.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## let MAX_KEY_LENGTH

```cangjie
public let MAX_KEY_LENGTH = 1024
```

**功能：** Key的最大长度限制为1024个字节。

**类型：** Int64

**起始版本：** 12

## let MAX_VALUE_LENGTH

```cangjie
public let MAX_VALUE_LENGTH = 16 * 1024 * 1024
```

**功能：** Value的最大长度限制为16 * 1024 * 1024个字节。

**类型：** Int64

**起始版本：** 12