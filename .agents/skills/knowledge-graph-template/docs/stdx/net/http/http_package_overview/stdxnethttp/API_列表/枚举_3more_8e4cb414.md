### 枚举

|             枚举名          |           功能           |
| --------------------------- | ------------------------ |
| [FileHandlerType](./http_package_api/http_package_enums.md#enum-filehandlertype) | 用于设置 `FileHandler` 是上传还是下载模式。  |
| [Protocol](./http_package_api/http_package_enums.md#enum-protocol) | 定义 HTTP 协议类型枚举。  |
| [WebSocketFrameType](./http_package_api/http_package_enums.md#enum-websocketframetype) | 定义 `WebSocketFrame` 的枚举类型。  |

### 结构体

|            结构体名          |           功能           |
| --------------------------- | ------------------------ |
| [HttpStatusCode](./http_package_api/http_package_structs.md#struct-httpstatuscode) | 用来表示网页服务器超文本传输协议响应状态的 3 位数字代码。  |
| [ServicePoolConfig](./http_package_api/http_package_structs.md#struct-servicepoolconfig) | Http Server 协程池配置。  |
| [TransportConfig](./http_package_api/http_package_structs.md#struct-transportconfig) | 传输层配置类，服务器建立连接使用的传输层配置。  |

### 异常类

|            异常类名          |           功能           |
| --------------------------- | ------------------------ |
| [ConnectionException](./http_package_api/http_package_exceptions.md#class-connectionexception) | Http 的 tcp 连接异常类。  |
| [CoroutinePoolRejectException](./http_package_api/http_package_exceptions.md#class-coroutinepoolrejectexception) | Http 的协程池拒绝请求处理异常类。  |
| [HttpException](./http_package_api/http_package_exceptions.md#class-httpexception) | Http 的通用异常类。  |
| [HttpStatusException](./http_package_api/http_package_exceptions.md#class-httpstatusexception) | Http 的响应状态异常类。  |
| [HttpTimeoutException](./http_package_api/http_package_exceptions.md#class-httptimeoutexception) | Http 的超时异常类。  |
| [WebSocketException](./http_package_api/http_package_exceptions.md#class-websocketexception) | WebSocket 的通用异常类。  |