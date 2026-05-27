### 查询设备列表

通过命令list targets，查询已连接的所有目标设备。

添加-v参数，则会打印设备详细信息。

命令格式如下：

```shell
hdc list targets [-v]
```

**返回值：**

| 返回值 | 说明 |
| -------- | -------- |
| 设备标识符列表 | 已连接的设备标识符列表，-t参数使用的connect-key即为此信息。 |
| [Empty] | 没有查询到设备信息。 |

**使用方法：**

```shell
hdc list targets
hdc list targets -v
```

### 连接指定的目标设备

连接单台设备时，执行命令无需指定设备标识符；
连接了多台设备时，每次执行命令时需要使用-t参数指定目标设备的标识符，命令格式如下：

```shell
hdc -t [connect-key] [command]
```

**参数：**

| 参数名 | 说明 |
| -------- | -------- |
| connect-key| 设备标识符，即为hdc list targets返回的信息。 |
| command | hdc支持的命令。 |

> **说明：**
>
> connect-key为每个设备唯一的标识符。如果通过usb连接，标识符为序列号；如果通过网络连接设备，标识符为“IP地址:端口号”。

**返回值：**

| 返回值 | 说明 |
| -------- | -------- |
| 命令执行返回内容 | 请参见对应命令的返回值。 |
| [Fail]Not match target founded, check connect-key please | 没有找到与connect-key匹配的设备。 |
| [Fail]Device not founded or connected | 设备未找到或尚未连接。 |
| [Fail]ExecuteCommand need connect-key? please confirm a device by help info | 多设备连接时需要指定一个设备。 |
| Unknown operation command... | 不支持的命令。 |

> **说明：**
>
> 返回的错误提示信息后续会调整优化，请勿用于自动化脚本或程序的结果判断。

**使用方法：**

该方法需要与具体的操作命令搭配使用，下面以shell命令举例：

```shell
hdc list targets  # 查询已连接的所有目标设备的connect-key
hdc -t [connect-key] shell # -t 后面添加的connect-key需要替换为指定的设备标识符
```

### 等待设备正常连接

命令格式如下：

```shell
hdc wait # 等待设备正常连接
hdc -t connect-key wait # 等待指定的设备正常连接，connect-key需要替换为指定的设备标识符
```

**返回值：**

| 返回值 | 说明 |
| -------- | -------- |
| 无 | hdc wait命令执行后，识别到正常连接的设备后结束。 |

**使用方法：**

```shell
hdc wait
hdc -t connect-key wait
```