## func isLocalContact(Context, Int64)

```cangjie
public func isLocalContact(context: Context, id: Int64): Bool
```

**功能：** 判断当前联系人id是否在电话簿中。

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](../AbilityKit/cj-apis-ability.md#class-context)|是|-|应用上下文Context。|
|id|Int64|是|-|联系人对象的id属性，一个联系人对应一个id。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|成功返回布尔值，true代表联系人id在本地电话簿中，false则代表联系人id不在本地电话簿中；失败抛出异常。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ContactsKit.*

let contactId = 1
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let isLocal = isLocalContact(abilityContext, contactId)
```

## func isMyCard(Context, Int64)

```cangjie
public func isMyCard(context: Context, id: Int64): Bool
```

**功能：** 判断是否为“我的名片”。

**需要权限：** ohos.permission.WRITE_CONTACTS和ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](../AbilityKit/cj-apis-ability.md#class-context)|是|-|应用上下文Context。|
|id|Int64|是|-|名片对象的id属性。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|成功返回是否为“我的名片”的布尔值。true代表的是“我的名片”，false则代表不是；失败抛出异常。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ContactsKit.*

let contactId = 1
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let isMyCard = isMyCard(abilityContext, contactId)
println(isMyCard)
```