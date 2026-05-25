## class DataChangeListener

```cangjie
public class DataChangeListener {}
```

**功能：** 数据变化监听器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func onDataAdd(IntNative)

```cangjie
public func onDataAdd(index: IntNative): Unit
```

**功能：** 通知组件index的位置有数据添加。添加数据完成后调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|IntNative|是|-|数据添加位置的索引值。|

### func onDataChange(IntNative)

```cangjie
public func onDataChange(index: IntNative): Unit
```

**功能：** 通知组件index的位置有数据有变化。改变数据完成后调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|IntNative|是|-|数据变化位置的索引值。|

### func onDataDelete(IntNative)

```cangjie
public func onDataDelete(index: IntNative): Unit
```

**功能：** 通知组件删除index位置的数据并刷新LazyForEach的展示内容。删除数据完成后调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|IntNative|是|-|数据删除位置的索引值。|

### func onDataMove(IntNative, IntNative)

```cangjie
public func onDataMove(from: IntNative, to: IntNative): Unit
```

**功能：** 通知组件数据有移动。将from和to位置的数据进行交换。数据移动起始位置与数据移动目标位置交换完成后调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|from|IntNative|是|-|数据移动起始位置。|
|to|IntNative|是|-|数据移动目标位置。|

### func onDataReloaded()

```cangjie
public func onDataReloaded(): Unit
```

**功能：** 通知组件重新加载所有数据。键值没有变化的数据项会使用原先的子组件，键值发生变化的会重建子组件。重新加载数据完成后调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22