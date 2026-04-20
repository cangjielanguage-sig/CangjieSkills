## func queryGroups(Context, Holder)

```cangjie
public func queryGroups(context: Context, holder!: Holder = Holder.EMPTY): Array<Group>
```

**功能：** 根据holder查询联系人的所有群组。

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](../AbilityKit/cj-apis-ability.md#class-context)|是|-|应用上下文Context。|
|holder|[Holder](#struct-holder)|否|Holder.EMPTY| **命名参数。** 创建联系人的应用信息。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Group](#struct-group)>|返回查询到的群组对象数组。|

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

let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let contacts: Array<Group> = queryGroups(abilityContext)
```

## func queryHolders(Context)

```cangjie
public func queryHolders(context: Context): Array<Holder>
```

**功能：** 查询所有创建联系人的应用信息。

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](../AbilityKit/cj-apis-ability.md#class-context)|是|-|应用上下文Context。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Holder](#struct-holder)>|成功返回查询到的创建联系人应用信息的对象数组；失败抛出异常。|

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

let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let holders: Array<Holder> = queryHolders(abilityContext)
```

## func queryKey(Context, Int64, Holder)

```cangjie
public func queryKey(context: Context, id: Int64, holder!: Holder = Holder.EMPTY): String
```

**功能：** 根据联系人的id和holder查询联系人的key，当id对应的联系人不存在时，抛出401异常。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](../AbilityKit/cj-apis-ability.md#class-context)|是|-|应用上下文Context。|
|id|Int64|是|-|根据联系人的id查询联系人的key。|
|holder|[Holder](#struct-holder)|否|Holder.EMPTY| **命名参数。** 创建联系人的应用信息。|

**返回值：**

|类型|说明|
|:----|:----|
|String|成功返回查询到的联系人对应的key；失败抛出异常。|

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
let key: String = queryKey(abilityContext, contactId)
```