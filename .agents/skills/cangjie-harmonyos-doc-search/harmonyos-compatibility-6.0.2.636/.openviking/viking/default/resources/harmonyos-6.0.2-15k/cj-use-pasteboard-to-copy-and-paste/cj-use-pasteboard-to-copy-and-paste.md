# 使用剪贴板进行复制粘贴

## 场景介绍

[剪贴板](../../../API_Reference/source_zh_cn/apis/BasicServicesKit/cj-apis-pasteboard.md)为开发者提供数据的复制粘贴能力。

当需要使用复制粘贴等功能时，例如：复制文字内容到备忘录中粘贴，复制图库照片到文件管理粘贴，就可以通过剪贴板来完成。

## 约束限制

- 剪贴板内容大小&lt;128MB。
- 为保证剪贴板数据的准确性，同一时间只能支持一个复制操作。
- 系统为提升用户隐私安全保护能力，剪贴板读取接口增加[权限管控](./cj-get-pastedata-permission-guidelines.md)。

## 使用基础数据类型进行复制粘贴

剪贴板支持使用基础数据类型进行复制粘贴，当前支持的基础数据类型有文本、HTML、URI、Want、PixelMap。ArkTS接口与NDK接口支持数据类型不完全一致，使用时须匹配接口支持类型。

新开发的应用建议使用本方案实现复制粘贴功能。

### 接口说明

详细接口见[接口文档](../../../API_Reference/source_zh_cn/apis/BasicServicesKit/cj-apis-pasteboard.md#func-getdata)。

使用剪贴板getData接口获取到uri类型数据之后，请使用文件管理的[fs.copy](../../../API_Reference/source_zh_cn/apis/CoreFileKit/cj-apis-file_fs.md#static-func-copystring-string-copyoptions)接口获取文件。

| 名称 | 说明                                         |
| -------- |-----------------------------------------|
| setData(data: PasteData): Unit | 将数据写入系统剪贴板。|
| getData(): PasteData | 读取系统剪贴板内容。|

### 示例代码

<!-- run -->

```cangjie
import kit.BasicServicesKit.*
import kit.AbilityKit.*
import ohos.hilog.Hilog

@Entry
@Component
class EntryView {
    func build() {
        Row {
            Column {
                Button("test").onClick {
                    =>
                    // 获取系统剪贴板对象
                    let text = "hello"
                    // 创建一条纯文本类型的剪贴板内容对象
                    let pasteData = createData("text/plain", text)
                    // 将数据写入系统剪贴板
                    let systemPasteboard = getSystemPasteboard()
                    systemPasteboard.setData(pasteData)
                    //从系统剪贴板中读取数据
                    let data = systemPasteboard.getData()
                    // 从剪贴板数据中获取条目数量
                    let recordCount = Int32(data.getRecordCount())
                    // 从剪贴板数据中获取对应条目信息
                    for (i in 0..recordCount) {
                        let record = data.getRecord(i).toPlainText()
                        AppLog.info("Get data success, record: ${record}")
                    }
                }
            }.width(100.percent)
        }.height(100.percent)
    }
}
```
