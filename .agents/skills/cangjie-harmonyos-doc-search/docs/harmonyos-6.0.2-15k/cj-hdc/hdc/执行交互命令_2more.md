## 执行交互命令

命令格式如下：

```shell
hdc shell [-b bundlename] [command]
```

**参数：**

| 参数 | 说明 |
| -------- | -------- |
| \[-b _bundlename_] | 指定可调试应用包名，在可调试应用数据目录内，以非交互式模式执行命令。<br>此参数当前仅支持以非交互式模式执行命令，不支持缺省command参数执行命令进入交互式shell会话，未配置此参数默认执行路径为系统根目录。 |
| \[command] | 需要在设备侧执行的单次命令，不同类型或版本的系统支持的command命令有所差异，可以通过hdc shell ls /system/bin查阅支持的命令列表。当前许多命令都是由[toybox](./cj-toybox.md)提供，可通过 hdc shell toybox --help 获取命令帮助。<br>缺省该参数，hdc将会启动一个交互式的shell会话，开发者可以在命令提示符下输入命令，比如 ls、cd、pwd 等。 |

**返回值：**

| 返回值 | 说明 |
| -------- | -------- |
| 交互命令返回内容 | 返回内容详情请参见其他交互命令返回内容。 |
| /bin/sh: XXX : inaccessible or not found | 不支持的交互命令。 |
| \[Fail]具体失败信息 | 执行失败，参见[hdc错误码章节](#hdc错误码)。 |

**使用方法：**

```shell
# 进入交互式模式执行命令
hdc shell

# 以非交互式模式执行命令
hdc shell ps -ef

# 查询全部可用命令
hdc shell help -a

# 在指定包名的应用数据目录内以非交互式模式执行命令，支持touch、rm、ls、stat、cat、mkdir命令。
hdc shell -b com.example.myapplication ls data/storage/el2/base/
```

> **说明：**
>
> 使用参数[-b bundlename]指定包名，应满足条件：指定包名的已安装应用为“使用调试证书签名的应用”，如何申请调试证书及签名可参见：[申请调试证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-debugcert-0000001914263178)。

## 应用管理

| 命令 | 说明 |
| -------- | -------- |
| install src | 安装指定的应用文件。 |
| uninstall packageName | 卸载指定的应用包package包名。 |

1. 安装APP package，命令格式如下：

   ```shell
   hdc install [-r|-s] src
   ```

   **参数：**

   | 参数名 | 说明 |
   | -------- | -------- |
   | src| 应用安装包的文件名 |
   | -r | 替换已存在应用（.hap） |
   | -s | 安装一个共享包（.hsp） |

   **返回值：**

   | 返回值 | 说明 |
   | -------- | -------- |
   | AppMod finish | 成功情况下返回安装信息和AppMod finish。 |
   | 具体安装失败原因 | 失败情况下返回具体安装失败信息。 |

   **使用方法：**

   以安装example.hap包为例：

   ```shell
   hdc install E:\example.hap
   ```

2. 卸载应用，命令格式如下：

   ```shell
   hdc uninstall [-k|-s] packageName
   ```

   **参数：**

   | 参数名 | 说明 |
   | -------- | -------- |
   | packageName | 应用安装包。 |
   | -k | 保留/data和/cache目录。 |
   | -s | 卸载共享包。 |

   **返回值：**

   | 返回值 | 说明 |
   | -------- | -------- |
   | AppMod finish | 成功情况下返回卸载信息和AppMod finish。 |
   | 具体卸载失败原因 | 失败情况下返回具体卸载失败信息。 |

   **使用方法：**

   以卸载com.example.hello包为例：

   ```shell
   hdc uninstall com.example.hello
   ```