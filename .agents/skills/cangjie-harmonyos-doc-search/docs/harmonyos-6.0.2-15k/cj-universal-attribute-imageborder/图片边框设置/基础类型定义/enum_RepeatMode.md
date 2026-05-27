### enum RepeatMode

```cangjie
public enum RepeatMode {
    | SPACE
    | STRETCH
    | REPEAT
    | ROUND
}
```

**功能：** 设置被切割的图片在边框上的重复方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SPACE

```cangjie
SPACE
```

**功能：** 被切割图片以整数次平铺在图片边框上，无法以整数次平铺时以空白填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### STRETCH

```cangjie
STRETCH
```

**功能：** 被切割图片以拉伸填充的方式铺满图片边框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### REPEAT

```cangjie
REPEAT
```

**功能：** 被切割图片重复铺平在图片边框上，超出的部分会被剪裁。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ROUND

```cangjie
ROUND
```

**功能：** 被切割图片以整数次平铺在图片边框上，无法以整数次平铺时压缩被切割图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19