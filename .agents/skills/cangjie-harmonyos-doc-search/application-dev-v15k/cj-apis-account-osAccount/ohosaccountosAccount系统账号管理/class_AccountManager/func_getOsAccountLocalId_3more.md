### func getOsAccountLocalId()

```cangjie
public func getOsAccountLocalId(): Int32
```

**功能：** 获取当前进程所属的系统账号ID。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回当前进程所属的系统账号ID。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)。

  | 错误码ID | 错误信息                                     |
  | :-------- | :-------------------------------------------- |
  | 12300001 | System service exception.                    |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let accountManager: AccountManager = getAccountManager()
let localId: Int32 = accountManager.getOsAccountLocalId()
```

### func getOsAccountLocalIdForDomain(DomainAccountInfo)

```cangjie
public func getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo): Int32
```

**功能：** 根据域账号信息，获取与其关联的系统账号ID。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|domainInfo|[DomainAccountInfo](#class-domainaccountinfo)|是|域账号信息。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回域账号关联的系统账号ID。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                                     |
  | :-------- | :-------------------------------------------- |
  | 201 |Permission denied.                  |
  | 401      | Parameter error.                             |
  | 12300001 | System service exception.                    |
  | 12300002 | Invalid parameter.                   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let accountManager: AccountManager = getAccountManager()
let localId: Int32 = accountManager.getOsAccountLocalIdForDomain(DomainAccountInfo("testDomain", "testAccountName"))
```

### func getOsAccountLocalIdForSerialNumber(Int64)

```cangjie
public func getOsAccountLocalIdForSerialNumber(serialNumber: Int64): Int32
```

**功能：** 通过SN码查询与其关联的系统账号的账号ID。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|serialNumber|Int64|是|账号SN码。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回与SN码关联的系统账号的账号ID。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                                     |
  | :-------- | :-------------------------------------------- |
  | 401 | Parameter error.                    |
  | 12300001 | System service exception.                    |
  | 12300002 | Invalid parameter.                   |
  | 12300003 | The account indicated by serialNumber dose not exist.      |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let serialNumber: Int32 = 12345 //查询与SN码12345关联的系统账号的ID
let accountManager: AccountManager = getAccountManager()
let localId: Int32 = accountManager.getOsAccountLocalIdForSerialNumber(serialNumber)
```