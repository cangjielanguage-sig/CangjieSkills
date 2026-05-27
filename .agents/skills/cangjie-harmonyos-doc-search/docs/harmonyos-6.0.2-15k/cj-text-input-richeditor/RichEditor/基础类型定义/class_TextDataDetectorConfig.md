### class TextDataDetectorConfig

```cangjie
public class TextDataDetectorConfig {
    public var types: Array<TextDataDetectorType>
    public var onDetectResultUpdate: ?(String) -> Unit = None
    public var color: ?ResourceColor = None
    public var decoration: ?DecorationStyleInterface = None
    public init (
        types: Array<TextDataDetectorType>,
        onDetectResultUpdate!: ?(String) -> Unit = None,
        color!: ?ResourceColor = None,
        decoration!: ?DecorationStyleInterface = None
    )
}
```

**功能：** 文本识别配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var types

```cangjie
public var types: Array<TextDataDetectorType>
```

**功能：** 设置文本识别的实体类型。设置types为[]时，识别所有类型的实体，否则只识别指定类型的实体。

**类型：** Array<[TextDataDetectorType](./cj-text-input-text.md#enum-textdatadetectortype)>

**读写能力：** 可读写

**起始版本：** 20

#### var onDetectResultUpdate

```cangjie
public var onDetectResultUpdate: ?(String) -> Unit = None
```

**功能：** 文本识别成功后触发该回调函数。**参数:**：文本识别的结果，Json格式。

**类型：** ?(String) -> Unit

**读写能力：** 可读写

**起始版本：** 20

#### var color

```cangjie
public var color: ?ResourceColor = None
```

**功能：** 设置文本识别成功后的实体颜色。初始值：0xff0a59f7。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**起始版本：** 20

#### var decoration

```cangjie
public var decoration: ?DecorationStyleInterface = None
```

**功能：** 设置文本识别成功后的实体装饰线样式。初始值：type: TextDecorationType.Underline, color: 与实体颜色一致, style: TextDecorationStyle.SOLID。

**类型：** ?[DecorationStyleInterface](#class-decorationstyleinterface)

**读写能力：** 可读写

**起始版本：** 20

#### init(Array\<TextDataDetectorType>, ?(String) -> Unit, ?ResourceColor, ?DecorationStyleInterface)

```cangjie
public init (
        types: Array<TextDataDetectorType>,
        onDetectResultUpdate!: ?(String) -> Unit = None,
        color!: ?ResourceColor = None,
        decoration!: ?DecorationStyleInterface = None
    )
```

**功能：** 创建TextDataDetectorConfig类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|types|Array<[TextDataDetectorType](./cj-text-input-text.md#enum-textdatadetectortype)>|是|-| 设置文本识别的实体类型。设置types为[]时，识别所有类型的实体，否则只识别指定类型的实体。|
|onDetectResultUpdate|?(String) -> Unit|否|None|**命名参数。** 文本识别成功后触发该回调函数。<br>**参数:**：文本识别的结果，Json格式。|
|color|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。** 设置文本识别成功后的实体颜色。</br>初始值：0xff0a59f7。|
|decoration|?[DecorationStyleInterface](#class-decorationstyleinterface)|否|None|**命名参数。** 设置文本识别成功后的实体装饰线样式。</br>初始值：type: TextDecorationType.Underline, color: 与实体颜色一致, style: TextDecorationStyle.SOLID。|