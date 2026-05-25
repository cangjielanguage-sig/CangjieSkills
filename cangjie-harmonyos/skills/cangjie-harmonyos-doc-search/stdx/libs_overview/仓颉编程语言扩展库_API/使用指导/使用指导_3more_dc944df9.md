## 使用指导

仓颉编程语言扩展库 stdx 二进制包包含静态（static）和 动态 （dynamic） 两部分，请按需引用。

### 二进制产物结构

二进制包解压出来的目录包含 dynamic 和 static 两个目录：

dynamic/stdx 是动态产物，包含动态文件、cjo、bc 文件。

static/stdx 是静态产物，包含静态文件、cjo、bc 文件。

### 包依赖

| 导入库名                                  | 依赖包                                                                                                                                                                                                                         |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |                                                                                                                                                                                                     |
| import stdx.aspectCJ.*                    | stdx.aspectCJ                                                                                                                                                                                                                  |
| import stdx.compress.zlip.*               | stdx.compress.zlib                                                                                                                                                                                                             |
| import stdx.crypto.crypto.*               | stdx.crypto.crypto、stdx.crypto.digest                                                                                                                                               |
| import stdx.crypto.digest.*               | stdx.crypto.digest                                                                                                                                                                   |
| import stdx.crypto.keys.*                 | stdx.crypto.keys、stdx.crypto.x509、stdx.encoding.hex、stdx.crypto.crypto、stdx.crypto.digest、stdx.encoding.base64  |
| import stdx.crypto.x509.*                 | stdx.crypto.x509、stdx.encoding.hex、stdx.crypto.crypto、stdx.crypto.digest、stdx.encoding.base64                      |                                                                                                                                                                                                              |
| import stdx.encoding.hex.*                | stdx.encoding.hex                                                                                                                                                                                                              |
| import stdx.encoding.base64.*             | stdx.encoding.base64                                                                                                                                                                                                           |
| import stdx.encoding.json.*               | stdx.encoding.json、stdx.serialization.serialization                                                                                                                                                                           |
| import stdx.encoding.json.stream.*        | stdx.encoding.json.stream                                                                                                                                                                                                      |
| import stdx.encoding.url.*                | stdx.encoding.url                                                                                                                                                                                                              |
| import stdx.log.*                         | stdx.log                                                                                                                                                                                                                       |
| import stdx.logger.*                      | stdx.logger                                                                                                                                                                                                                    |
| import stdx.serialization.serialization.* | stdx.serialization.serialization                                                                                                                                                                                               |
| import stdx.fuzz.fuzz.*                   | stdx.fuzz.fuzz                                                                                                                                                                                                                 |
| import stdx.net.http .*                   | stdx.net.http、 stdx.net.tls、stdx.logger、stdx.log、stdx.encoding.url、stdx.encoding.json.stream、stdx.crypto.x509、stdx.encoding.hex、stdx.crypto.crypto、stdx.crypto.digest、stdx.encoding.base64 |
| import stdx.net.tls.*                     | stdx.net.tls、stdx.crypto.x509、stdx.encoding.hex、stdx.crypto.crypto、stdx.crypto.digest、stdx.encoding.base64                                                                       |
| import stdx.unittest.data.*               | stdx.encoding.json、stdx.serialization.serialization                                                                                                                                                                           |

代码中导入上述包，用 cjc 命令去编译代码，需要严格按照上述包的依赖的顺序去链接。 如果是用 cjpm 则无需关注。

如果使用静态库，在导入 crypto 和 net 库时，由于需要依赖系统符号，所以 `Windows` 操作系统 需要额外添加 `-lcrypt32`，`Linux` 操作系统 需要额外添加 `-ldl`。