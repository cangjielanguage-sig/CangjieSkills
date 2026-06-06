## 如何通过文件后缀获取对应的MIMEType列表

下面以通过“.mp3”文件后缀获取对应的MIMEType列表为例，说明如何通过文件后缀获取对应的MIMEType列表。

1. 导入uniformTypeDescriptor模块。
2. 可根据 “.mp3” 文件后缀查询对应UTD数据类型。
3. 根据UTD数据类型查询对应的MIMEType列表。

```cangjie
// 1. 导入模块
import kit.ArkData.*
import kit.UIKit.BusinessException

try {
    // 2. 可根据 “.mp3” 文件后缀查询对应UTD数据类型
    let fileExtention = '.mp3'
    let typeId = getUniformDataTypeByFilenameExtension(fileExtention)
    // 3. 根据UTD数据类型查询对应的MIMEType列表
    let typeObj = getTypeDescriptor(typeId)
    let mimeTypes = typeObj.mimeTypes
    AppLog.info('mimeTypes: ${mimeTypes}')
} catch (e: BusinessException) {
    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
}
```

## 如何通过MIMEType获取对应的后缀列表

下面以通过“audio/mp3”MIMEType获取对应文件后缀列表为例，说明如何通过MIMEType获取对应的后缀列表。

1. 导入uniformTypeDescriptor模块。
2. 可根据 “audio/mp3” MIMEType查询对应UTD数据类型。
3. 根据UTD数据类型查询对应的MIMEType列表。

```cangjie
// 1. 导入模块
import kit.ArkData.*
import kit.UIKit.BusinessException

try {
    // 2. 可根据 “audio/mp3” MIMEType查询对应UTD数据类型
    let mineType = 'audio/mp3'
    let typeId = getUniformDataTypeByMIMEType(mineType)
    // 3. 根据UTD数据类型查询对应的MIMEType列表
    let typeObj = getTypeDescriptor(typeId)
    let filenameExtensions = typeObj.filenameExtensions
    AppLog.info('filenameExtensions: ${filenameExtensions}')
} catch (e: BusinessException) {
    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
}
```