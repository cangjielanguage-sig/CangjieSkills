## enum SoundPoolEvent

```cangjie
public enum SoundPoolEvent <: ToString {
    | LoadCompleted
    | PlayFinished
    | EventError
    | ...
}
```

**功能：** soundPool事件状态。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**父类型：**

- ToString

### EventError

```cangjie
EventError
```

**功能：** 错误事件。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

### LoadCompleted

```cangjie
LoadCompleted
```

**功能：** 事件加载完成。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

### PlayFinished

```cangjie
PlayFinished
```

**功能：** 事件播放完成。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取事件信息。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|获取事件信息。|