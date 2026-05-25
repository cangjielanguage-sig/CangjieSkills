# User-Agent开发指导

User-Agent（简称UA）是一个特殊的字符串，包含设备类型、操作系统及版本等关键信息。在Web开发中，这个字符串使服务器能够识别请求的来源设备及其特性，从而根据这些信息提供定制化的内容和服务。如果页面无法正确识别UA，可能会导致多种异常情况。例如，为移动设备优化的页面布局可能会在桌面设备上显示错乱，反之亦然。此外，某些特定的浏览器功能或CSS样式可能仅在特定的浏览器版本中受支持，如果页面无法根据UA字符串做出正确的判断，就可能导致渲染问题或逻辑错误。

## 默认User-Agent结构

- 默认User-Agent定义

    ```cangjie
    Mozilla/5.0 ({DeviceType}; {OSName} {OSVersion}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ChromeCompatibleVersion}.0.0.0 Safari/537.36  ArkWeb/{ArkWeb VersionCode} {DeviceCompat} {扩展区}
    ```

- 举例说明

    ```cangjie
    Mozilla/5.0 (Phone; OpenHarmony 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36  ArkWeb/4.1.6.1 Mobile
    ```

- 字段说明

    | 字段                  | 含义                                                         |
    | :--------------------- | :------------------------------------------------------------ |
    | DeviceType            | 当前的设备类型。<br>取值范围：<br>- Phone：手机<br>- Tablet：平板设备<br>-  PC：2in1设备 |
    | OSName                | 基础操作系统名称。<br>默认取值：OpenHarmony                  |
    | OSVersion             | 基础操作系统版本，两位数字，M.S。<br>通过系统参数const.ohos.fullname解析版本号得到，取版本号部分M.S前两位。<br>默认取值：例如5.0       |
    | ChromeCompatibleVersion | 兼容Chrome主版本的版本号，从114版本开始演进。<br>默认取值：114            |
    | ArkWeb                | HarmonyOS版本Web内核名称。<br>默认取值：ArkWeb             |
    | ArkWeb VersionCode    | ArkWeb版本号，格式a.b.c.d。<br>默认取值：例如4.1.6.1         |
    | DeviceCompat          | 前向兼容字段。<br>默认取值：Mobile                          |
    | 扩展区                | 三方应用可以扩展的字段。<br>三方应用使用ArkWeb组件时，可以做UA扩展，例如加入APP相关信息标识。 |

> **说明：**
>
> - 当前默认User-Agent的ArkWeb字段前有两个空格。
> - 当前通过User-Agent中是否含有"Mobile"字段来判断是否开启前端HTML页面中meta标签的viewport属性。当User-Agent中不含有"Mobile"字段时，meta标签中viewport属性默认关闭，此时可通过显性设置[metaViewport](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#func-metaviewportbool)属性为true来覆盖关闭状态。
> - 建议通过OpenHarmony关键字识别是否是HarmonyOS设备，同时可以通过DeviceType识别设备类型用于不同设备上的页面显示（ArkWeb关键字表示设备使用的web内核，OpenHarmony关键字表示设备使用的操作系统，因此推荐通过OpenHarmony关键字识别是否是HarmonyOS设备）。