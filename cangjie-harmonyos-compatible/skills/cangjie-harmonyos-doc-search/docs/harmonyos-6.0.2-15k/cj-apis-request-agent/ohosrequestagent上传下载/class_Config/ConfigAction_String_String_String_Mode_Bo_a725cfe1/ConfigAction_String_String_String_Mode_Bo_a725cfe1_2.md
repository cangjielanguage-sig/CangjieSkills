|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|action|[Action](#enum-action)|是|-| **命名参数。** 任务操作选项。<br>- UPLOAD表示上传任务。<br>- DOWNLOAD表示下载任务。|
|url|String|是|-| **命名参数。** 资源地址，其最大长度为2048个字符。|
|title|?String|否|None| **命名参数。** 任务标题，其最大长度为256个字符，默认值为小写的upload 或download，与上面的action 保持一致。|
|description|?String|否|None| **命名参数。** 任务的详细信息，其最大长度为1024个字符，默认值为空字符串。|
|mode|?[Mode](#enum-mode)|否|None| **命名参数。** 任务模式, 默认为后台任务。|
|overwrite|Bool|否|false| **命名参数。** 下载过程中路径已存在时的解决方案选择，默认为false。<br>- true，覆盖已存在的文件。<br>- false，下载失败。|
|method|?String|否|None| **命名参数。** 上传或下载的HTTP标准方法，包括GET、POST和PUT，不区分大小写。<br>-上传时，使用PUT或POST，默认值为PUT。<br>-下载时，使用GET或POST，默认值为GET。|
|headers|?HashMap&lt;String, String&gt;|否|None| **命名参数。** 添加要包含在任务中的HTTP协议标志头。<br>-对于上传请求，默认的Content-Type为"multipart/form-data"。<br>-对于下载请求，默认的Content-Type为"application/json"。 |
|data|?[ConfigDataType](#enum-configdatatype)|否|None| **命名参数。** -下载时，data为字符串类型，通常使用json(object将被转换为json文本)，默认为空。<br>-上传时，data是表单项数组Array&lt;FormItem&gt;，默认为空。|
|saveas|?String|否|None| **命名参数。** 保存下载文件的路径，包括如下几种：<br>-相对路径，位于调用方的缓存路径下，如"./xxx/yyy/zzz.html"、"xxx/yyy/zzz.html"。<br>-internal协议路径，仅支持"internal://cache/"及其子路径，如"internal://cache/path/to/file.txt"。<br>-应用沙箱目录，只支持到base及其子目录下，如"/data/storage/el1/base/path/to/file.txt"。<br>-file协议路径，必须匹配应用包名，只支持到base及其子目录下，如"file://com.example.test/data/storage/el2/base/file.txt"。<br>默认为相对路径，即下载至调用方当前缓存路径下。|
|network|[Network](#enum-network)|否|Network.ANY| **命名参数。** 网络选项，当前支持无线网络WIFI和蜂窝数据网络CELLULAR，默认为ANY（WIFI或CELLULAR）。|
|metered|Bool|否|false| **命名参数。** 是否允许在按流量计费的网络中工作，默认为false。<br>-true：是<br>-false：否|
|roaming|Bool|否|true| **命名参数。** 是否允许在漫游网络中工作，默认为true。<br>-true：是<br>-false：否|
|retry|Bool|否|true| **命名参数。** 是否为后台任务启用自动重试，仅应用于后台任务，默认为true。<br>-true：是<br>-false：否|
|redirect|Bool|否|true| **命名参数。** 是否允许重定向，默认为true。<br>-true：是<br>-false：否|
|index|UInt32|否|0| **命名参数。** 任务的路径索引，通常用于任务断点续传，默认为0。 |
|begins|Int64|否|0| **命名参数。** 文件起点，通常用于断点续传。默认值为0，取值为闭区间。<br>-下载时，请求读取服务器开始下载文件时的起点位置（http协议中设置"Range"选项）。<br>-上传时，在上传开始时读取。|
|ends|Int64|否|- 1| **命名参数。** 文件终点，通常用于断点续传。默认值为-1，取值为闭区间。<br>-下载时，请求读取服务器开始下载文件时的结束位置（http协议中设置"Range"选项）。<br>-上传时，在上传时结束读取。|
|gauge|Bool|否|false| **命名参数。** 后台任务的过程进度通知策略，仅应用于后台任务，默认值为false。<br>-false：代表仅完成或失败的通知。<br>-true：发出每个进度已完成或失败的通知。|
|precise|Bool|否|false| **命名参数。** -如果设置为true，在上传/下载无法获取文件大小时任务失败。<br>-如果设置为false，将文件大小设置为-1时任务继续。<br>默认值为false。|
|token|?String|否|None| **命名参数。** 当创建了一个带有token的任务后，token则为正常查询期间必须提供的，否则将无法通过查询进行检索。其最小为8个字节，最大为2048个字节。默认为空。|
|priority|UInt32|否|0| **命名参数。** 任务的优先级。任务模式相同的情况下，该配置项的数字越小优先级越高，默认值为0。|
|extras|?HashMap&lt;String, String&gt;|否|None| **命名参数。** 配置的附加功能，默认为空。|