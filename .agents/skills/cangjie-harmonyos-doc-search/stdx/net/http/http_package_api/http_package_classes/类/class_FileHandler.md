## class FileHandler

```cangjie
public class FileHandler <: HttpRequestHandler {
    public init(path: String, handlerType!: FileHandlerType = DownLoad, bufferSize!: Int64 = 64 * 1024)
}
```

功能：用于处理文件下载或者文件上传。

文件下载：

- 构造 [FileHandler](http_package_classes.md#class-filehandler) 时需要传入待下载文件的路径，目前一个 [FileHandler](http_package_classes.md#class-filehandler) 只能处理一个文件的下载；
- 下载文件只能使用 GET 请求，其他请求返回 400 状态码；
- 文件如果不存在，将返回 404 状态码。

文件上传：

- 构造 [FileHandler](http_package_classes.md#class-filehandler) 时需要传入一个存在的目录路径，上传到服务端的文件将保存在这个目录中；
- 上传文件时只能使用 POST 请求，其他请求返回 400 状态码；
- 上传数据的 http 报文必须是 `multipart/form-data` 格式的，`Content-Type` 头字段的值为 `multipart/form-data; boundary=----XXXXX`；
- 上传文件的文件名存放在 `form-data` 数据报文中，报文数据格式为 `Content-Disposition: form-data; name="xxx"; filename="xxxx"`，文件名是 `filename` 字段的值；
- 目前 form-data 中必须包含 filename 字段；
- 如果请求报文不正确，将返回 400 状态码；
- 如果出现其他异常，例如文件处理异常，将返回 500 状态码。

父类型：

- [HttpRequestHandler](http_package_interfaces.md#interface-httprequesthandler)

### init(String, FileHandlerType, Int64)

```cangjie
public init(path: String, handlerType!: FileHandlerType = DownLoad, bufferSize!: Int64 = 64 * 1024)
```

功能：[FileHandler](http_package_classes.md#class-filehandler) 的构造函数。

参数：

- path: String - [FileHandler](http_package_classes.md#class-filehandler) 构造时需要传入的文件或者目录路径字符串，上传模式中只能传入存在的目录路径；路径中存在../时，用户需要确认标准化后的绝对路径是期望传入的路径。
- handlerType!: [FileHandlerType](http_package_enums.md#enum-filehandlertype) - 构造 [FileHandler](http_package_classes.md#class-filehandler) 时指定当前 [FileHandler](http_package_classes.md#class-filehandler) 的工作模式，默认为 DownLoad 下载模式。
- bufferSize!: Int64 - 内部从网络读取或者写入的缓冲区大小，默认值为 64*1024（64k），若小于 4096，则使用 4096 作为缓冲区大小。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 当 path 不存在时，抛出异常。
- IllegalArgumentException - 参数错误时抛出异常，如 path 为空或者包含空字符串等。

### func handle(HttpContext)

```cangjie
public func handle(ctx: HttpContext): Unit
```

功能：根据请求对响应数据进行处理。

参数：

- ctx: [HttpContext](http_package_classes.md#class-httpcontext) - Http 请求上下文。