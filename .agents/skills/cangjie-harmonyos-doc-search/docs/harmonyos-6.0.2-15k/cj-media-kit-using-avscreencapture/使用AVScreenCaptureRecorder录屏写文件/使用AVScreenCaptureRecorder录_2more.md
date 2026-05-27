# 使用AVScreenCaptureRecorder录屏写文件

屏幕录制主要为主屏幕录屏功能。

开发者可以调用录屏（[AVScreenCaptureRecorder](cj-media-kit-intro.md#avscreencapture)）模块的ArkTs接口，完成屏幕录制，采集设备内、麦克风等的音视频源数据。可以调用录屏模块获取音视频文件，然后通过文件的形式流转到其他模块进行播放或处理，达成文件形式分享屏幕内容的场景。

录屏模块和窗口（Window）、图形（Graphic）等模块协同完成整个视频采集的流程。

使用AVScreenCaptureRecorder录制屏幕涉及到AVScreenCaptureRecorder实例的创建、音视频采集参数的配置、采集的开始与停止、资源的释放等。

开始屏幕录制时正在通话中或者屏幕录制过程中来电，录屏将自动停止。因通话中断的录屏会上报SCREENCAPTURE_STATE_STOPPED_BY_CALL状态。

本开发指导将以完成一次屏幕数据录制的过程为例，向开发者讲解如何使用AVScreenCaptureRecorder进行屏幕录制，详细的API声明请参见[AVScreenCaptureRecoder API参考](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#class-avscreencapturerecorder)。

当前暂不支持配置采集麦克风音频数据。

## 申请权限

在开发此功能前，开发者应根据实际需求申请相关权限：

- 当需要使用麦克风时，需要申请**ohos.permission.MICROPHONE**麦克风权限。申请方式请参考：[向用户申请授权](../../security/AccessToken/cj-request-user-authorization.md)。
- 当需要读取图片或视频文件时，请优先使用媒体库[Picker选择媒体资源](../../media/medialibrary/cj-photoAccessHelper-photoviewpicker.md)。
- 当需要保存图片或视频文件时，请优先使用[安全控件保存媒体资源](../../media/medialibrary/cj-photoAccessHelper-savebutton.md)。

> **说明：**
>
> 仅应用需要克隆、备份或同步用户公共目录的图片、视频类文件时，可申请ohos.permission.READ_IMAGEVIDEO、ohos.permission.WRITE_IMAGEVIDEO权限来读写音频文件，申请方式请参见[申请受控权限](../../security/AccessToken/cj-declare-permissions-in-acl.md)。