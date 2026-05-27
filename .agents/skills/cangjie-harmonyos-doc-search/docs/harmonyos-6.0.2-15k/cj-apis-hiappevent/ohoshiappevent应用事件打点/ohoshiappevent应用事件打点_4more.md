# ohos.hiappevent（应用事件打点）

本模块提供了应用事件打点能力，包括应用事件落盘、应用事件订阅、应用事件清理、打点功能配置等功能。

## 导入模块

```cangjie
import kit.PerformanceAnalysisKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## class AppEventPackage

```cangjie
public class AppEventPackage {
    public let packageId: Int32
    public let row: Int32
    public let size: Int32
    public let data: Array<String>
    public init(packageId: Int32, row: Int32, size: Int32, data: Array<String>)
}
```

**功能：** 提供了订阅返回的应用事件包的参数定义。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### let data

```cangjie
public let data: Array<String>
```

**功能：** 事件包的事件信息。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### let packageId

```cangjie
public let packageId: Int32
```

**功能：** 事件包ID，从0开始自动递增。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let row

```cangjie
public let row: Int32
```

**功能：** 事件包的事件数量。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let size

```cangjie
public let size: Int32
```

**功能：** 事件包的事件大小，单位为byte。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### init(Int32, Int32, Int32, Array\<String>)

```cangjie
public init(packageId: Int32, row: Int32, size: Int32, data: Array<String>)
```

**功能：** 创建[AppEventPackage](#class-appeventpackage)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|packageId|Int32|是|-|事件包ID，从0开始自动递增。|
|row|Int32|是|-|事件包的事件数量。|
|size|Int32|是|-|事件包的事件大小，单位为byte。|
|data|Array\<String>|是|-|事件包的事件信息。|