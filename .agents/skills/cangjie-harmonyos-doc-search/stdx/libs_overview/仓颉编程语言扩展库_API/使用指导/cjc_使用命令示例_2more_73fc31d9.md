### cjc 使用命令示例

cjc 的介绍和编译请查看 cangjie 用户手册

```cangjie
import stdx.aspectCJ.*
import stdx.compress.zlib.*
import stdx.crypto.crypto.*
import stdx.crypto.digest.*
import stdx.crypto.keys.*
import stdx.crypto.x509.*
import stdx.encoding.hex.*
import stdx.encoding.base64.*
import stdx.encoding.json.*
import stdx.encoding.url.*
import stdx.encoding.json.stream.*
import stdx.net.tls.*
import stdx.net.http.*
import stdx.log.*
import stdx.logger.*
import stdx.serialization.serialization.*
main() {
    0
}
```

Linux 和 mac 的编译命令：

```shell
$ cjc main.cj -L $CANGJIE_STDX_PATH -lstdx.aspectCJ -lstdx.encoding.json -lstdx.serialization.serialization -lstdx.net.http -lstdx.net.tls -lstdx.logger -lstdx.log -lstdx.encoding.url -lstdx.encoding.json.stream -lstdx.crypto.keys -lstdx.crypto.x509 -lstdx.encoding.hex -lstdx.crypto.crypto -lstdx.crypto.digest -lstdx.encoding.base64 -lstdx.compress.zlib -lstdx.compress -ldl --import-path $CANGJIE_STDX_PATH -o main.out
```

windows 编译命令：

```shell
$ cjc main.cj -L $CANGJIE_STDX_PATH -lstdx.aspectCJ -lstdx.encoding.json -lstdx.serialization.serialization -lstdx.net.http -lstdx.net.tls -lstdx.logger -lstdx.log -lstdx.encoding.url -lstdx.encoding.json.stream -lstdx.crypto.keys -lstdx.crypto.x509 -lstdx.encoding.hex -lstdx.crypto.crypto -lstdx.crypto.digest -lstdx.encoding.base64 -lstdx.compress.zlib -lstdx.compress -lcrypt32 --import-path $CANGJIE_STDX_PATH -o main.out
```

CANGJIE_STDX_PATH 是设置的 stdx 路径。

例如在 linux 系统中设置：

```shell
export CANGJIE_STDX_PATH=/target/linux_x86_64_cjnative/dynamic/stdx
```

运行前 Linux 操作系统需要在 LD_LIBRARY_PATH 中设置扩展库的路径，Windows 操作系统需要在 PATH 中设置扩展库的路径，macOS 操作系统需要在 DYLD_LIBRARY_PATH 中设置扩展库的路径。

### cjpm 使用示例

cjpm 的介绍和使用请查看 cjpm 手册。

cjpm.toml 增加如下配置：

```text
[target.x86_64-unknown-linux-gnu]
  [target.x86_64-unknown-linux-gnu.bin-dependencies]
    path-option = ["${CANGJIE_STDX_PATH}"]
```

上面配置中 x86_64-unknown-linux-gnu 这是表示的系统架构信息，需要通过 cjc -v 获取。并替换成自己获取的系统信息。
CANGJIE_STDX_PATH 是设置的 stdx 路径。