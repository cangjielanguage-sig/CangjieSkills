## enum ConfigData

```cangjie
public enum ConfigData {
    | StringValue(String)
    | FormItems(Array<FormItem>)
    | ...
}
```

**功能：** 上传/下载任务的data配置枚举类型。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### FormItems(Array\<FormItem>)

```cangjie
FormItems(Array<FormItem>)
```

**功能：** 表示上传时，data是表单项数组Array&lt;FormItem&gt;。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22

### StringValue(String)

```cangjie
StringValue(String)
```

**功能：** 表示下载时，data为字符串类型，通常使用json(object将被转换为json文本)。

**系统能力：** SystemCapability.Request.FileTransferAgent

**起始版本：** 22