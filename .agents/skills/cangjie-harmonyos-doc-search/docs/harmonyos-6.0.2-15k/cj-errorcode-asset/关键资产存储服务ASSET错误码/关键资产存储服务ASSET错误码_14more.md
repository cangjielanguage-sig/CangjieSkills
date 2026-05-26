# 关键资产存储服务(ASSET)错误码

> **说明：**
>
> 以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](./cj-errorcode-universal.md)。

## 24000001 关键资产服务不可用

**错误信息**

The ASSET service is unavailable.

**可能原因**

系统异常导致关键资产服务不可用。

**处理步骤**

重新发起关键资产处理请求。

## 24000002 未找到关键资产

**错误信息**

The asset is not found.

**可能原因**

1. 关键资产从未写入过。
2. 关键资产已经删除。

**处理步骤**

1. 根据别名确认该关键资产是否已经写入过，或已经删除。
2. 重新写入关键资产，再访问该关键资产。

## 24000003 关键资产已存在

**错误信息**

The asset already exists.

**可能原因**

已存在同别名（AssetTag.ALIAS相同）的关键资产。

**处理步骤**

请先确认写入同别名的关键资产是否符合预期，如果不符合需排查别名是否错误，如果符合则可通过以下任意一种方式处理：

1. 先调用[remove](../apis/AssetStoreKit/cj-apis-asset_store.md#func-removearrayassetparam)
2. 删除同别名的关键资产，再调用[add](../apis/AssetStoreKit/cj-apis-asset_store.md#func-addarrayassetparam)重新写入。
3. 调用[add](../apis/AssetStoreKit/cj-apis-asset_store.md#func-addarrayassetparam)时，指定参数AssetTag.CONFLICT_RESOLUTION的值为AssetConflictResolution.OVERWRITE

## 24000004 拒绝访问关键资产

**错误信息**

Access to the asset is denied.

**可能原因**

1. 在访问需要用户认证的关键资产前，用户认证失败。

2. 挑战值与授权令牌不匹配。

**处理步骤**

1. 用户在访问需要用户认证的关键资产前，先进行用户认证。

2. 传递匹配的挑战值与授权令牌。

## 24000005 锁屏状态不匹配

**错误信息**

The screen lock status does not match.

**可能原因**

1. 在设备处于未设置锁屏密码的状态下，访问仅设置密码才允许访问的关键资产。
2. 在设备未完成首次解锁的状态下，访问仅首次解锁后才允许访问的关键资产。
3. 在设备未处于解锁状态下，访问仅解锁时才允许访问的关键资产。

**处理步骤**

设置锁屏密码或解锁后，再访问关键资产。

## 24000006 系统内存不足

**错误信息**

Insufficient memory.

**可能原因**

系统内存不足。

**处理步骤**

关闭已打开的其他应用，重新发起处理请求。

## 24000007 关键资产损坏

**错误信息**

The asset is corrupted.

**可能原因**

因设备掉电或存储系统异常导致的关键资产文件损坏。

**处理步骤**

恢复出厂设置。

## 24000008 数据库操作失败

**错误信息**

The database operation failed.

**可能原因**

1. 用户尚未调用过[add](../apis/AssetStoreKit/cj-apis-asset_store.md#func-addarrayassetparam)接口，进行asset数据库的创建，此时数据库还没创建出来，直接查询，会有该报错。
2. 数据库访问异常。

**处理步骤**

1. 用户先调用[add](../apis/AssetStoreKit/cj-apis-asset_store.md#func-addarrayassetparam)接口，将asset数据库创建出来之后再进行查询。
2. 查看错误信息，排查数据库异常原因。

## 24000009 算法库操作失败

**错误信息**

The cryptography operation failed.

**可能原因**

密码算法操作失败。

**处理步骤**

查看错误信息，排查算法库异常原因。

## 24000010 进程通信错误

**错误信息**

IPC failed.

**可能原因**

进程通信错误。

**处理步骤**

查看错误信息，排查IPC通信异常原因。

## 24000011 包管理服务异常

**错误信息**

Calling the Bundle Manager service failed.

**可能原因**

包管理服务异常。

**处理步骤**

查看错误信息，排查包管理服务异常原因。

## 24000012 账号系统异常

**错误信息**

Calling the OS Account service failed.

**可能原因**

账号系统异常。

**处理步骤**

查看错误信息，排查账号系统异常原因。

## 24000013 访问控制服务异常

**错误信息**

Calling the Access Token service failed.

**可能原因**

访问控制服务异常。

**处理步骤**

查看错误信息，排查访问控制服务异常原因。