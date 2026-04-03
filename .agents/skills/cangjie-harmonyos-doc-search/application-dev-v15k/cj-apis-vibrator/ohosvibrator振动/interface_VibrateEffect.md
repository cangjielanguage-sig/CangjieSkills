## interface VibrateEffect

```cangjie
public interface VibrateEffect {
    prop effectType: String
}
```

**功能：** 马达振动效果。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

### prop effectType

```cangjie
prop effectType: String
```

**功能：** 马达振动效果类型。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

| 支持类型                                       | 说明                                 |
| :----------------------------------------- | :----------------------------------- |
| "[VibrateTime](#class-vibratetime)"         | 按照指定持续时间触发马达振动。       |
| "[VibratePreset](#class-vibratepreset)"     | 按照预置振动类型触发马达振动。       |
| "[VibrateFromFile](#class-vibratefromfile)" | 按照自定义振动配置文件触发马达振动。 |