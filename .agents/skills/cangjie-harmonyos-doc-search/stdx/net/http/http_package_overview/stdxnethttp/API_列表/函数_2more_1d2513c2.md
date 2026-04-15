### 函数

|              函数名          |           功能           |
| --------------------------- | ------------------------ |
| [handleError(HttpContext, UInt16)](./http_package_api/http_package_funcs.md#func-handleerrorhttpcontext-uint16) | 便捷的 Http 请求处理函数，用于回复错误请求。  |
| [notFound(HttpContext)](./http_package_api/http_package_funcs.md#func-notfoundhttpcontext) | 便捷的 Http 请求处理函数，用于回复 404 响应。 |
| [upgrade(HttpContext)](./http_package_api/http_package_funcs.md#func-upgradehttpcontext) | 在 handler 内获取 StreamingSocket，可用于支持协议升级和处理 CONNECT 请求。  |

### 接口

|             接口名          |           功能           |
| --------------------------- | ------------------------ |
| [CookieJar](./http_package_api/http_package_interfaces.md#interface-cookiejar) | Client 用来管理 Cookie 的工具。  |
| [HttpRequestDistributor](./http_package_api/http_package_interfaces.md#interface-httprequestdistributor) | Http request 分发器接口，将一个 request 按照 url 中的 path 分发给对应的 HttpRequestHandler 处理。  |
| [HttpRequestHandler](./http_package_api/http_package_interfaces.md#interface-httprequesthandler) | Http request 处理器。  |
| [ProtocolServiceFactory](./http_package_api/http_package_interfaces.md#interface-protocolservicefactory) | Http 服务实例工厂，用于生成 `ProtocolService` 实例。  |