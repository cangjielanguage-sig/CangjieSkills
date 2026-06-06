## class InputAttribute

```cangjie
public class InputAttribute {
    public InputAttribute(
        public let textInputType: TextInputType,
        public let enterKeyType: EnterKeyType
    )
}
```

**功能：** 编辑框属性，包含文本输入类型和Enter键功能类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### let enterKeyType

```cangjie
public let enterKeyType: EnterKeyType
```

**功能：** Enter键功能类型。

**类型：** [EnterKeyType](#enum-enterkeytype)

**读写能力：** 只读

**起始版本：** 19

### let textInputType

```cangjie
public let textInputType: TextInputType
```

**功能：** 文本输入类型。

**类型：** [TextInputType](#enum-textinputtype)

**读写能力：** 只读

**起始版本：** 19

### InputAttribute(TextInputType, EnterKeyType)

```cangjie
public InputAttribute(
    public let textInputType: TextInputType,
    public let enterKeyType: EnterKeyType
)
```

**功能：** 构建编辑框属性的对象。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|textInputType|[TextInputType](#enum-textinputtype)|是|-|文本输入类型。|
|enterKeyType|[EnterKeyType](#enum-enterkeytype)|是|-|Enter键功能类型。|