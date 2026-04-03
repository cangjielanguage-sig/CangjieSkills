# 使用AVRecorder录制音频

使用[AVRecorder](./cj-media-kit-intro.md#avrecorder)可以实现音频录制功能，本开发指导将以“开始录制-暂停录制-恢复录制-停止录制”的一次流程为示例，向开发者讲解AVRecorder音频录制相关功能。

在进行应用开发的过程中，开发者可以通过AVRecorder的state属性，主动获取当前状态或使用on("stateChange")方法监听状态变化。开发过程中应该严格遵循状态机要求，例如只能在started状态下调用pause()接口，只能在paused状态下调用resume()接口。录制状态变化示意图如下所示。

![Recording status change](./figures/recording-status-change.png)

状态的详细说明请参见[AVRecorderState](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#enum-avrecorderstate)。

## 申请权限

在开发此功能前，开发者应根据实际需求申请相关权限：

- 当需要使用麦克风时，需要申请**ohos.permission.MICROPHONE**麦克风权限。申请方式请参考：[向用户申请授权](../../security/AccessToken/cj-request-user-authorization.md)。
- 当需要读取和保存音频文件时，请优先使用[AudioViewPicker音频选择器对象](../../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_picker.md#class-audioviewpicker)。

> **说明：**
>
> 仅应用需要克隆、备份或同步用户公共目录的音频类文件时，可申请ohos.permission.READ_AUDIO、ohos.permission.WRITE_AUDIO权限来读写音频文件，申请方式请参见[申请受控权限](../../security/AccessToken/cj-declare-permissions-in-acl.md)。