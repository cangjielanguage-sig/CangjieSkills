### WebSocket

本实现为 WebSocket 提供 sub-protocol 协商，包括基础的 frame 解码、读取、消息发送、frame 编码、ping、pong、关闭等功能。

用户通过 WebSocket.upgradeFromClient 从一个 HTTP/1.1 或 HTTP/2 Client 实例升级到 WebSocket 协议，之后通过返回的 WebSocket 实例进行 WebSocket 通讯。

用户在一个 server 端的 handler 中，通过 WebSocket.upgradeFromServer 从 HTTP/1.1 或 HTTP/2 协议升级到 WebSocket 协议，之后通过返回的 WebSocket 实例进行 WebSocket 通讯。

按照协议，HTTP/1.1 中，升级后的 WebSocket 连接是建立在 tcp/tls 连接之上；HTTP/2 中，升级后的 WebSocket 连接是建立在 HTTP/2 connection 的一个 stream 之上。HTTP/1.1 中，close 最终会直接关闭 tcp/tls 连接；HTTP/2 中，close 只会关闭 connection 上的一个 stream。