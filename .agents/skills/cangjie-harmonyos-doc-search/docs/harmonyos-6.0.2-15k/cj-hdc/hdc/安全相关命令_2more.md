## 安全相关命令

| 命令 | 说明 |
| -------- | -------- |
| keygen FILE | 生成一个新的秘钥对，并将私钥和公钥分别保存到FILE和FILE.pub，其中文件名FILE可自定义。 |

1. 生成一个新的秘钥对，命令格式如下：

   ```shell
   hdc keygen FILE
   ```

   **参数：**

   | 参数 | 说明 |
   | -------- | -------- |
   | FILE | FILE为自定义的文件名 |

   **使用方法：**

   ```shell
   hdc keygen key # 在当前目录下生成key和key.pub文件
   ```

## 查询版本号

| 命令 | 说明 |
| -------- | -------- |
| -v/version | 打印hdc版本信息。 |
| checkserver | 获取客户端与服务进程版本。 |

1. 显示hdc的版本信息，命令格式如下：

   ```shell
   hdc -v/version
   ```

   **返回值：**

   | 返回值 | 说明 |
   | -------- | -------- |
   | Ver:X.X.Xa | hdc（SDK）的版本信息。 |

   **使用方法：**

   ```shell
   hdc -v 或 hdc version
   ```

2. 获取客户端与服务进程版本，命令格式如下：

   ```shell
   hdc checkserver
   ```

   **返回值：**

   | 返回值 | 说明 |
   | -------- | -------- |
   | Client version: Ver:X.X.Xa, Server version: Ver:X.X.Xa | client（客户端），server（服务进程）版本号。 |

   **使用方法：**

   ```shell
   hdc checkserver
   ```