### var method

```cangjie
public var method: ?String = None
```

**功能：** 上传或下载的HTTP标准方法，包括GET、POST和PUT，不区分大小写。上传时，使用PUT或POST，默认值为PUT。下载时，使用GET或POST，默认值为GET。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 12

### var mode

```cangjie
public var mode: ?Mode = None
```

**功能：** 任务模式, 默认为后台任务。

**类型：** ?[Mode](#enum-mode)

**读写能力：** 可读写

**起始版本：** 12

### var network

```cangjie
public var network: Network = Network.ANY
```

**功能：** 网络选项，当前支持无线网络WIFI和蜂窝数据网络CELLULAR，默认为ANY（WIFI或CELLULAR）。

**类型：** [Network](#enum-network)

**读写能力：** 可读写

**起始版本：** 12

### var overwrite

```cangjie
public var overwrite: Bool = false
```

**功能：** 下载过程中路径已存在时的解决方案选择，默认为false。true：覆盖已存在的文件。false：下载失败。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

### var precise

```cangjie
public var precise: Bool = false
```

**功能：** 如果设置为true，在上传/下载无法获取文件大小时任务失败。如果设置为false，将文件大小设置为-1时任务继续。默认值为false。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

### var priority

```cangjie
public var priority: UInt32 = 0
```

**功能：** 任务的优先级。任务模式相同的情况下，该配置项的数字越小优先级越高，默认值为0。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 12

### var redirect

```cangjie
public var redirect: Bool = true
```

**功能：** 是否允许重定向，默认为true。true：是。false：否。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

### var retry

```cangjie
public var retry: Bool = true
```

**功能：** 是否为后台任务启用自动重试，仅应用于后台任务，默认为true。true：是。false：否。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

### var roaming

```cangjie
public var roaming: Bool = true
```

**功能：** 是否允许在漫游网络中工作，默认为true。true：是。false：否。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

### var saveas

```cangjie
public var saveas: ?String = None
```

**功能：** 保存下载文件的路径，包括如下几种：
-相对路径，位于调用方的缓存路径下，如"./xxx/yyy/zzz.html"、"xxx/yyy/zzz.html"。
-internal协议路径，仅支持"internal://cache/"及其子路径，如"internal://cache/path/to/file.txt"。-应用沙箱目录，只支持到base及其子目录下，如"/data/storage/el1/base/path/to/file.txt"。
-file协议路径，必须匹配应用包名，只支持到base及其子目录下，如"file://com.example.test/data/storage/el2/base/file.txt"。
默认为相对路径，即下载至调用方当前缓存路径下。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 12

### var title

```cangjie
public var title: ?String = None
```

**功能：** 任务标题，其最大长度为256个字符，默认值为小写的upload或download，与上面的action保持一致。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 12

### var token

```cangjie
public var token: ?String = None
```

**功能：** 当创建了一个带有token的任务后，token则为正常查询期间必须提供的，否则将无法通过查询进行检索。其最小长度为8个字节，最大长度为2048个字节。默认为空。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 12

### var url

```cangjie
public var url: String
```

**功能：** 资源地址，其最大长度为2048个字符。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12