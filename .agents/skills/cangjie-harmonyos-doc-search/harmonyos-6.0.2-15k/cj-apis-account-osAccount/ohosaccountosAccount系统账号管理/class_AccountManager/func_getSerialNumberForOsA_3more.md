### func getSerialNumberForOsAccountLocalId(Int32)

```cangjie
public func getSerialNumberForOsAccountLocalId(localId: Int32): Int64
```

**功能：** 通过系统账号ID获取与该系统账号关联的SN码。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|localId|Int32|是|系统账号ID。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回与该系统账号关联的SN码。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                                     |
  | :-------- | :-------------------------------------------- |
  | 401 | Parameter error.                    |
  | 12300001 | System service exception.                    |
  | 12300002 | Invalid parameter.                   |
  | 12300003 | Account not found.    |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let localId: Int32 = 100 //获取ID为100的系统账号关联的SN码
let accountManager: AccountManager = getAccountManager()
let serialNumber: Int64 = accountManager.getSerialNumberForOsAccountLocalId(localId)
```

### func isOsAccountConstraintEnabled(String)

```cangjie
public func isOsAccountConstraintEnabled(constraint: String): Bool
```

**功能：** 判断当前系统账号是否使能指定约束。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|constraint|String|是|指定的约束名称。详见[系统账号约束列表](#系统账号约束列表)。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示已使能指定的约束；返回false表示未使能指定的约束。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                                     |
  | :-------- | :-------------------------------------------- |
  | 401 | Parameter error.                    |
  | 12300001 | System service exception.                    |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let accountManager: AccountManager = getAccountManager()
let result = accountManager.isOsAccountConstraintEnabled("constraint.wifi")
```

### func isOsAccountUnlocked()

```cangjie
public func isOsAccountUnlocked(): Bool
```

**功能：** 检查当前系统账号是否已认证解锁。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示当前账号已认证解锁；返回false表示当前账号未认证解锁。|

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
let ret: Bool = accountManager.isOsAccountUnlocked()
```