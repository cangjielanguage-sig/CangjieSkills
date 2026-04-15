# ohos.request（上传下载）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

request模块给应用提供上传下载文件、后台代理传输的基础功能。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 权限列表

ohos.permission.INTERNET

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func create(UIAbilityContext, Config)

```cangjie
public func create(context: UIAbilityContext, config: Config): Task
```

**功能：** 创建需要上传或下载的任务，并将其排入队列。支持HTTP/HTTPS协议。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名  | 类型 | 必填 | 默认值 | 说明 |
| :------ | :------ | :------| :------ | :------ |
| context | [UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext) | 是   | -      | 基于应用程序的上下文。     |
| config  | [Config](#class-config)                                                                    | 是   | -      | 上传/下载任务的配置信息。 |

**返回值：**

| 类型                | 说明                                               |
| :------------------ | :------------------------------------------------- |
| [Task](#class-task) | 返回一个Task对象，里面包括任务id和任务的配置信息。 |

**异常：**

- BusinessException：对应错误码如下表，详见[上传下载错误码](./cj-errorcode-request.md)与[通用错误码说明文档](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 13400001 | Invalid file or file system error. |
  | 13400003 | Task service ability error. |
  | 13499999 | Other error. |
  | 21900004 | the application task queue is full. |
  | 21900005 | Operation with wrong task mode. |

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let context = Global.abilityContext
    let config = Config(
        Action.Download,
        "https://example.com/file.txt"
    )
    let task = create(context, config)
    Hilog.info(0, "test", "成功创建任务，任务ID: ${task.tid}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```