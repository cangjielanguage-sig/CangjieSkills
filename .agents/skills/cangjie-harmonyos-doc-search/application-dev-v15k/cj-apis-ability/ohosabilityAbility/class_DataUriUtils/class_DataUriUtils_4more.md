## class DataUriUtils

```cangjie
public class DataUriUtils {}
```

**功能：** 提供uri处理方法的类。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### static func attachId(String, Int64)

```cangjie
public static func attachId(uri: String, id: Int64): String
```

**功能：** 将ID附加到uri的路径末尾。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|表示uri对象。|
|id|Int64|是|-|表示要附加的ID。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回附加ID之后的uri对象。|

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

let id: Int64 = 1122
try {
    let retUri = DataUriUtils.attachId("com.example.dataUriUtils", id)
} catch(e: BusinessException) {
    AppLog.info(e.message)
}
```

### static func deleteId(String)

```cangjie
public static func deleteId(uri: String): String
```

**功能：** 删除指定uri路径末尾的ID。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|表示要从中删除ID的uri对象。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回删除ID之后的uri对象。|

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

try {
    let retUri = DataUriUtils.deleteId("com.example.dataUriUtils/123")
} catch(e: BusinessException) {
    AppLog.info(e.message)
}
```

### static func getId(String)

```cangjie
public static func getId(uri: String): Int64
```

**功能：** 获取指定uri路径末尾的ID。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|表示uri对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回uri路径末尾的ID。|

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

try {
    let retId = DataUriUtils.getId("com.example.dataUriUtils/123")
} catch(e: BusinessException) {
    AppLog.info(e.message)
}
```