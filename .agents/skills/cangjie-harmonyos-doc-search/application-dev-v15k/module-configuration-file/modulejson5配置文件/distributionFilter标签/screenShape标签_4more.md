### screenShape标签

**表13** screenShape标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| policy | 标识条件属性的过滤规则。<br/>-&nbsp;exclude：表示需要排除的value属性。<br/>-&nbsp;include：表示需要包含的value属性。 | 字符串 | 该标签不可缺省。 |
| value | 支持的取值为circle（圆形）、rect（矩形）。例如，针对智能穿戴设备，可为圆形表盘和矩形表盘分别提供不同的HAP。 | 字符串数组 | 该标签不可缺省。 |

### screenWindow标签

**表14** screenWindow标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| policy | 标识条件属性的过滤规则。当前取值仅支持“include”。<br/>-&nbsp;include：表示需要包含的value属性。 | 字符串 | 该标签不可缺省。 |
| value | 单个字符串的取值格式为“宽&nbsp;\*&nbsp;高”，取值为整数像素值，例如“454&nbsp;\*&nbsp;454”。 | 字符串数组 | 该标签不可缺省。 |

### screenDensity标签

**表15** screenDensity标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| policy | 标识条件属性的过滤规则。<br/>-&nbsp;exclude：表示需要排除的value属性。<br/>-&nbsp;include：表示需要包含的value属性。 | 字符串 | 该标签不可缺省。 |
| value | 标识屏幕的像素密度（dpi&nbsp;:Dot&nbsp;Per&nbsp;Inch）。支持的取值如下：<br/>-&nbsp;sdpi：表示小规模的屏幕密度（Small-scale&nbsp;Dots&nbsp;per&nbsp;Inch），适用于dpi取值为(0,120]的设备。<br/>-&nbsp;mdpi：表示中规模的屏幕密度（Medium-scale&nbsp;Dots&nbsp;Per&nbsp;Inch），适用于dpi取值为(120,160]的设备。<br/>-&nbsp;ldpi：表示大规模的屏幕密度（Large-scale&nbsp;Dots&nbsp;Per&nbsp;Inch），适用于dpi取值为(160,240]的设备。<br/>-&nbsp;xldpi：表示大规模的屏幕密度（Extra&nbsp;Large-scale&nbsp;Dots&nbsp;Per&nbsp;Inch），适用于dpi取值为(240,320]的设备。<br/>-&nbsp;xxldpi：表示大规模的屏幕密度（Extra&nbsp;Extra&nbsp;Large-scale&nbsp;Dots&nbsp;Per&nbsp;Inch），适用于dpi取值为(320，480]的设备。<br/>-&nbsp;xxxldpi：表示大规模的屏幕密度（Extra&nbsp;Extra&nbsp;Extra&nbsp;Large-scale&nbsp;Dots&nbsp;Per&nbsp;Inch），适用于dpi取值为(480,&nbsp;640]的设备。 | 字符串数组 | 该标签不可缺省。 |

### countryCode标签

**表16** countryCode标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| policy | 标识条件属性的过滤规则。<br/>-&nbsp;exclude：表示需要排除的value属性。<br/>-&nbsp;include：表示需要包含的value属性。 | 字符串 | 该标签不可缺省。 |
| value | 标识应用需要分发的国家地区码。 | 字符串数组 | 该标签不可缺省。 |

示例如下：

1. 在开发视图的resources/base/profile下定义配置文件，文件名为distributionFilter_config.json，文件名可以自定义。

   ```json
   {
     "distributionFilter": {
       "screenShape": {
         "policy": "include",
         "value": [
           "circle",
           "rect"
         ]
       },
       "screenWindow": {
         "policy": "include",
         "value": [
           "454*454",
           "466*466"
         ]
       },
       "screenDensity": {
         "policy": "exclude",
         "value": [
           "ldpi",
           "xldpi"
         ]
       },
       "countryCode": { // 支持在中国分发
         "policy": "include",
         "value": [
           "CN"
         ]
       }
     }
   }
   ```

2. 在module.json5配置文件的module标签中定义metadata信息。

   ```json
   {
     "module": {
       // ...
       "metadata": [
         {
           "name": "ohos.module.distribution",
           "resource": "$profile:distributionFilter_config",
         }
       ]
     }
   }
   ```