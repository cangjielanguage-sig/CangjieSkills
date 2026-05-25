# 显式Want与隐式Want匹配规则

在启动目标应用组件时，会通过显式[Want](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)或者隐式[Want](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)进行目标应用组件的匹配。本章所述的匹配规则是：调用方传入的[Want](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)参数中设置的参数如何与目标应用组件声明的配置文件进行匹配。

## 显式Want匹配原理

显式[Want](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)匹配原理如下表所示。

| 名称 | 类型 | 匹配项 | 必选 | 规则 |
| -------- | -------- | -------- | -------- | -------- |
| deviceId | String | 是 | 否 | 留空将仅匹配本设备内的应用组件。 |
| bundleName | String | 是 | 是 | 如果指定abilityName，而不指定bundleName，则匹配失败。 |
| moduleName | String | 是 | 否 | 留空时当同一个应用内存在多个模块且模块间存在重名应用组件，将默认匹配第一个。 |
| abilityName | String | 是 | 是 | 该字段必须设置表示显式匹配。 |
| uri | String | 否 | 否 | 系统匹配时将忽略该参数，但仍可作为参数传递给目标应用组件。 |
| type | String | 否 | 否 | 系统匹配时将忽略该参数，但仍可作为参数传递给目标应用组件。 |
| action | String | 否 | 否 | 系统匹配时将忽略该参数，但仍可作为参数传递给目标应用组件。 |
| entities | Array&lt;String&gt; | 否 | 否 | 系统匹配时将忽略该参数，但仍可作为参数传递给目标应用组件。 |
| flags | UInt32 | 否 | 否 | 不参与匹配，直接传递给系统处理，一般用来设置运行态信息，例如URI数据授权等。 |
| parameters | String | 否 | 否 | 不参与匹配，应用自定义数据将直接传递给目标应用组件。 |