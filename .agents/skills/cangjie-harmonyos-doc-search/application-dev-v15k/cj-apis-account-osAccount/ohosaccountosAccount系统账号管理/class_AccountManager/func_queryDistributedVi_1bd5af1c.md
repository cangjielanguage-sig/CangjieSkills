### func queryDistributedVirtualDeviceId()

```cangjie
public func queryDistributedVirtualDeviceId(): String
```

**功能：** 获取分布式虚拟设备ID。

**需要权限：** ohos.permission.MANAGE_LOCAL_ACCOUNTS（仅系统应用可申请）或ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回分布式虚拟设备ID。|

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
let deviceId: String = accountManager.queryDistributedVirtualDeviceId()
```