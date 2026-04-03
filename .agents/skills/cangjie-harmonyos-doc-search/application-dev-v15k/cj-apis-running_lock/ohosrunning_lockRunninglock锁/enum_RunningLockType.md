## enum RunningLockType

```cangjie
public enum RunningLockType <: ToString {
    | PROXIMITY_SCREEN_CONTROL
    | ...
}
```

**功能：** RunningLock锁的类型。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

**父类型：**

- ToString

### PROXIMITY_SCREEN_CONTROL

```cangjie
PROXIMITY_SCREEN_CONTROL
```

**功能：** 接近光锁，使能接近光传感器，并根据传感器与障碍物的距离远近发起亮灭屏流程。

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举类型的字符串表示。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举类型的字符串表示。|