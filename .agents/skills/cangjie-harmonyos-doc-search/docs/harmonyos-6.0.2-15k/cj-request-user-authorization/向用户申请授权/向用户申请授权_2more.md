# 向用户申请授权

当应用需要访问用户的隐私信息或使用系统能力时，例如获取位置信息、访问日历、使用相机拍摄照片或录制视频等，应该向用户请求授权，这部分权限是user_grant权限。

当应用申请user_grant权限时，需要完成以下步骤：

1. 在配置文件中，声明应用需要请求的权限。

2. 将应用中需要申请权限的目标对象与对应目标权限进行关联，让用户明确地知道，哪些操作需要用户向应用授予指定的权限。

    以上两步请参见章节[声明权限](./cj-declare-permissions.md)完成。

3. 运行应用时，在用户触发访问操作目标对象时应该调用接口，精准触发动态授权弹框。该接口的内部会检查当前用户是否已经授权应用所需的权限，如果当前用户尚未授予应用所需的权限，该接口会拉起动态授权弹框，向用户请求授权。

4. 检查用户的授权结果，确认用户已授权才可以进行下一步操作。

本章节会介绍如何完成步骤3和4。

## 约束与限制

- user_grant权限授权要基于用户可知可控的原则，需要应用在运行时主动调用系统动态申请权限的接口，系统弹框由用户授权，用户结合应用运行场景的上下文，识别出应用申请相应敏感权限的合理性，从而做出正确的选择。
- 系统不鼓励频繁弹窗打扰用户，如果用户拒绝授权，将无法再次拉起弹窗，需要应用引导用户在系统应用“设置”的界面中手动授予权限。
- 系统权限弹窗不可被遮挡。

  系统权限弹窗不可被其他组件/控件遮挡，弹窗信息需要完整展示，以便用户识别并完成授权动作。

  如果系统权限弹窗与其他组件/控件同时同位置展示，系统权限弹窗将默认覆盖其他组件/控件。

- 每次执行需要目标权限的操作时，应用都必须检查自己是否已经具有该权限。

  如需检查用户是否已向您的应用授予特定权限，可以使用[checkAccessToken()](../../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability_access_ctrl.md#func-checkaccesstokenuint32-permissions)函数，此方法会返回[PERMISSION_GRANTED](../../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability_access_ctrl.md#enum-grantstatus)或[PERMISSION_DENIED](../../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability_access_ctrl.md#enum-grantstatus)。具体示例可参考下文。

- 每次访问受目标权限保护的接口之前，都需要使用[requestPermissionsFromUser()](../../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability_access_ctrl.md#func-requestpermissionsfromuserstagecontext-arraypermissions-asynccallbackaccessctrlpermissionrequestresult)接口请求相应的权限。

  用户可能在动态授予权限后通过系统设置来取消应用的权限，因此不能将之前授予的授权状态持久化。

- 应用在onWindowStageCreate()回调中申请授权时，需要等待异步接口loadContent()/setUIContent()执行结束后或在loadContent()/setUIContent()回调中调用[requestPermissionsFromUser()](../../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability_access_ctrl.md#func-requestpermissionsfromuserstagecontext-arraypermissions-asynccallbackaccessctrlpermissionrequestresult)，否则在Content加载完成前，requestPermissionsFromUser会调用失败。