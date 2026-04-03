# 蓝牙服务开发概述

## 概述

蓝牙技术是一种无线通信技术，可以在短距离内传输数据。它是由爱立信公司于1994年提出的，使用2.4 GHz的ISM频段，可以在10米左右的距离内进行通信。可以用于连接手机、耳机、音箱、键盘、鼠标、打印机等各种设备。特点是低功耗、低成本、简单易用。目前已经发展到了第五代，支持更高的数据传输速率和更广的覆盖范围。

## 实现原理

蓝牙的实现原理是基于无线电技术的短距离通信协议，使用2.4GHz频段的无线电波进行通信，使用频率跳跃技术（Frequency Hopping Spread Spectrum，FHSS）来避免与其他无线设备的干扰。在通信过程中，蓝牙设备会发送和接收数据包，并且使用不同的蓝牙协议来控制通信流程和数据传输。

## 模块介绍

- a2dp模块（高级音频分发配置文件）：A2DP是Advanced Audio Distribution Profile的缩写，即高级音频分发配置文件。它是一种蓝牙协议，允许无线传输高品质音频流，例如音乐或语音通话，同时支持双向通信，因此可以用于耳机、扬声器、汽车音响等设备。详情请参见[@ohos.bluetooth.a2dp API参考](../../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-bluetooth-a2dp.md)。
- ble模块（低功耗蓝牙）：BLE是Bluetooth Low Energy的缩写，意为“低功耗蓝牙”。它是一种能够在低功耗情况下进行通信的蓝牙技术，与传统蓝牙相比，BLE的功耗更低，适用于需要长时间运行的低功耗设备，如智能手表、健康监测设备、智能家居等。详情请参见[@ohos.bluetooth.ble API参考](../../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-bluetooth-ble.md)。
- gatt模块（通用属性）：GATT是指蓝牙技术中的通用属性（Generic Attribute），它是一种用于在蓝牙低功耗设备之间传输数据的协议。GATT协议定义了一套通用的属性和服务框架，用于描述蓝牙设备之间的通信，同时蓝牙设备可以向其他设备提供服务，也可以从其他设备获取服务。详情请参见[@ohos.bluetooth.ble API参考](../../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-bluetooth-ble.md)。
