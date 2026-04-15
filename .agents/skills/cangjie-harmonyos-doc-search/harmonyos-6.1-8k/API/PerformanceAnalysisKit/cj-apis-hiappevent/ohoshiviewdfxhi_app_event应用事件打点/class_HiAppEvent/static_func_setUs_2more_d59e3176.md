### static func setUserId(String, String)

```cangjie
public static func setUserId(name: String, value: String): Unit
```

**功能：** 设置用户ID值。用于在配置[Processor](#class-processor)数据处理者时进行关联。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|用户ID的key。只能包含大小写字母、数字、下划线和 $，不能以数字开头，长度非空且不超过256个字符。|
|value|String|是|-|用户ID的值。长度不超过256，当值为空字符串时，则清除用户ID。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    HiAppEvent.setUserId("test_getUserId_name", "test_getUserId_value")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func setUserProperty(String, String)

```cangjie
public static func setUserProperty(name: String, value: String): Unit
```

**功能：** 设置用户属性值。用于在配置[Processor](#class-processor)数据处理者时进行关联。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|用户属性的key。只能包含大小写字母、数字、下划线和 $，不能以数字开头，长度非空且不超过256个字符。|
|value|String|是|-|用户属性的值。长度不超过1024，当值为空字符串时，则清除用户属性。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    HiAppEvent.setUserProperty("test_setUserProperty_name", "test_setUserProperty_value")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```