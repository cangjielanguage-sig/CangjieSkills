# ohos.file.fileuri（文件URI）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

fileuri模块提供通过PATH获取文件统一资源标志符（Uniform Resource Identifier，URI）的能力，后续可通过使用[ohos.file_fs（文件管理）](cj-apis-file_fs.md)进行相关操作，如open、read、write等，以实现文件分享。

## 导入模块

```cangjie
import kit.CoreFileKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func getUriFromPath(String)

```cangjie
public func getUriFromPath(path: String): String
```

**功能：** 通过传入的路径path生成应用自己的URI；将path转URI时，路径中的中文及非数字字母的特殊字符将会被编译成对应的ASCII码，拼接在URI中。

**系统能力：** SystemCapability.FileManagement.AppFileService

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|文件的沙箱路径。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回文件URI。|

**异常：**

- BusinessException：对应错误码如下表，详见[文件管理错误码](./cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900020 | Invalid argument. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CoreFileKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let uri = getUriFromPath("test.txt")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```