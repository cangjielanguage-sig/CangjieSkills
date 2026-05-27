# 使用AVMetadataExtractor提取音视频元数据信息（仓颉）

使用[AVMetadataExtractor](./cj-media-kit-intro.md#avmetadataextractor)可以实现从原始媒体资源中获取元数据，本开发指导将以获取一个音频资源的元数据作为示例，向开发者讲解AVMetadataExtractor元数据相关功能。视频资源的元数据获取流程与音频类似，由于视频没有专辑封面，所以无法获取视频资源的专辑封面。

获取音频资源的元数据的全流程包含：创建AVMetadataExtractor，设置资源，获取元数据，获取专辑封面，销毁资源。

## 开发步骤及注意事项

详细的API说明请参见[AVMetadataExtractor API参考](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#class-avmetadataextractor)。

1. 使用createAVMetadataExtractor()创建实例。

2. 设置资源：用户可以根据需要选择设置属性fdSrc（表示文件描述符）, 或者设置属性dataSrc（表示dataSource描述符）。

   > **说明：**
   >
   > 开发者需根据实际情况，确认资源有效性并设置（只能设置其中一种）：
   >
   > - 如果设置fdSrc，可以使用ResourceManager.getRawFd打开HAP资源文件描述符，使用方法请参见[ResourceManager API参考](../../../API_Reference/source_zh_cn/apis/LocalizationKit/cj-apis-resource_manager.md#func-getrawfdstring)。也可以通过应用沙箱路径访问对应资源（必须确保资源可用），请参见[获取应用文件路径](../../application-models/cj-application-context-stage.md#获取应用文件路径)。应用沙箱的介绍及如何向应用沙箱推送文件，请参见[文件管理](../../file-management/cj-app-sandbox-directory.md)。
   >
   > - 如果设置dataSrc，必须正确设置dataSrc中的callback属性，确保callback被调用时能正确读取到对应资源，使用应用沙箱路径访问对应资源，请参见[获取应用文件路径](../../application-models/cj-application-context-stage.md#获取应用文件路径)。应用沙箱的介绍及如何向应用沙箱推送文件，请参见[文件管理](../../file-management/cj-app-sandbox-directory.md)。
   >
   > - 不同AVMetadataExtractor或者[AVImageGenerator](../../../API_Reference/source_zh_cn/apis/MediaKit/cj-apis-multimedia_media.md#class-avimagegenerator)实例，如果需要操作同一资源，需要多次打开文件描述符，不要共用同一文件描述符。

3. 获取元数据：调用fetchMetadata()，可以获取到一个AVMetadata对象，通过访问该对象的各个属性，可以获取到元数据。

4. （可选）获取专辑封面：调用fetchAlbumCover()，可以获取到专辑封面。

5. 释放资源：调用release()销毁实例，释放资源。