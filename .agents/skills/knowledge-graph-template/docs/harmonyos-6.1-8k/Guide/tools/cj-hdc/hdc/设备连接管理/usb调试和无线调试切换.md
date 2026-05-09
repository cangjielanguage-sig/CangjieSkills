### usb调试和无线调试切换

用于连接模式切换的命令如下表所示：

当前推荐通过设备端的usb调试开关和无线调试开关来控制连接通道的开启和关闭。

| 命令 | 说明 |
| -------- | -------- |
| tmode usb | 该命令已经废弃，不会实际操作设备连接通道，需要在设备设置界面通过USB调试开关进行设置。 |
| tmode port [port-number] | 打开设备网络连接通道：设备端daemon进程会重启，已建立的USB连接会中断，需要重新连接。 |
| tmode port close | 关闭设备网络连接通道：设备端daemon进程会重启，已建立的USB连接会中断，需要重新连接。 |
| tconn [IP]:[port] [-remove] | 连接指定的设备，通过“IP地址：端口号”来指定连接的设备，使用-remove参数断开连接。 |

1. 打开设备网络连接通道，命令格式如下：

   ```shell
   hdc tmode port [port-number]
   ```

   **参数：**

   | 参数 | 参数说明 |
   | -------- | -------- |
   | port-number | 监听连接的网络端口号，范围:1~65535。 |

   **返回值：**

   | 返回值 | 说明 |
   | -------- | -------- |
   | Set device run mode successful. | 打开成功。 |
   | [Fail]ExecuteCommand need connect-key | 打开失败，设备列表无设备，无法打开设备无线调试通道。 |
   | [Fail]Incorrect port range | 端口号超出可设置范围（1~65535）。 |

   **使用方法：**

   ```shell
   hdc tmode port 1234
   ```

   > **注意：**
   >
   > 切换前，请确保条件满足：远端设备与近端PC处于同一网络，且PC可ping通远端设备IP。如不满足以上条件请勿使用该命令进行切换。
   > 执行完毕后，远端daemon进程将会退出并重启，USB连接将会断开，需要重新连接。

2. 关闭设备网络连接通道，命令格式如下：

   ```shell
   hdc tmode port close
   ```

   **返回值：**

   | 返回值 | 说明 |
   | -------- | -------- |
   | [Fail]ExecuteCommand need connect-key | 设备列表无设备，无法执行命令。 |

   **使用方法：**

   ```shell
   hdc tmode port close
   ```

   > **说明：**
   >
   > 执行完毕后，远端daemon进程将会退出并重启，USB连接将会断开，需要重新连接。

3. 通过TCP连接指定的设备，命令格式如下：

   ```shell
   hdc tconn [IP]:[port] [-remove]
   ```

   **参数：**

   | 参数 | 参数说明 |
   | -------- | -------- |
   | [IP]:[port]  | 设备的IP地址与端口号。 |
   | -remove | 可选参数，断开指定设备的连接。 |

   **返回值：**

   | 返回值 | 说明 |
   | -------- | -------- |
   | Connect OK | 连接成功 |
   | [Info]Target is connected, repeat opration | 设备当前已连接 |
   | [Fail]Connect failed | 连接失败 |

   **使用方法：**

   ```shell
   hdc tconn 192.168.0.1:8888
   hdc tconn 192.168.0.1:8888 -remove  // 断开指定网络设备连接
   ```