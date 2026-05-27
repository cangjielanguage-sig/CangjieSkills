# 通过系统相机拍照和录像（仓颉）

应用可调用CameraPicker拍摄照片或录制视频，无需申请相机权限。

CameraPicker的相机交互界面由系统提供，在用户点击拍摄和确认按钮后，调用CameraPicker的应用获取对应的照片或者视频。

应用开发者如果只是需要获取即时拍摄的照片或者视频，则可以使用CameraPicker能力来轻松实现。

由于照片的拍摄和确认都是由用户进行主动确认，因此应用开发者可以不用申请操作相机的相关权限。

## 开发步骤

详细的API说明请参见[CameraPicker API参考](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera_picker.md)。

1. 导入相关接口，导入方法如下。

    ```cangjie
    import kit.CameraKit.*
    import kit.CoreFileKit.*
    import kit.UIKit.*
    import std.time.*
    import ohos.base.*
    ```

2. 配置[PickerProfile](../../../API_Reference/source_zh_cn/apis/CameraKit/cj-apis-multimedia-camera_picker.md#struct-pickerprofile)。

    > **说明：**
    >
    > PickerProfile的saveUri为可选参数，如果未配置该项，拍摄的照片和视频默认存入媒体库中。
    >
    > 如果不想将照片和视频存入媒体库，请自行配置应用沙箱内的文件路径。
    >
    > 应用沙箱内的这个文件必须是一个存在的、可写的文件。这个文件的uri传入picker接口之后，相当于应用给系统相机授权该文件的读写权限。系统相机在拍摄结束之后，会对此文件进行覆盖写入。

    ```cangjie
    let pathDir = context.filesDirectory
    let fileName = DateTime.now().toString()
    let filePath = pathDir + "/${fileName}.tmp"
    FileFs.createRandomAccessFile(filePath, mode: OpenMode.CREATE.mode)

    let uri = FileUri.getUriFromPath(filePath)
    let pickerProfile: PickerProfile = PickerProfile(CameraPosition.CAMERA_POSITION_BACK, saveUri: uri)
    ```

3. 调用picker拍摄接口获取拍摄的结果。

    ```cangjie
    class PickCallBack <: Callback1Argument<PickerResult> {
        var cb: (PickerResult) -> Unit
        init(cb: (PickerResult) -> Unit) {this.cb = cb}
        public open func invoke(result: PickerResult): Unit {
            cb(result)
        }
    }

    pick(context, [PickerMediaType.PHOTO, PickerMediaType.VIDEO], pickerProfile, PickCallBack(cb))
    ```