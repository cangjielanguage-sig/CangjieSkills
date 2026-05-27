## 场景介绍

当应用后台运行时，可能由于系统资源管控等原因导致应用关闭、进程退出，应用直接退出可能会导致用户数据丢失。如果应用在[UIAbilityContext](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiabilitycontext)中启用了[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability )备份恢复功能，并对临时数据进行保存，则可以在应用退出后的下一次启动时恢复先前的状态和数据（包括应用的页面栈以及[onSaveState](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onsavestatestatetype-string)接口中保存的数据），从而保证用户体验的连贯性。

> **说明：**
>
> 应用正常关闭时，不会触发[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)备份流程。应用正常启动（例如通过startAbility接口启动或点击图标启动），不触发[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)恢复流程。

## 运行机制

- [UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)数据备份：在应用的[onBackground](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onbackground)生命周期后，系统自动调用[onSaveState](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onsavestatestatetype-string)进行备份。
- [UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)数据恢复：恢复的[Want](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)数据可以在应用的[onCreate](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-oncreate)生命周期中获取，页面栈数据在应用的[onWindowStageCreate](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#let-onwindowstagecreate)生命周期中恢复。

## 约束限制

- [UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)备份恢复支持多实例，备份数据保存7天，以文件的形式存储在应用的[沙箱路径](../file-management/cj-app-sandbox-directory.md)中。
- 备份数据以[WantParams](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)形式存储，由于序列化大小限制，支持的最大数据量为200KB。
- 重启设备不支持还原备份。
- [UIExtensionAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiextensionability)不支持备份恢复。