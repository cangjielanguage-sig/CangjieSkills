# ohos.net.connection（网络连接管理）

网络连接管理提供管理网络一些基础能力，包括获取默认激活的数据网络、获取所有激活数据网络列表、开启关闭飞行模式、获取网络能力信息等功能。

本节错误码的详细介绍请参见[网络连接管理错误码](../../errorcodes/cj-errorcode-net-connection.md)。

## 导入模块

```cangjie
import kit.NetworkKit.*
```

## 权限列表

ohos.permission.GET_NETWORK_INFO

ohos.permission.INTERNET

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func createNetConnection(?NetSpecifier, UInt32)

```cangjie
public func createNetConnection(netSpecifier!: ?NetSpecifier = None, timeout!: UInt32 = 0): NetConnection
```

**功能：** 创建一个NetConnection对象，netSpecifier指定关注的网络的各项特征；timeout是超时时间(单位是毫秒)；netSpecifier是timeout的必要条件，两者都没有则表示关注默认网络。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|netSpecifier|?[NetSpecifier](#class-netspecifier)|否|None| **命名参数。** 指定网络的各项特征，为None时关注默认网络。|
|timeout|UInt32|否|0| **命名参数。** 获取netSpecifier指定的网络时的超时时间，仅netSpecifier存在时生效，默认值为0。|

**返回值：**

|类型|说明|
|:----|:----|
|[NetConnection](#class-netconnection)|所关注的网络的句柄。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

// 关注默认网络, 不需要传参
let netConnection = createNetConnection()

// 关注蜂窝网络，需要传入相关网络特征，timeout参数未传入说明未使用超时时间，此时timeout为0
let netspecifier = NetSpecifier(NetCapabilities([NetBearType.BEARER_CELLULAR]))
let netConnectionCellular = createNetConnection(netSpecifier: netspecifier)
```

## func getAddressesByName(String)

```cangjie
public func getAddressesByName(host: String): Array<NetAddress>
```

**功能：** 使用对应网络解析主机名以获取所有IP地址。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|host|String|是|-|需要解析的主机名。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[NetAddress](#class-netaddress)>|返回所有IP地址。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[网络连接管理错误码](../../errorcodes/cj-errorcode-net-connection.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error.|
  |2100001|Invalid parameter value.|
  |2100002|Operation failed. Cannot connect to service.|
  |2100003|System internal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let addresses = getAddressesByName("localhost")
```