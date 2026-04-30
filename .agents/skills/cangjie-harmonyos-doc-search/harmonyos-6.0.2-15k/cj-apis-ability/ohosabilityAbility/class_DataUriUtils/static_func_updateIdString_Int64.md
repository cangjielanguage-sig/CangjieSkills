### static func updateId(String, Int64)

```cangjie
public static func updateId(uri: String, id: Int64): String
```

**功能：** 更新指定uri中的ID。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|表示uri对象。|
|id|Int64|是|-|表示要更新的ID。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回更新ID之后的uri对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.base.*

let id = 999
try {
    let retUri = DataUriUtils.updateId("com.example.dataUriUtils/123", id)
} catch(e: BusinessException) {
    AppLog.info(e.message)
}
```