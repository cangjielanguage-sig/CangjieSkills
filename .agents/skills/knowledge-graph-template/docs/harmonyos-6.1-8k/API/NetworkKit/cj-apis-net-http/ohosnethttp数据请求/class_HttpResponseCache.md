## class HttpResponseCache

```cangjie
public class HttpResponseCache {}
```

**功能：** 存储HTTP访问请求响应的对象。在调用HttpResponseCache的方法前，需要先通过[createHttpResponseCache()](#func-createhttpresponsecacheuint32)创建一个任务。

**响应头中的相应关键字使用**

- **`Cache-Control`**：用于指定缓存策略，如`no-cache`, `no-store`, `max-age`, `public`, `private`等。

- **`Expires`**：指定资源的过期时间，格式为GMT时间。

- **`ETag`**：用于资源版本标识，客户端可以使用`If-None-Match`请求头来验证资源是否已更改。

- **`Last-Modified`**：指定资源最后修改时间，客户端可以使用`If-Modified-Since`请求头来验证资源是否已更改。

- **`Vary`**：指定哪些请求头的值会影响缓存的响应，用于区分不同的缓存版本。

使用这些关键字时，服务器端需要正确配置响应头，客户端则需要根据这些响应头来决定是否使用缓存的资源，以及如何验证资源是否是最新的。正确的缓存策略可以显著提高应用的性能和用户体验。

**如何设置Cache-Control头**

`Cache-Control`为通用报头，但通常是在服务器端进行的，允许定义一个响应资源应该何时、如何被缓存以及缓存多长时间。以下是一些常用的`Cache-Control`指令及其含义：

- **`no-cache`**：表示在使用缓存前，必须先去源服务器校验资源的有效性。如果资源未变更，则响应状态码为304(Not Modified)，不发送资源内容，使用缓存中的资源。如果资源已经过期，则响应状态码为200(OK)，并发送资源内容。

- **`no-store`**：表示不允许缓存资源，每次请求都必须从服务器获取资源。

- **`max-age`**：指定缓存的最大时间(以秒为单位)。例如，`Cache-Control: max-age=3600`表示缓存的有效期为1小时。

- **`public`**：表明响应可以被任何对象(包括：发送请求的客户端，代理服务器等)缓存。

- **`private`**：表明响应只能被单个用户缓存，不能作为共享缓存(即代理服务器不能缓存)。

- **`must-revalidate`**：表示必须在使用缓存前验证旧资源的状态，并且在缓存过期后，需要重新验证资源。

- **`no-transform`**：表示不允许代理服务器修改响应内容。

- **`proxy-revalidate`**：与`must-revalidate`类似，但仅适用于共享缓存。

- **`s-maxage`**：类似于`max-age`，但仅适用于共享缓存。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### func delete()

```cangjie
public func delete(): Unit
```

**功能：** 禁用缓存并删除其中的数据。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import ohos.business_exception.*
import kit.NetworkKit.*
import kit.PerformanceAnalysisKit.Hilog

let httpResponseCache = createHttpResponseCache()
try {
    httpResponseCache.delete()
} catch (e: BusinessException) {
    Hilog.info(0, "", "${e}")
}
```

### func flush()

```cangjie
public func flush(): Unit
```

**功能：** 将缓存中的数据写入文件系统，以便在下一个HTTP请求中访问所有缓存数据。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import ohos.business_exception.*
import kit.NetworkKit.*
import kit.PerformanceAnalysisKit.Hilog

let httpResponseCache = createHttpResponseCache()
try {
    httpResponseCache.flush()
} catch (e: BusinessException) {
    Hilog.info(0, "", "${e}")
}
```