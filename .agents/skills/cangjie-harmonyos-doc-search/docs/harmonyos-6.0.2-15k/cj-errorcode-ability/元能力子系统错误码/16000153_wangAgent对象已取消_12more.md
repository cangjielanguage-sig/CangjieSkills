## 16000153 wangAgent对象已取消

**错误信息**

The wantAgent object has been canceled.

**错误描述**

当传入接口的wangAgent对象已取消时，方法将返回该错误码。

**可能原因**

传入接口的触发的wantAgent已取消。

**处理步骤**

检查触发的wantAgent对象是否已取消。

## 16100001 指定Uri的Ability不存在

**错误信息**

The ability with the specified URI does not exist.

**错误描述**

当指定Uri的Ability不存在时，方法将返回该错误码。

**可能原因**

所查询的Ability不存在。

**处理步骤**

确认查询的Ability是否存在。

## 16100002 接口调用Ability类型错误

**错误信息**

Incorrect ability type.

**错误描述**

当接口调用Ability类型错误时，方法将返回该错误码。

**可能原因**

接口调用所在的Ability类型不支持该接口调用。

**处理步骤**

1. 检查包名对应的Ability是否正确。
2. 根据Ability类型调用不同接口。

## 16200001 通用组件客户端(Caller)已回收

**错误信息**

The caller has been released.

**错误描述**

当通用组件客户端(Caller)已回收时，方法将返回该错误码。

**可能原因**

通用组件客户端(Caller)已回收。

**处理步骤**

1. 请重新注册有效通用组件客户端调用接口。
2. 检查调用context.startAbility时，context对应的ability是否还在运行。若该ability已被析构，会抛出该错误码。
3. 若存在连续调用startAbility和terminateSelf的情况，请确认收到startAbility成功或失败的回调后，再调用terminateSelf。

## 16200002 通用组件服务端(Callee)无效

**错误信息**

The callee does not exist.

**错误描述**

当通用组件服务端(Callee)无效时，方法将返回该错误码。

**可能原因**

通用组件服务端(Callee)不存在。

**处理步骤**

请检查通用组件服务端是否存在。

## 16200003 回收失败

**错误信息**

Release error. The caller does not call any callee.

**错误描述**

当回收失败时，方法将返回该错误码。

**可能原因**

通用组件客户端(Caller)对象未注册通用组件服务端(Callee)。

**处理步骤**

请检查是否已注册通用组件服务端。

## 16200004 方法已注册

**错误信息**

The method has been registered.

**错误描述**

当方法已注册时，方法将返回该错误码。

**可能原因**

方法已在通用组件服务端注册过。

**处理步骤**

请检查是否已注册该方法。

## 16200005 方法未注册

**错误信息**

The method has not been registered.

**错误描述**

当方法未注册时，方法将返回该错误码。

**可能原因**

方法未在通用组件服务端注册。

**处理步骤**

请检查是否未注册该方法。

## 16200006 没有权限设置常驻进程使能状态

**错误信息**

The caller application can only set the resident status of the configured process.

**错误描述**

当调用者没有权限设置常驻进程使能状态时返回。

**可能原因**

调用者没有常驻进程使能配置权限。

**处理步骤**

接口调用时从数据库查询调用者的常驻进程使能配置权限。

## 16300001 指定的任务不存在

**错误信息**

Mission not found.

**错误描述**

当指定的任务不存在时，方法将返回该错误码。

**可能原因**

操作的目标任务不存在。

**处理步骤**

确认操作的任务是否存在。

## 16300002 指定的任务监听器不存在

**错误信息**

The specified mission listener does not exist.

**错误描述**

当指定的任务监听器不存在时，方法将返回该错误码。

**可能原因**

操作的目标任务监听器不存在。

**处理步骤**

确认操作的任务监听器是否存在。

## 16300003 目标应用程序不是自身应用程序

**错误信息**

The target application is not the current application.

**错误描述**

当被拉起的应用程序不是自身应用程序时，方法将返回该错误码。

**可能原因**

被拉起的应用和发起调用的应用不是同一个应用程序。

**处理步骤**

确认被拉起的应用程序是否为自身应用程序。