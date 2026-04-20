# ohos.contact（联系人）

本模块提供联系人管理能力，包括添加联系人、删除联系人、更新联系人等。

## 导入模块

```cangjie
import kit.ContactsKit.*
```

## 权限列表

ohos.permission.READ_CONTACTS

ohos.permission.WRITE_CONTACTS

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func addContact(Context, Contact)

```cangjie
public func addContact(context: Context, contact: Contact): Int64
```

**功能：** 添加联系人，成功返回联系人id，失败抛出异常。

**需要权限：** ohos.permission.WRITE_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](../AbilityKit/cj-apis-ability.md#class-context)|是|-|应用上下文Context，Stage模型的应用Context定义见Context。|
|contact|[Contact](#struct-contact)|是|-|联系人信息，若参数中存在id时，会忽略该项而返回新的id。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|添加的联系人id。|

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

let contact = Contact(
    name: Name(fullName: "MyFullName"),
    nickName: NickName("myNickName")
)
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let contactId = addContact(abilityContext, contact)
println(contactId)
```

## func deleteContact(Context, String)

```cangjie
public func deleteContact(context: Context, key: String): Unit
```

**功能：** 删除联系人。当不存在要删除的联系人时会抛出401异常。

**需要权限：** ohos.permission.WRITE_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](../AbilityKit/cj-apis-ability.md#class-context)|是|-|应用上下文Context，Stage模型的应用Context定义见Context。|
|key|String|是|-|联系人的唯一查询键key值，一个联系人对应一个key。|

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

let contactId =  1
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let key = queryKey(abilityContext, contactId)
deleteContact(abilityContext, key)
```