## Connectivity Kit开发概述

移动终端设备已经深入人民日常生活的方方面面，如连接蓝牙耳机听音乐、连接WIFI上网、使用NFC进行一碰开门等已成为终端用户日常生活中常见的行为。

当用户处于这些丰富的使用场景中时，蓝牙提供基于蓝牙连接的基础能力，如音乐/通话/分享等，WIFI提供基础的无线连接能力，NFC提供基础的靠近刷卡和读卡能力。

对于开发者，设计基础通信的体验服务，可以使应用的使用体验更贴近每个终端用户的日常生活。

### 蓝牙简介

蓝牙技术是一种无线通信技术，可以在短距离内传输数据。可以用于连接手机、耳机、音箱、键盘、鼠标、打印机等各种设备。特点是低功耗、低成本、简单易用。目前已经发展到了第五代，支持更高的数据传输速率和更广的覆盖范围。
下面简介几种常见的蓝牙涉及的模块：

- **ACCESS接入模块**

  蓝牙接入模块，提供了开关蓝牙以及获取蓝牙开关状态等接口功能。使用蓝牙功能需要通过该模块打开蓝牙，在蓝牙开关状态正确的条件下使用其他功能。

  详情请参见[ohos.bluetooth.access API参考](../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-bluetooth-access.md)。

- **CONNECTION连接模块**

  蓝牙连接模块，提供了设备发现、配对连接、获取本端及外设信息的接口功能。使用和外设交互的功能，需要使用该模块提供的能力和外设配对、连接成功，才能继续进行后续的数据传输等功能。

  详情请参见[ohos.bluetooth.connection API参考](../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-bluetooth-connection.md)。

- **BLE模块（低功耗蓝牙）**

  BLE是Bluetooth Low Energy的缩写，意为“低功耗蓝牙”。它是一种能够在低功耗情况下进行通信的蓝牙技术，与传统蓝牙相比，BLE的功耗更低，适用于需要长时间运行的低功耗设备，如智能手表、健康监测设备、智能家居等。

  详情请参见[ohos.bluetooth.ble API参考](../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-bluetooth-ble.md)。

- **A2DP模块（高级音频分发配置文件）**

  A2DP是Advanced Audio Distribution Profile的缩写，即高级音频分发配置文件。它是一种蓝牙协议，允许无线传输高品质音频流，例如音乐或语音通话，同时支持双向通信，因此可以用于耳机、扬声器、汽车音响等设备。

  详情请参见[ohos.bluetooth.a2dp API参考](../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-bluetooth-a2dp.md)。

相关开发指南请参见：[蓝牙开发指南](./bluetooth/cj-bluetooth-overview.md)。