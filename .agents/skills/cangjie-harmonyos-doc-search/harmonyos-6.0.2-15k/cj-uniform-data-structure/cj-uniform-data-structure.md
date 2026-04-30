# 标准化数据结构

## 场景介绍

针对[UTD标准化数据类型](../../API_Reference/source_zh_cn/apis/ArkData/cj-apis-uniformTypeDescriptor.md#enum-uniformdatatype)中的部分常见类型，为了方便业务使用，仓颉编程语言按照不同的数据类型提供标准化数据结构，例如系统定义的桌面图标类型（对应的标准化数据类型标识为`openharmony.app-item`），明确定义了该数据结构对应的相关描述信息。

某些业务场景下应用可以直接使用我们具体定义的UTD标准化数据结构，例如跨应用拖拽场景。拖出方应用可以按照标准化数据结构将拖拽数据写入[拖拽事件](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-event-drag.md#class-dragevent)，拖入方应用从拖拽事件中读取拖拽数据并按照标准化数据结构进行数据的解析。这使得不同应用间的数据交互遵从相同的标准定义，有效减少了跨应用数据交互的开发工作量。

## 开发步骤

以使用标准化数据结构定义数据内容（包含纯文本的两条数据记录）为例，提供基本的开发步骤。

```cangjie
import kit.ArkData.*

// 1. 创建纯文本数据类型记录
let plainTextDataType = UniformDataType.PLAIN_TEXT.get()
let plainTextValue = UnifiedDataChannelValueType.STRING("This is plainText textContent example")
let plainTextRecord = UnifiedRecord(plainTextDataType, plainTextValue)
// 2. 创建超链接数据记录
let hyperlinkDataType = UniformDataType.HYPERLINK.get()
let hyperlinkValue = UnifiedDataChannelValueType.STRING("www.XXX.com")
let hyperlinkRecord = UnifiedRecord(hyperlinkDataType, hyperlinkValue)
// 3. 创建一个统一数据对象实例
let unifiedData = UnifiedData()
// 4. 添加plainText数据记录
unifiedData.addRecord(plainTextRecord)
// 5. 添加hyperlink数据记录
unifiedData.addRecord(hyperlinkRecord)
// 6. 记录添加完成后，可获取当前UnifiedData对象内的所有数据记录。
let records = unifiedData.getRecords()
// 7. 遍历每条记录，判断该记录的数据类型，得到原数据记录。
for (i in (0..records.size)) {
    let recordType = records[i].getType()
    AppLog.info("Show records type: ${recordType}")
    let recordValue = records[i].getValue()
    let message: String = match (recordValue) {
        case INTEGER32(v) => v.toString()
        case INTEGER64(v) => v.toString()
        case DOUBLE(v) => v.toString()
        case BOOLEAN(v) => v.toString()
        case STRING(v) => v
        case ARRAYBUFFER(v) => v.toString()
        case PIXELMAP(v) => "PIXELMAP"
        case _ => throw IllegalArgumentException("The type is not supporte.")
    }
    AppLog.info("Show records message: ${message}")
}
```
