## deviceTypes标签

**表2** deviceTypes标签说明
<!--RP2-->
| 设备类型 | 枚举值 | 说明 |
| -------- | -------- | -------- |
| 平板 | tablet | - |
| 默认设备 | default | 支持使用所有系统能力的设备。 |
<!--RP2End-->

deviceTypes示例：

```json
{
  "module": {
    "name": "myHapName",
    "type": "feature",
    "deviceTypes" : [
       "tablet"
    ]
  }
}
```

## pages标签

该标签是一个profile文件资源，用于指定描述页面信息的配置文件。

```json
{
  "module": {
    // ...
    "pages": "$profile:main_pages", // 通过profile下的资源文件配置
  }
}
```

在开发视图的resources/base/profile下面定义配置文件main_pages.json，其中文件名"main_pages"可自定义，需要和pages标签指定的信息对应。配置文件中列举了当前应用组件中的页面信息，包含页面的路由信息和显示窗口相关的配置。

**表3** pages标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- |-----------| -------- | -------- |
| src | 标识当前Module中所有页面的路由信息，包括页面路径和页面名称。其中，页面路径是以当前Module的src/main/cangjie为基准。该标签取值为一个字符串数组，其中每个元素表示一个页面。 | 字符串数组 | 该标签不可缺省。 |
| window | 标识用于定义与显示窗口相关的配置。 | 对象 | 该标签可缺省，缺省值为空。 |

**表4** window标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省  |
| -------- | -------- | -------- |-----------------|
| designWidth | 标识页面设计基准宽度。以此为基准，根据实际设备宽度来缩放元素大小。 | 数值 | 可缺省，缺省值为720.px。 |
| autoDesignWidth | 标识页面设计基准宽度是否自动计算。当配置为true时，designWidth将会被忽略，设计基准宽度由设备宽度与屏幕密度计算得出。当配置为false时，设计基准宽度为designWidth。 | 布尔值 | 可缺省，缺省值为false。  |

```json
{
  "src": [
    "pages/index/mainPage",
    "pages/second/payment",
    "pages/third/shopping_cart",
    "pages/four/owner"
  ],
  "window": {
    "designWidth": 720,
    "autoDesignWidth": false
  }
}
```