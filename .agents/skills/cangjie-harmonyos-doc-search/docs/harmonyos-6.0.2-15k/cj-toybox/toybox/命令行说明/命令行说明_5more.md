## 命令行说明

toybox的执行方式有两种：

- toybox [command] [arguments...]
- 直接执行 [command] [arguments...]

其中 [command] 可被替换为toybox支持的任意命令（可通过输入不带参数的toybox命令查询）。
[arguments...] 为[command]所需要的参数。

### 帮助命令

格式：toybox [--long | --help | --version | [command] [arguments...]]

| 选项 | 参数 | 说明 |
| :- | :- | :- |
| --help | NA | 显示命令帮助。 |
| --long | NA | 显示支持的所有命令的路径。 |
| --version | NA | 显示版本号。|
| NA | NA | 显示所有[command]支持的命令。 |
| [command] | [arguments] | 执行具体的命令。大部分命令也支持--help和--version参数。 |

格式：help [-ah] [command]

| 参数 | 说明 |
| :- | :- |
| command | 显示command的帮助。[command] 可被替换为toybox支持的任意命令。 |

| 选项 | 说明 |
| :- | :- |
| -a | 显示所有命令的帮助。 |

### 数学与计算机基础函数

| 命令 | 说明 |
| :- | :- |
| ascii     | 显示acsii编码表。<br/>usage: ascii |
| factor     | 分解质因数。<br/>usage: factor NUMBER... |
| mcookie | 生成128位强随机数。<br/>usage: mcookie [-vV] |
| mkpasswd | 对密码进行加密。<br/>usage: mkpasswd [-P FD] [-m TYPE] [-S SALT] [PASSWORD] [SALT] |
| uuidgen    | 创建并打印新的RFC4122随机UUID。<br/>usage: uuidgen |

### 终端操作

| 命令 | 说明 |
| :- | :- |
| chvt   | 切换到虚拟终端N。<br/>usage: chvt N |
| chroot | 以指定的根目录运行命令。<br/>usage: chroot NEWROOT [COMMAND [ARG...]] |
| clear  | 清空终端。<br/>usage: clear |
| nohup  | 运行一个独立于终端的命令。<br/>usage: nohup COMMAND [ARG...] |
| tty    | 显示连接到标准输入设备的终端的名称。<br/>usage: tty [-s] |
| reset  | 复位终端。<br/>usage: reset |
| microcom | 简单串口终端。<br/>usage: microcom [-s SPEED] [-X] DEVICE |

### sh逻辑命令

| 命令 | 说明 |
| :- | :- |
| false | 返回非零值。<br/>usage: false |
| sh    | shell命令解释器。 |
| test  | 通过执行测试返回true或false。没有参数时返回false。<br/>usage: test [-bcdefghLPrSsuwx PATH] [-nz STRING] [-t FD] [X ?? Y] |
| true  | 返回零。<br/>usage: true |
| yes   | 反复输出行直到被杀死。如果没有参数，则输出“y”。<br/>usage: yes [args...] |