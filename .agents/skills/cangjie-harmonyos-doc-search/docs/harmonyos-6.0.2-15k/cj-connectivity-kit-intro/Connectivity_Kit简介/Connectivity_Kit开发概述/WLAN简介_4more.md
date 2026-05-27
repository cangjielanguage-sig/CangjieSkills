### WLAN简介

无线局域网（Wireless Local Area Networks，WLAN），是通过无线电、红外光信号或者其他技术发送和接收数据的局域网，用户可以通过WLAN实现结点之间无物理连接的网络通讯。常用于用户携带可移动终端的办公、公众环境中。

WLAN系统为用户提供接入WLAN网络功能（STA模式）、点对点的数据传输功能（P2P模式）和热点分享功能（AP模式），让应用可以通过WLAN和其他设备互联互通。

- **STA模式**
  STA模式即工作站模式，可以理解为某网络中的一个工作站即客户端。当某设备具备该功能时，它可以连到另外的一个路由网络中，如家用路由器，通常用于提供网络的数据上行服务。

  详情请参见[ohos.wifiManager API参考](../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-wifi_manager.md)。

- **P2P模式**
  P2P模式即为Wi-Fi Direct；Wi-Fi Direct 是一种点对点连接技术，它可以在两台 STA 之间直接建立 TCP/IP 链接，并不需要AP的参与；其中一台STA会起到传统意义上的AP的作用，称为Group Owner(GO)，另外一台station则称为Group Client(GC)，像连接AP一样连接到GO。

  详情请参见[ohos.wifiManager API参考](../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-wifi_manager.md)。

- **AP模式**
  AP模式为加入无线局域网的成员设备（即客户端）提供下行数据业务，它提供以无线方式组建无线局域网WLAN，相当于WLAN的中心设备。

  详情请参见[ohos.wifiManager API参考](../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-wifi_manager.md)。

### NFC简介

NFC英文全称Near Field Communication，近距离无线通信。NFC服务提供NFC开关控制、NFC标签读写、NFC卡模拟等业务功能。

- **NFC卡模拟**

  NFC卡模拟模块，提供了NFC的刷卡业务，电子设备和读卡器触碰完成刷卡。应用程序需要按照规定的格式来声明NFC卡模拟能力，只有声明后应用程序才能够具备刷卡能力。

  详情请参见[ohos.nfc.cardEmulation API参考](../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-nfc-cardEmulation.md)。

### 运作机制

Connectivity能力作为系统为应用提供的一种基础通信服务，需要在应用使用场景中打开相应开关/连接等处理，在业务结束时主动结束连接等。

### 约束与限制

使用设备的相关能力，需要用户主动授权打开开关。否则系统不会向三方应用提供服务。