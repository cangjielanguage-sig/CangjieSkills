### func dataDetectorConfig(TextDataDetectorConfig)

```cangjie
public func dataDetectorConfig(config: TextDataDetectorConfig): This
```

**功能：** 设置文本识别配置。

需配合[enableDataDetector](#func-enabledatadetectorbool)一起使用，设置enableDataDetector为true时，dataDetectorConfig的配置才能生效。

当有两个实体A、B重叠时，按以下规则保留实体：

1. 若A ⊂ B，则保留B，反之则保留A。

2. 当A ⊄ B且B ⊄ A时，若A.start < B.start，则保留A，反之则保留B。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|config|[TextDataDetectorConfig](#class-textdatadetectorconfig)|是|-|文本识别配置。|

### func editMenuOptions(EditMenuOptions)

```cangjie
public func editMenuOptions(options: EditMenuOptions): This
```

**功能：** 设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[EditMenuOptions](#class-editmenuoptions)|是|-|扩展菜单选项。|