## class HttpResponseCache

```cangjie
public class HttpResponseCache {}
```

**功能：** 存储HTTP访问请求响应的对象。在调用HttpResponseCache的方法前，需要先通过[createHttpResponseCache](#func-createhttpresponsecacheuint32)创建一个任务。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### func delete()

```cangjie
public func delete(): Unit
```

**功能：** 禁用缓存并删除其中的数据。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import ohos.hilog.Hilog

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

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import ohos.hilog.Hilog

let httpResponseCache = createHttpResponseCache()
try {
    httpResponseCache.flush()
} catch (e: BusinessException) {
    Hilog.info(0, "", "${e}")
}
```