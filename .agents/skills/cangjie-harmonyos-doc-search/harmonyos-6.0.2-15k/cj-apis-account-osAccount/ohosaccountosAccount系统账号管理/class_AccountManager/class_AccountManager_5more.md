## class AccountManager

```cangjie
public class AccountManager {}
```

**功能：** 系统账号管理类。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

### func checkMultiOsAccountEnabled()

```cangjie
public func checkMultiOsAccountEnabled(): Bool
```

**功能：** 判断是否支持多系统账号。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示支持多系统账号；返回false表示不支持。|

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
let ret: Bool = accountManager.checkMultiOsAccountEnabled()
```

### func checkOsAccountTestable()

```cangjie
public func checkOsAccountTestable(): Bool
```

**功能：** 检查当前系统账号是否为测试账号。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示当前账号为测试账号；返回false表示当前账号非测试账号。|

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
let ret: Bool = accountManager.checkOsAccountTestable()
```

### func getActivatedOsAccountLocalIds()

```cangjie
public func getActivatedOsAccountLocalIds(): Array<Int32>
```

**功能：** 查询当前处于激活状态的系统账号的ID列表。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int32>|如果查询成功，返回为当前处于激活状态的系统账号的ID列表。|

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
let localIds: Array<Int32> = accountManager.getActivatedOsAccountLocalIds()
```

### func getOsAccountCount()

```cangjie
public func getOsAccountCount(): UInt32
```

**功能：** 获取已创建的系统账号数量。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS，以上权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回已创建的系统账号的数量。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                                     |
  | :-------- | :-------------------------------------------- |
  | 201 |Permission denied.                  |
  | 12300001 | System service exception.                    |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let accountManager: AccountManager = getAccountManager()
let count: UInt32 = accountManager.getOsAccountCount()
```