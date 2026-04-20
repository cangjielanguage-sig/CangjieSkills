## struct ServicePoolConfig

```cangjie
public struct ServicePoolConfig {
    public let capacity: Int64
    public let queueCapacity: Int64
    public let preheat: Int64
    public init(capacity!: Int64 = 10 ** 4, queueCapacity!: Int64 = 10 ** 4, preheat!: Int64 = 0)
}
```

功能：Http [Server](http_package_classes.md#class-server) 协程池配置。

> **说明：**
>
> HTTP/1.1 [Server](http_package_classes.md#class-server) 每次收到一个请求，将从协程池取出一个协程进行处理，如果任务等待队列已满，将拒绝服务该次请求，并断开连接。
> HTTP/2 [Server](http_package_classes.md#class-server) 处理过程中会从协程池取出若干协程进行处理，如果任务等待队列已满，将阻塞直至有协程空闲。

### let capacity

```cangjie
public let capacity: Int64
```

功能：获取协程池容量。

类型：Int64

### let preheat

```cangjie
public let preheat: Int64
```

功能：获取服务启动时预先启动的协程数量。

类型：Int64

### let queueCapacity

```cangjie
public let queueCapacity: Int64
```

功能：获取缓冲区等待任务的最大数量。

类型：Int64

### init(Int64, Int64, Int64)

```cangjie
public init(
    capacity!: Int64 = 10 ** 4,
    queueCapacity!: Int64 = 10 ** 4,
    preheat!: Int64 = 0
)
```

功能：构造一个 [ServicePoolConfig](http_package_structs.md#struct-servicepoolconfig) 实例。

参数：

- capacity!: Int64 - 协程池容量，默认值为 10000。
- queueCapacity!: Int64 - 缓冲区等待任务的最大数量，默认值为 10000。
- preheat!: Int64 - 服务启动时预先启动的协程数量，默认值为 0。

异常：

- IllegalArgumentException - 当参数 capacity/queueCapacity/preheat 小于 0，或参数 preheat 大于 capacity。

## struct TransportConfig

```cangjie
public struct TransportConfig
```

功能：传输层配置类，服务器建立连接使用的传输层配置。

### prop keepAliveConfig

```cangjie
public mut prop keepAliveConfig: SocketKeepAliveConfig
```

功能：设定和读取传输层连接的消息保活配置，默认配置空闲时间为 45s，发送探测报文的时间间隔为 5s，在连接被认为无效之前发送的探测报文数 5 次，实际时间粒度可能因操作系统而异。

类型：SocketKeepAliveConfig

### prop readBufferSize

```cangjie
public mut prop readBufferSize: ?Int64
```

功能：设定和读取传输层连接的读缓冲区大小，默认值为 None ，若设置的值小于 0，将在服务器进行服务建立连接后抛出 IllegalArgumentException。

> **说明：**
>
> 使用默认值时，实际的缓冲区大小将由操作系统决定。

类型：?Int64

### prop readTimeout

```cangjie
public mut prop readTimeout: Duration
```

功能：设定和读取传输层连接的读超时时间，如果设置的时间小于 0 将置为 0，默认值为 Duration.Max。

类型：Duration

### prop writeBufferSize

```cangjie
public mut prop writeBufferSize: ?Int64
```

功能：设定和读取传输层连接的写缓冲区大小，默认值为 None ，若设置的值小于 0，将在服务器进行服务建立连接后抛出 IllegalArgumentException。

> **说明：**
>
> 使用默认值时，实际的缓冲区大小将由操作系统决定。

类型：?Int64

### prop writeTimeout

```cangjie
public mut prop writeTimeout: Duration
```

功能：设定和读取传输层连接的写超时时间，如果设置的时间小于 0 将置为 0，默认值为 Duration.Max。

类型：Duration