### func set(String, String)

```cangjie
public func set(member: String, value: String): Unit
```

**功能：** 设置PhotoAsset成员参数。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|member|String|是|-|成员参数名称例如：[PhotoKeys](#enum-photokeys).TITLE。字符串长度为1~255。|
|value|String|是|-|设置成员参数名称，只能修改[PhotoKeys](#enum-photokeys).TITLE的值。title的参数规格为：<br>- 不应包含扩展名。<br>- 文件名字符串长度为1~255（资产文件名为标题+扩展名）。<br>- 不允许出现的非法英文字符，包括：. \ / : * ? " ' ` < > \| { } [ ] |

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[文件管理错误码](../CoreFileKit/cj-errorcode-filemanagement.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 13900020 | Invalid argument. |
  | 14000014 | The provided member must be a property name of PhotoKey. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaLibraryKit.*
import kit.ArkData.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let phAccessHelper = getPhotoAccessHelper(ctx)
    let predicates = DataSharePredicates()
    let fetchColumns = [PhotoKeys.Title.toString()]
    let fetchOptions: FetchOptions = FetchOptions(fetchColumns, predicates)
    let fetchResult = phAccessHelper.getAssets(fetchOptions)
    let firstPhotoAsset = fetchResult.getFirstObject()
    let newTitle = "NEW_TITLE" // 新标题，实际使用按需取名
    firstPhotoAsset.set('title', newTitle)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```