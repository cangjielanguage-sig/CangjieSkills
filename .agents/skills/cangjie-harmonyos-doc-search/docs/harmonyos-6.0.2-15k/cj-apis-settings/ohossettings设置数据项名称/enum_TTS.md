## enum TTS

```cangjie
public enum TTS <: ToString {
    | DEFAULT_TTS_PITCH
    | DEFAULT_TTS_RATE
    | DEFAULT_TTS_SYNTH
    | ENABLED_TTS_PLUGINS
    | ...
}
```

**功能：** 提供设置文本到语音（TTS）转换信息的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**父类型：**

- ToString

### DEFAULT_TTS_PITCH

```cangjie
DEFAULT_TTS_PITCH
```

**功能：** 文本转语音(TTS)引擎的默认音高。其中100=1x，该值设置为200，表示频率是正常声音频率的两倍。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DEFAULT_TTS_RATE

```cangjie
DEFAULT_TTS_RATE
```

**功能：** TTS引擎的默认语速。其中100=1x。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DEFAULT_TTS_SYNTH

```cangjie
DEFAULT_TTS_SYNTH
```

**功能：** 默认TTS引擎。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### ENABLED_TTS_PLUGINS

```cangjie
ENABLED_TTS_PLUGINS
```

**功能：** 于TTS的已激活插件包列表， 多个插件包以空格分隔。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回设置文本到语音(TTS)转换信息的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**返回值：**

| 类型  | 说明  |
| :------ | :------ |
| String | 设置文本到语音(TTS)转换信息的数据项。 |