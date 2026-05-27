### 媒体文件uri介绍

**媒体文件uri的格式类型为：**

- 图片uri格式：'file://media/Photo/\<id>/IMG_datetime_0001/displayName.jpg'

- 视频uri格式：'file://media/Photo/\<id>/VID_datetime_0001/displayName.mp4'

- 音频uri格式：'file://media/Audio/\<id>/AUD_datetime_0001/displayName.mp3'

**其中各个字段表示的含义为：**

| uri字段          | 说明        |
| ------------- | ------------------- |
| 'file://media' | 表示这个uri是媒体文件。 |
| 'Photo' | 表示这个uri是媒体文件中的图片或者视频类文件。 |
| 'Audio' | 表示这个uri是媒体文件中的音频类文件。 |
| '\<id>' | 表示在数据库中多个表中处理后的值，并不是指表中的file_id列，注意请不要使用此id去数据库中查询具体文件。 |
| 'IMG_datetime_0001' | 表示图片文件在用户文件系统中存储的文件名去掉后缀剩下的部分。 |
| 'VID_datetime_0001' | 表示视频文件在用户文件系统中存储的文件名去掉后缀剩下的部分。 |
| 'AUD_datetime_0001' | 表示音频文件在用户文件系统中存储的文件名去掉后缀剩下的部分。 |

### 媒体文件uri获取方式

1. 通过[PhotoAccessHelper的PhotoViewPicker](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#class-photoviewpicker)选择媒体文件，返回选择的媒体文件文件的uri。

2. 通过[photoAccessHelper模块](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md)>中的[getAssets](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-getassetsfetchoptions)或[createAsset](../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#static-func-createassetrequestabilitycontext-phototype-string-createoptions)接口获取媒体文件对应文件的uri。