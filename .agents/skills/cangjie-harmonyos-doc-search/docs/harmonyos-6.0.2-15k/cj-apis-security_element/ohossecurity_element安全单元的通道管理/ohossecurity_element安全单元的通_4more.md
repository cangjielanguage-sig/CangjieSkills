# ohos.security_element（安全单元的通道管理）

本模块主要用于操作及管理安全单元（SecureElement，简称SE），电子设备上可能存在的安全单元有eSE(Embedded SE)和SIM卡。文档中出现的SE服务为SEService实例，参见[SEServer](#class-seservice)。

## 导入模块

```cangjie
import kit.ConnectivityKit.*
```

## 使用说明

对于文档中出现以下类型说明：

| 类型    | 说明                                   |
| :------ | :-------------------------------------|
| [Reader](#class-reader)  | 此类的实例表示该设备支持的SE，如果支持eSE和SIM，则返回两个实例。 |
| [Session](#class-session) | 此类的实例表示在某个SE Reader实例上创建连接会话。        |
| [Channel](#class-channel) | 此类的实例表示在某个Session实例上创建通道，可能为基础通道或逻辑通道。 |

## func createService()

```cangjie
public func createService(): SEService
```

**功能：** 建立一个可用于连接到系统中所有可用SE的新连接（服务）。

仅当[isConnected](#func-isconnected)方法返回true时，该返回SEService对象是可用的。

**系统能力：** SystemCapability.Communication.SecureElement

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[SEService](#class-seservice)|可用于连接到系统中所有可用SE的新连接（服务）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|