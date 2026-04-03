## M

### MAP

Message Access Profile，即消息访问协议。可用于实现蓝牙设备间的消息同步，支持短信、邮件等数据传输。该协议定义了2种角色：[MCE](#mce)和[MSE](#mse)。

### MCE

Message Client Equipment，即[MAP](#map)协议中的消息客户端，可查看和管理[MSE](#mse)的消息。典型设备如：车载蓝牙。

### MSE

Message Server Equipment，即[MAP](#map)协议中的消息服务端，存储原始消息数据（如短信或邮件）。典型设备如‌：手机。

### MTU

Maximum Transmission Unit，即最大传输单元。表示网络中单次传输的最大数据包大小，单位是字节。

## N

### NAP

Network Access Point，即[PAN](#pan)协议中的网络接入点，充当网关设备，提供互联网接入或本地网络共享功能。典型设备如：手机、平板等。

## O

### OPP

Object Push Profile，即对象推送协议。基于通用对象交换协议（Generic Object Exchange Profile，GOEP）构建，可用于实现设备间数据（如图片、文档等）传输。

## P

### PAN

Personal Area Network，即蓝牙个人局域网协议。支持设备间网络共享。在该协议中，[NAP](#nap)和[PANU](#panu)是两种核心角色。

### PANU

Personal Area Network User，即[PAN](#pan)协议中的个人局域网用户，作为客户端设备，主动连接[NAP](#nap)以获取网络服务。

### PBAP

Phone Book Access Profile，即蓝牙电话簿访问协议。可用于实现蓝牙设备间的电话簿数据同步，支持联系人、通话记录等数据传输。该协议定义了2种角色：[PCE](#pce)和[PSE](#pse)。

### PCE

Phone Book Client Equipment，即[PBAP](#pbap)协议中的电话簿客户端，作为数据请求方，可获取[PSE](#pse)的电话簿数据。典型设备如：车载蓝牙。

### PSE

Phone Book Server Equipment，即[PBAP](#pbap)协议中的电话簿服务端，存储原始电话簿数据（如联系人和通话记录）。典型设备如：手机。

### Profile

在蓝牙子系统中，一般特指某种蓝牙技术协议或者能力。例如：[A2DP](#a2dp)、[HFP](#hfp)和[HID](#hid)协议等。

### PSM

Protocol/Service Multiplexer，即协议/服务多路复用器。用于标识[L2CAP](#l2cap)层上的不同服务或协议。

## R

### RFCOMM

Radio Frequency Communication，即无线电频率通信协议。用于模拟传统的RS232串行通信（一种常见的有线数据传输标准），提供一种简单可靠的数据传输方式，支持多个同时连接的通道。

### RSSI

Received Signal Strength Indicator，是无线通信中用于量化接收端信号强度的指标，单位是dBm。

## S

### Service

在蓝牙协议中，一般特指[GATT](#gatt)协议中的服务。是一种包含多个特征值和所依赖的其他服务的数据结构，表示[BLE](#ble)设备的一种能力，通过[UUID](#uuid)标识。

### SPP

Serial Port Profile，即串口通信协议。可用于实现蓝牙设备间通信连接和传输数据。

## U

### UUID

Universally Unique Identifier，即通用唯一标识，是一个128比特的数据格式。在蓝牙技术中，可用于标识不同的[Profile](#profile)协议，也可用于[GATT](#gatt)协议中的服务、特征值和描述符。