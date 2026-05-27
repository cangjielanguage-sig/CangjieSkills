# 指定用户空间进行关键资产操作（仅对系统应用开放）（仓颉）

对于提供了系统级管理功能的单实例应用，一般场景下，所有用户共用一个实例，该实例负责实现不同用户的数据隔离。

1. 当同时有多个用户处于活跃状态时，单实例应用如果需要为不同用户存储、访问、销毁关键资产，则需要准确告知所操作的关键资产所属的用户空间。
2. 单实例应用需要存储“首次解锁后可访问”、“解锁状态时可访问”类型的关键资产时，需要指定关键资产所属的用户空间。

为了支持上述场景中单实例应用的关键资产数据隔离和访问控制，ASSET提供了一套可以指定用户空间进行关键资产操作的接口（仅面向系统应用）。

## 约束与限制

使用接口需要申请权限：ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS。

申请流程请参考：[申请应用权限](../AccessToken/cj-determine-application-mode.md#应用申请权限的方式)。

## 接口介绍

可通过API文档查看相关接口：

|基础功能接口（不指定用户空间）<br>开发示例|说明|
| -------- | -------- |
|[add](./cj-asset-add.md)|新增一条关键资产。|
|[remove](./cj-asset-remove.md)|删除符合条件的一条或多条关键资产。|
|[update](./cj-asset-update.md)|更新符合条件的一条关键资产。|
|[preQuery](./cj-asset-query-auth.md)|查询的预处理，用于需要用户认证的关键资产。在用户认证成功后，应当随后调用[query](../../../API_Reference/source_zh_cn/apis/AssetStoreKit/cj-apis-asset_store.md#func-queryarrayassetparam)、[postQuery](../../../API_Reference/source_zh_cn/apis/AssetStoreKit/cj-apis-asset_store.md#func-postqueryarrayassetparam)。|
|若查询需要用户认证的关键资产: [query](./cj-asset-query-auth.md)。<br>若查询不需要用户认证的关键资产: [query](./cj-asset-query.md)。|查询一条或多条符合条件的关键资产。若查询需要用户认证的关键资产，则需要在本函数前调用[preQuery](../../../API_Reference/source_zh_cn/apis/AssetStoreKit/cj-apis-asset_store.md#func-prequeryarrayassetparam)，在本函数后调用[postQuery](../../../API_Reference/source_zh_cn/apis/AssetStoreKit/cj-apis-asset_store.md#func-postqueryarrayassetparam)。|
| [postQuery](./cj-asset-query-auth.md)|查询的后置处理，用于需要用户认证的关键资产。需与[preQuery](../../../API_Reference/source_zh_cn/apis/AssetStoreKit/cj-apis-asset_store.md#func-prequeryarrayassetparam)函数成对出现。|
