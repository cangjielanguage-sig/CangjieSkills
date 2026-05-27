## 简介

安全单元（SecureElement，简称SE），电子设备上可能存在一个或多个安全单元，比如有eSE(Embedded SE)和SIM卡。能够充当安全单元的SIM卡，要求具备NFC功能。

## 场景介绍

应用程序可以通过接口访问安全单元，比如往安全单元里面写入数据，实现在电子设备上模拟一张NFC卡片的目的。该卡片数据可能存储在eSE安全单元，或在SIM卡安全单元上。安全单元上一般会预置有访问控制规则，应用程序需要具备对应的权限，也就是通过安全单元的访问控制权限校验之后，才能正常访问安全单元。

## 接口说明

完整的仓颉 API 说明以及实例代码请参见：[安全单元接口](../../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-security_element.md)。
实现安全单元的访问，可能使用到下面的接口。

| 接口名 | 功能描述 |
| ----------------------------|---------------------------------------------------------|
| createService(): SEService | 建立一个可用于连接到系统中所有可用SE的新连接。 |
| getReaders(): Array\<Reader> | 返回可用SE Reader的数组，包含该设备上支持的所有的安全单元。 |
| openSession(): Session | 在SE Reader实例上创建连接会话，返回Session实例。 |
| openLogicalChannel(): Channel | 打开逻辑通道，返回逻辑Channel实例对象。 |
| transmit(): Array\<Int32> | 向SE发送APDU数据。 |
| close(): Unit | 关闭Channel。 |