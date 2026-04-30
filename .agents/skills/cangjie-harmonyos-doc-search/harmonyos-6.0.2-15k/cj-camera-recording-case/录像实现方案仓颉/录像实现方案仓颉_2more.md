# 录像实现方案（仓颉）

在开发相机应用时，需要先参考开发准备[申请相关权限](./cj-camera-preparation.md)。

当前示例提供完整的录像流程介绍，方便开发者了解完整的接口调用顺序。

在参考以下示例前，建议开发者查看[相机开发指导](./cj-camera-preparation.md)的具体章节，了解[设备输入](./cj-camera-device-input.md)、[会话管理](./cj-camera-session-management.md)、[录像](./cj-camera-recording.md)等单个流程。

如需要将视频保存到媒体库中请参见[保存媒体库资源](../../../Dev_Guide/media/medialibrary/cj-photoAccessHelper-savebutton.md#保存媒体库资源)。

## 开发流程

在获取到相机支持的输出流能力后，开始创建录像流，开发流程如下。

![Recording Development Process](./figures/recording-development-process.png)