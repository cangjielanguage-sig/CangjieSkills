### func getOsAccountLocalIdForUid(Int32)

```cangjie
public func getOsAccountLocalIdForUid(uid: Int32): Int32
```

**功能：** 根据uid查询对应的系统账号ID。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|uid|Int32|是|进程uid。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回对应的系统账号ID。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                                     |
  | :-------- | :-------------------------------------------- |
  | 401 | Parameter error.                    |
  | 12300001 | System service exception.                    |
  | 12300002 | Invalid parameter.                   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let uid: Int32 = 12345678 //查询值为12345678的uid所属的系统账号ID
let accountManager: AccountManager = getAccountManager()
let localId: Int32 = accountManager.getOsAccountLocalIdForUid(uid)
```

### func getOsAccountName()

```cangjie
public func getOsAccountName(): String
```

**功能：** 查询调用方所属系统账号的名称。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回调用方所属系统账号的名称。|

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
let name: String = accountManager.getOsAccountName()
```

### func getOsAccountType()

```cangjie
public func getOsAccountType(): OsAccountType
```

**功能：** 查询当前进程所属的系统账号的账号类型。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[OsAccountType](#enum-osaccounttype)|返回当前进程所属的系统账号的账号类型。|

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
let type_: OsAccountType = accountManager.getOsAccountType()
```