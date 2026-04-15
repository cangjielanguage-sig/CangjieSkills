## class Hilog

```cangjie
public class Hilog {}
```

**功能：** 日志系统对象，使应用/服务可以按照指定级别、标识和格式字符串输出日志内容。提供DEBUG、INFO、WARNING、ERROR、FATAL不同级别的日志打印方法。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 22

### static func debug(UInt32, String, String, Array\<String>)

```cangjie
public static func debug(domain: UInt32, tag: String, format: String, args: Array<String>): Unit
```

**功能：** 打印DEBUG级别的日志。

DEBUG级别的日志在正式发布版本中默认不被打印，只有在调试版本或打开调试开关的情况下才会打印。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domain|UInt32|是|-|日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。<br/>建议开发者在应用内根据需要自定义划分。|
|tag|String|是|-|指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。|
|format|String|是|-|格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。<br>隐私标识分为{public}和{private}，缺省为{private}。标识{public}的内容明文输出，标识{private}的内容以\<private>过滤回显。|
|args|Array\<String>|是|-|与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    Hilog.debug(0, "testTag", "Debug: Hello world!")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func error(UInt32, String, String, Array\<String>)

```cangjie
public static func error(domain: UInt32, tag: String, format: String, args: Array<String>): Unit
```

**功能：** 打印ERROR级别的日志。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domain|UInt32|是|-|日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。<br/>建议开发者在应用内根据需要自定义划分。|
|tag|String|是|-|指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。 tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。|
|format|String|是|-|格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。<br/>隐私标识分为{public}和{private}，缺省为{private}。标识{public}的内容明文输出，标识{private}的内容以\<private>过滤回显。|
|args|Array\<String>|是|-|与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    Hilog.error(0, "testTag", "Error: Hello world!")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```