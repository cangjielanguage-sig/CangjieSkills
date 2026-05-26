## 监控默认网络变化并主动重建网络连接

根据当前网络状态及网络质量情况，默认网络可能会发生变化，如下所示。

1. 在WiFi弱信号的情况下，默认网络可能会切换到蜂窝网络。
2. 在蜂窝网络状态差的情况下，默认网络可能会切换到WiFi。
3. 关闭WiFi后，默认网络可能会切换到蜂窝网络。
4. 关闭蜂窝网络后，默认网络可能会切换到WiFi。
5. 在WiFi弱信号的情况下，默认网络可能会切换到其他WiFi(存在跨网情况)。
6. 在蜂窝网络状态差的情况下，默认网络可能会切换到其他蜂窝(存在跨网情况)。

本节旨在介绍监控默认网络的变化后，应用报文能够快速迁移到新默认网络上，具体做法如下。

### 监控默认网络变化

```cangjie
import kit.NetworkKit.*
import ohos.base.*

func test() {
    let netConnection = createNetConnection()
    netConnection.onNetAvailable {
        netHandle => AppLog.info("net is available, netId is ${netHandle.netId}")
    }
}
```

## 获取所有注册的网络

1. 声明接口调用所需要的权限：ohos.permission.GET_NETWORK_INFO。此权限级别为normal，在申请权限前，请确保符合[权限使用的基本原则](../security/AccessToken/cj-app-permission-mgmt-overview.md#权限使用的基本原则)。然后参考[访问控制-声明权限](../security/AccessToken/cj-declare-permissions.md)声明对应权限。

2. 从kit.NetworkKit中导入connection。

3. 调用[getAllNets](../../API_Reference/source_zh_cn/apis/NetworkKit/cj-apis-net-connection.md#func-getallnets)方法，获取所有处于连接状态的网络列表。

```cangjie
// 引入包名。
import kit.NetworkKit.*
import ohos.base.*

// 获取所有处于连接状态的网络列表。
let nets = getAllNets()
```