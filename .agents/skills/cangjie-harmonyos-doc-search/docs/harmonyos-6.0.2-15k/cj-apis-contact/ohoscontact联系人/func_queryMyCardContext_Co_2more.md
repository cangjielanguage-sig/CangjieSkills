## func queryMyCard(Context, ContactAttributes)

```cangjie
public func queryMyCard(context: Context, attrs!: ContactAttributes = ContactAttributes.ALL): Contact
```

**功能：** 查询“我的名片”，当不存在我的名片时，抛出401异常。

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](../AbilityKit/cj-apis-ability.md#class-context)|是|-|应用上下文Context。|
|attrs|[ContactAttributes](#struct-contactattributes)|否|ContactAttributes.ALL| **命名参数。** 联系人的属性列表。|

**返回值：**

|类型|说明|
|:----|:----|
|[Contact](#struct-contact)|成功返回“我的名片”信息；失败抛出异常。|

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

let attrs = ContactAttributes([Attribute.ATTR_NAME, ATTR_NICKNAME])
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let contact = queryMyCard(abilityContext, attrs: attrs)
println(contact.id)
```

## func selectContacts(Context, AsyncCallback\<Array\<Contact>>, ContactSelectOptions)

```cangjie
public func selectContacts(context: Context,
                           callback: AsyncCallback<Array<Contact>>,
                           options!: ContactSelectOptions = ContactSelectOptions()): Unit
```

**功能：** 调用选择联系人接口，打开选择联系人UI界面，选定的联系人使用callback方式作为异步方法。

**系统能力：** SystemCapability.Applications.Contacts

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](../AbilityKit/cj-apis-ability.md#class-context)|是|-|应用上下文Context。|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<Array\<[Contact](#struct-contact)>>|是|-|回调函数，返回选择的联系人对象数组。|
|options|[ContactSelectOptions](#class-contactselectoptions)|否|ContactSelectOptions()| **命名参数。** 选择联系人时的筛选条件。|

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

let callback = {
    errorCode: Option<AsyncError>, data: Option<Array<Contact>> => match (errorCode) {
        case Some(e) => AppLog.error("        testSelect error: ${e.code}")
        case _ => match (data) {
            case Some(contacts) => AppLog.info(
                "        selectContacts: ${contacts.size} contacts selected!")
            case _ => AppLog.error("        testSelect None contacts returned, error: 0")
        }
    }
}
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
selectContacts(abilityContext, callback, options: ContactSelectOptions(isMultiSelect: false))
```