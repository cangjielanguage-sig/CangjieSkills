# 元能力子系统错误码

> **说明：**
>
> 以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](cj-errorcode-universal.md)。

## 16000001 指定的Ability名称不存在

**错误信息**

The specified ability does not exist.

**错误描述**

当指定的Ability名称不存在时，方法将返回该错误码。

**可能原因**

所查询的Ability不存在。

**处理步骤**

1. 检查want中的bundleName、moduleName和abilityName是否正确。
2. 检查传入want中bundleName对应的应用是否安装。可使用如下命令查询已安装的应用列表，若bundleName不在查询结果中，说明应用未安装成功。

    ``` text
    hdc shell bm dump -a
    ```

3. 多hap应用需确认ability所属的hap是否已被安装。可使用如下命令查询应用的包信息，若安装的应用中没有对应的hap和ability，说明ability所属的hap未被安装。

    ``` text
    hdc shell bm dump -n 包名
    ```

## 16000002 接口调用Ability类型错误

**错误信息**

Incorrect ability type.

**错误描述**

当接口调用Ability类型错误时，方法将返回该错误码。

**可能原因**

接口调用所在的Ability类型不支持该接口调用。

**处理步骤**

1. 检查want中的bundleName、moduleName和abilityName是否正确。
2. 根据Ability类型调用不同接口。

## 16000003 指定的ID不存在

**错误信息**

The specified ID does not exist.

**错误描述**

当指定的ID不存在时，方法将返回该错误码。

**可能原因**

操作的目标ID不存在。

**处理步骤**

确认操作的ID是否存在。

## 16000004 可见性校验失败

**错误信息**

Failed to start the invisible ability.

**错误描述**

当可见性校验失败时，方法将返回该错误码。

**可能原因**

应用可见性校验失败。

**处理步骤**

1. Stage模型下，拉起应用时抛出16000004异常，表示被拉应用调用失败，需要检查被拉应用module.json5的Ability字段的exported配置是否为true。该配置字段为true，表示可以被其他应用调用；该配置字段为false，表示不可以被其他应用调用。
2. 若应用需要拉起exported为false的ability，请申请ohos.permission.START_INVISIBLE_ABILITY权限（该权限仅系统应用可申请）。

## 16000005 指定的进程权限校验失败

**错误信息**

The specified process does not have the permission.

**错误描述**

当指定的进程权限校验失败时，方法将返回该错误码。

**可能原因**

指定的进程权限校验失败。

**处理步骤**

确认指定进程的权限是否正确。

## 16000006 不允许跨用户操作

**错误信息**

Cross-user operations are not allowed.

**错误描述**

当应用跨用户操作时，方法将返回该错误码。

**可能原因**

应用进行了跨用户操作。

**处理步骤**

确认是否进行了跨用户操作。

## 16000007 服务繁忙

**错误信息**

Service busy. There are concurrent tasks. Try again later.

**错误描述**

当服务繁忙时，方法将返回该错误码。

**可能原因**

服务繁忙。

**处理步骤**

服务繁忙，请稍后重试。

## 16000008 众测应用到期

**错误信息**

The crowdtesting application expires.

**错误描述**

当众测应用到期时，方法将返回该错误码。

**可能原因**

众测应用到期，无法打开。

**处理步骤**

请检查应用是否众测到期，已过有效期的众测应用无法启动。

## 16000009 wukong模式，不允许启动/停止ability

**错误信息**

An ability cannot be started or stopped in Wukong mode.

**错误描述**

当wukong模式下，启动/停止ability时，方法将返回该错误码。

**可能原因**

wukong模式，不允许启动/停止ability。

**处理步骤**

退出wukong模式后，再尝试启动/停止ability。请勿在wukong模式下启动/停止Ability。

## 16000010 不允许带迁移flag

**错误信息**

The call with the continuation flag is forbidden.

**错误描述**

当调用携带迁移flag时，方法将返回该错误码。

**可能原因**

当前调用不允许携带迁移flag。

**处理步骤**

请检查是否携带迁移flag。