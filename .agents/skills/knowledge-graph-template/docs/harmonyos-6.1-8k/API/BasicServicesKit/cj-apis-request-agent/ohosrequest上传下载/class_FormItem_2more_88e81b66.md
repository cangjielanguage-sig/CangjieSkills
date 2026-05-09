## class FormItem

```cangjie
public class FormItem {
    public var name: String
    public var value: FormItemValue

    public init(name: String, value: FormItemValue)
}
```

**功能：** 任务的表单项信息。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var name

```cangjie
public var name: String
```

**功能：** 表单参数名。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### var value

```cangjie
public var value: FormItemValue
```

**功能：** 表单参数值。

**类型：** [FormItemValue](#enum-formitemvalue)

**读写能力：** 可读写

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### init(String, FormItemValue)

```cangjie
public init(name: String, value: FormItemValue)
```

**功能：** 创建FormItem对象。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :----- | :--------- | :--- | :----- | :---------- |
| name   | String | 是   | -      | **命名参数。** 表单参数名。 |
| value  | [FormItemValue](#enum-formitemvalue) | 是   | -      | **命名参数。** 表单参数值。 |

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.BasicServicesKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let formItem = FormItem(
        "exampleField",
        FormItemValue.StringItem("exampleValue")
    )
    Hilog.info(0, "test", "成功创建表单项对象")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## class HttpResponse

```cangjie
public class HttpResponse {
    public let version: String
    public let statusCode: Int32
    public let reason: String
    public let headers: HashMap<String, Array<String>>
}
```

**功能：** 任务响应头的数据结构。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let headers

```cangjie
public let headers: HashMap<String, Array<String>>
```

**功能：** Http响应头部。

**类型：** HashMap\<String,Array\<String>>

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let reason

```cangjie
public let reason: String
```

**功能：** Http响应原因。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let statusCode

```cangjie
public let statusCode: Int32
```

**功能：** Http响应状态码。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### let version

```cangjie
public let version: String
```

**功能：** Http版本。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22