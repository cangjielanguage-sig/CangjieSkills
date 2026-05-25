# 应用/组件级配置

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

在开发应用时，需要配置应用的一些标签，例如应用的包名、图标等标识特征的属性。本文描述了在开发应用需要配置的一些关键标签。

## 应用包名配置

应用需要在工程的AppScope目录下的[app.json5配置文件](../cj-start/basic-knowledge/cj-app-configuration-file.md)中配置bundleName标签，该标签用于标识应用的唯一性。推荐采用反域名形式命名（如`com.example.demo`，建议第一级为域名后缀com，第二级为厂商/个人名，第三级为应用名，也可以多级）。