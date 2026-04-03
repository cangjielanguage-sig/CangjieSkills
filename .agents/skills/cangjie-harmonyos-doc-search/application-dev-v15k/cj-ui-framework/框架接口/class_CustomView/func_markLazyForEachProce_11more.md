### func markLazyForEachProcess(String)

```cangjie
public func markLazyForEachProcess(groupId: String): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|groupId|String|是|-|-|

### func notifyRead(String)

```cangjie
public func notifyRead(stateInfo: String): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|stateInfo|String|是|-|-|

### func observeComponentCreation(UpdateFuncNew)

```cangjie
public func observeComponentCreation(compilerAssignedUpdateFunc: UpdateFuncNew): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|compilerAssignedUpdateFunc|UpdateFuncNew|是|-|-|

### func observeRecycleComponentCreation(String, RecycleUpdateFunc)

```cangjie
public func observeRecycleComponentCreation(name: String, recycleUpdateFunc: RecycleUpdateFunc)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|-|
|recycleUpdateFunc|RecycleUpdateFunc|是|-|-|

### func onStateUpdate(String)

```cangjie
public func onStateUpdate(stateInfo: String): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|stateInfo|String|是|-|-|

### func onStateUpdate(String, ArrayList\<Int64>)

```cangjie
public func onStateUpdate(stateInfo: String, dependentElmtIds: ArrayList<Int64>): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|stateInfo|String|是|-|-|
|dependentElmtIds|ArrayList\<Int64>|是|-|-|

### func purgeDeletedElmtIds(ArrayList\<Int64>)

```cangjie
public func purgeDeletedElmtIds(rmElmtIds: ArrayList<Int64>)
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rmElmtIds|ArrayList\<Int64>|是|-|-|

### func removeChildById(Int64)

```cangjie
public func removeChildById(id: Int64): Bool
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|是|-|-|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|-|

### func removeChildGroupById(String)

```cangjie
public func removeChildGroupById(groupId: String): Bool
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|groupId|String|是|-|-|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|-|

### func resetLazyForEachProcess()

```cangjie
public func resetLazyForEachProcess(): Unit
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### func resetRecycleCustomNode()

```cangjie
public func resetRecycleCustomNode()
```

**功能：** UI框架使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19