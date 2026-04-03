| 参数名      | 类型 | 必填 | 默认值                     | 说明 |
| :---------- | :--------- | :--- | :------- | :-------- |
| action      | [Action](#enum-action) | 是   | - | **命名参数。** 任务操作选项。|
| url         | String | 是   | - | **命名参数。** 资源地址。最大长度为8192个字符。支持HTTP拦截功能。|
| title       | ?String | 否   | None | **命名参数。** 任务标题，其最大长度为256个字符，默认值为小写的 upload 或 download，与上面的 action 保持一致。|
| description | String | 否   | "" | **命名参数。** 任务的详细信息，其最大长度为1024个字符，默认值为空字符串。|
| mode        | [Mode](#enum-mode) | 否   | Mode.Background | **命名参数。** 任务模式，默认为后台任务。下载到用户文件场景必须为request.agent.Mode.FOREGROUND。|
| overwrite   | Bool | 否   | false | **命名参数。** 下载过程中路径已存在时的解决方案选择，默认为false。|
| method      | ?String | 否   | None  | **命名参数。** 上传或下载HTTP的标准方法，包括GET、POST和PUT，不区分大小写。|
| headers     | HashMap\<String,String>  | 否   | HashMap<String,String>()   | **命名参数。** 添加要包含在任务中的HTTP协议标志头。|
| data        | ?[ConfigData](#enum-configdata) | 否   | None | **命名参数。** - 下载时，data为字符串类型，通常情况下使用json格式（object将被转换为json文本），默认为空。|
| saveas      | String | 否   | "./" | **命名参数。** 保存下载文件的路径。|
| network     | [Network](#enum-network)  | 否   | Network.AnyType | **命名参数。** 网络选项，当前支持无线网络Wifi和蜂窝数据网络Cellular，默认为Network.AnyType（Wifi或Cellular）。|
| metered     | Bool | 否   | false  | **命名参数。** 是否允许在按流量计费的网络中工作，默认为false。|
| roaming     | Bool | 否   | true | **命名参数。** 是否允许在漫游网络中工作，默认为true。|
| retry       | Bool | 否   | true | **命名参数。** 是否为后台任务启用自动重试，仅应用于后台任务，默认为true。|
| redirect    | Bool | 否   | true | **命名参数。** 是否允许重定向，默认为true。|
| index       | UInt32 | 否   | 0 | **命名参数。** 任务的路径索引，通常情况下用于任务断点续传，默认为0。|
| begins      | Int64 | 否   | 0 | **命名参数。** 文件起点，通常情况下用于断点续传。默认值为0，取值为闭区间，表示从头开始传输。。|
| ends        | Int64 | 否   | - 1 | **命名参数。** 文件终点，通常情况下用于断点续传。默认值为-1，取值为闭区间，表示传输到整个文件末尾结束。|
| gauge       | Bool | 否   | false | **命名参数。** 后台任务的过程进度通知策略，仅应用于后台任务，默认值为false。|
| precise     | Bool | 否   | false | **命名参数。** - 如果设置为true，在上传/下载无法获取文件大小时任务失败。|
| token       | ?String | 否   | None | **命名参数。** 任务令牌。查询带有token的任务需提供token并通过[request.agent.touch](#func-touchstring-string)查询，否则无法查询到指定任务。其最小为8个字节，最大为2048个字节。默认为空。|
| priority    | UInt32 | 否   | 0 | **命名参数。** 任务的优先级。前台任务的优先级比后台任务高。任务模式相同的情况下，该配置项的数字越小优先级越高，默认值为0。|
| extras      | HashMap\<String,String> | 否   | HashMap\<String, String>() | **命名参数。** 配置的附加功能，默认为空。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let config = Config(
        Action.Download,
        "https://example.com/file.txt",
        title: "示例下载任务",
        description: "这是一个示例下载任务",
        mode: Mode.Background,
        overwrite: true,
        network: Network.Wifi,
        metered: false,
        roaming: true,
        retry: true,
        redirect: true,
        gauge: false,
        precise: false,
        priority: 0
    )
    Hilog.info(0, "test", "成功创建配置对象")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```