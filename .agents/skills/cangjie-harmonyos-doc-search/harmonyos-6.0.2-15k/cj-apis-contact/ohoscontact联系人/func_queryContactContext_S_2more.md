## func queryContact(Context, String, Holder, ContactAttributes)

```cangjie
public func queryContact(context: Context, key: String,
                         holder!: Holder = Holder.EMPTY,
                         attrs!: ContactAttributes = ContactAttributes.ALL
                        ): Contact
```

**功能：** 根据key，holder和attrs查询联系人。当不存在该联系人时，抛出401异常。

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](../AbilityKit/cj-apis-ability.md#class-context)|是|-|应用上下文Context。|
|key|String|是|-|联系人的key值，一个联系人对应一个key。|
|holder|[Holder](#struct-holder)|否|Holder.EMPTY| **命名参数。** 创建联系人的应用信息。|
|attrs|[ContactAttributes](#struct-contactattributes)|否|ContactAttributes.ALL| **命名参数。** 联系人的属性列表。|

**返回值：**

|类型|说明|
|:----|:----|
|[Contact](#struct-contact)|成功返回查询的联系人对象；失败抛出异常。|

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
let key = queryKey(abilityContext, contactId)
let attrs = ContactAttributes([Attribute.ATTR_NAME, ATTR_NICKNAME])
let holder = Holder("displayName", 1, bundleName: "com.ohos.contacts")
let contact = queryContact(abilityContext, key, holder: holder, attrs: attrs)
println(contact.id)
```

## func queryContacts(Context, Holder, ContactAttributes)

```cangjie
public func queryContacts(context: Context,
                          holder!: Holder = Holder.EMPTY,
                          attrs!: ContactAttributes = ContactAttributes.ALL
                         ): Array<Contact>
```

**功能：** 根据holder和attrs查询所有联系人。

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](../AbilityKit/cj-apis-ability.md#class-context)|是|-|应用上下文Context。|
|holder|[Holder](#struct-holder)|否|Holder.EMPTY| **命名参数。** 创建联系人的应用信息。|
|attrs|[ContactAttributes](#struct-contactattributes)|否|ContactAttributes.ALL| **命名参数。** 创建联系人的应用信息。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Contact](#struct-contact)>|成功返回查询的联系人对象数组；失败抛出异常。|

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
let holder = Holder("displayName", 1, bundleName: "com.ohos.contacts")
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let contacts = queryContacts(abilityContext, holder: holder, attrs: attrs)
```