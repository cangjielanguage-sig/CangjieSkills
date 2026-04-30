## 16000076 指定的APP_INSTANCE_KEY不存在

**错误信息**

The APP_INSTANCE_KEY is invalid.

**错误描述**

指定的APP_INSTANCE_KEY不存在时，返回该错误码。

**可能原因**

应用的实例中不存在该APP_INSTANCE_KEY指定的实例。

**处理步骤**

确保传入的APP_INSTANCE_KEY是一个有效值。

## 16000077 应用的实例数量已达到上限

**错误信息**

The number of app instances reaches the limit.

**错误描述**

当应用的实例数量达到上限后，继续创建应用实例，返回该错误码。

**可能原因**

创建应用实例前未判断应用实例数量是否已达到应用自己设置的上限值。

**处理步骤**

调整设置的应用实例上限，或者删除已有应用实例后，才能继续创建新的应用实例。

## 16000078 不支持应用多实例

**错误信息**

The multi-instance is not supported.

**错误描述**

应用不支持多实例。

**可能原因**

1. 目标应用未配置多实例。
2. 当前设备类型不支持多实例。

**处理步骤**

1. 对目标应用配置多实例。
2. 在2in1设备上调用该方法。

## 16000079 不支持指定APP_INSTANCE_KEY

**错误信息**

The APP_INSTANCE_KEY cannot be specified.

**错误描述**

APP_INSTANCE_KEY和CREATE_APP_INSTANCE_KEY不支持同时指定。当指定CREATE_APP_INSTANCE_KEY的同时指定APP_INSTANCE_KEY，返回该错误码。

**可能原因**

参数传入过多。

**处理步骤**

参数APP_INSTANCE_KEY和CREATE_APP_INSTANCE_KEY只支持二选一。

## 16000080 不支持创建新实例

**错误信息**

Creating an instance is not supported.

**错误描述**

只允许应用使用CREATE_APP_INSTANCE_KEY创建自己的实例，不允许应用间启动时为其他应用创建实例。否则，返回该错误码。

**可能原因**

参数使用场景有误。

**处理步骤**

删除参数CREATE_APP_INSTANCE_KEY。

## 16000082 单实例模式下的UIAbility未完成启动

**错误信息**

The UIAbility is being started.

**错误描述**

如果UIAbility启动模式为“singleton”，在UIAbility启动完成之前不能再次调用启动接口，否则将返回该错误码。

**可能原因**

该UIAbility为singleton模式，正在启动过程中。

**处理步骤**

确保该UIAbility启动完成，再执行新的启动任务。

## 16000100 监听Ability生命周期变化的AbilityMonitor方法执行失败

**错误信息**

- Calling AddAbilityMonitor failed.

- Calling AddAbilityMonitorSync failed.

- Calling RemoveAbilityMonitor failed.

- Calling RemoveAbilityMonitorSync failed.

- Calling WaitAbilityMonitor failed.

- Calling GetCurrentTopAbility failed.

- Calling DoAbilityForeground failed.

- Calling DoAbilityBackground failed.

- Calling FinishTest failed.

- Calling AddAbilityStageMonitor failed.

- Calling AddAbilityStageMonitorSync failed.

- Calling RemoveAbilityStageMonitor failed.

- Calling RemoveAbilityStageMonitorSync failed.

- Calling WaitAbilityStageMonitor failed.

**错误描述**

当监听指定Ability的生命周期变化的AbilityMonitor方法执行失败时，返回该错误码。

**可能原因**

创建AbilityDelegatorRegistry实例执行失败。

**处理步骤**

检查是否成功创建了AbilityDelegatorRegistry实例。

## 16000101 执行shell命令失败

**错误信息**

Failed to run the shell command.

**错误描述**

当命令不是有效的shell命令时，方法将返回该错误码。

**可能原因**

命令不是有效的shell命令。

**处理步骤**

检查命令是否为有效的shell命令。

## 16000151 无效wantAgent对象

**错误信息**

Invalid wantAgent object.

**错误描述**

当传入接口的wantAgent对象无效时，方法将返回该错误码。

**可能原因**

传入接口的wantAgent对象无效。

**处理步骤**

检查传入接口的wantAgent对象。

## 16000152 未找到wantAgent对象

**错误信息**

The wantAgent object does not exist.

**错误描述**

当传入接口的wantAgent对象不存在时，方法将返回该错误码。

**可能原因**

传入接口的wantAgent对象不存在。

**处理步骤**

检查传入接口的wantAgent对象是否合法。