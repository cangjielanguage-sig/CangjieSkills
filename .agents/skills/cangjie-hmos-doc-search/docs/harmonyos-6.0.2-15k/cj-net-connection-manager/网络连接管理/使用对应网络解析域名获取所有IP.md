## 使用对应网络解析域名，获取所有IP

1. 声明接口调用所需要的权限：ohos.permission.INTERNET。此权限级别为normal，在申请权限前，请确保符合[权限使用的基本原则](../../cj-app-permission-mgmt-overview/.overview.md)。然后参考[访问控制-声明权限](../../cj-declare-permissions/.overview.md)声明对应权限。

2. 从kit.NetworkKit中导入connection。

3. 调用[getAddressesByName](../../cj-apis-net-connection/.overview.md)方法，使用默认网络解析主机名以获取所有IP地址。

```cangjie
// 引入包名。
import kit.NetworkKit.*
import ohos.base.*

// 使用默认网络解析主机名以获取所有IP地址。
let addrs: Array<NetAddress> = getAddressesByName("xxxx)
AppLog.info("Succeeded to get data")
```