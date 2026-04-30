## 16000068 Ability已经在运行中

**错误信息**

The ability is already running.

**错误描述**

当目标Ability已经在运行中时，返回该错误码。

**可能原因**

调用startAbility时，指定了processMode和startupVisibility，目标Ability的launchType是singleton或者specified，并且目标Ability正在运行中，则返回该错误码。

**处理步骤**

当目标Ability的launchType是singleton或者specified时，避免通过指定processMode和startupVisibility的方式重复startAbility。

## 16000069 严格模式下不允许该类型Extension启动三方应用

**错误信息**

The extension cannot start the third party application.

**错误描述**

严格模式下，不允许该类型Extension启动三方应用。

**可能原因**

当前Extension处于严格模式，且对应的Extension类型不允许严格模式下启动其他三方应用。

**处理步骤**

1. 查看对应Extension类型严格模式开启条件。
2. 以非严格模式启动当前Extension。

## 16000070 严格模式下不允许该类型Extension启动指定ServiceExtensionAbility

**错误信息**

The extension cannot start the service.

**错误描述**

严格模式下，不允许该类型Extension启动指定ServiceExtensionAbility。

**可能原因**

当前Extension处于严格模式，且对应的Extension类型不允许严格模式下启动指定ServiceExtensionAbility。

**处理步骤**

1. 查看对应Extension类型严格模式开启条件。
2. 以非严格模式启动当前Extension。

## 16000071 不支持应用分身模式

**错误信息**

App clone is not supported.

**错误描述**

当应用不支持分身模式时，返回该错误码。

**可能原因**

在不支持应用分身的应用中调用getCurrentAppCloneIndex时，则返回该错误码。

**处理步骤**

在不支持应用分身的应用中，避免调用getCurrentAppCloneIndex。

<!--Del-->

## 16000072 不支持应用多开

**错误信息**

App clone or multi-instance is not supported.

**错误描述**

当应用不支持多开时，返回该错误码。

**可能原因**

调用getRunningMultiAppInfo查询不支持应用多开的应用多开信息，则返回该错误码。

**处理步骤**

调用getCurrentAppCloneIndex时确保查询的应用支持应用多开。
<!--DelEnd-->

## 16000073 传入的appCloneIndex是一个无效值

**错误信息**

The app clone index is invalid.

**错误描述**

传入一个无效的appCloneIndex，返回该错误码。

**可能原因**

1.调用startAbility时，使用ohos.extra.param.key.appCloneIndex携带的appCloneIndex是一个无效值，则返回该错误码。
<!--Del-->
2.调用isAppRunning是，入参appCloneIndex是一个无效值，则返回该错误码。
<!--DelEnd-->

**处理步骤**

确认appCloneIndex的约束条件是否满足。

## 16000074 返回结果时requestCode对应的调用方不存在

**错误信息**

The caller does not exist.

**错误描述**

通过backTocallerAbilityResult接口向调用方返回结果时，如果根据传入的requestCode无法找到调用方，返回该错误码。

**可能原因**

1. requestCode不是通过want中的CALLER_REQUEST_CODE字段获取的。

2. requestCode对应的调用方已经被销毁或结果已经返回。

**处理步骤**

1. 确认requestCode是否是通过want中的CALLER_REQUEST_CODE获取的。

2. 确认调用方是否被销毁或结果已经返回。

## 16000075 不支持返回结果时拉起调用方

**错误信息**

Not support back to caller.

**错误描述**

不支持通过backToCallerAbilityWithResult接口返回到调用方时，返回该错误码。

**可能原因**

当前应用未进行linkFeature配置或未通过系统审核。

**处理步骤**

1. 确认当前应用已在module.json5文件中配置linkFeature字段。
2. 确认当前应用声明的linkFeature取值正确，linkFeature描述的功能与应用链接对应的实际功能一致，且应用通过系统审核。