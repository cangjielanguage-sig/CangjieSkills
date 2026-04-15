### func set\<T>(String, T)

```cangjie
public func set<T>(propName: String, newValue: T): Bool
```

**功能：** 设置LocalStorage中propName对应的属性值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|
|newValue|T|是|-|要设置的新值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果LocalStorage中存在对应的属性，则设置成功并返回true，否则返回false。|

### func setAndLink\<T>(String, T)

```cangjie
public func setAndLink<T>(propName: String, defaultValue: T): ObservedProperty<T>
```

**功能：** 与LocalStorage中对应的propName建立双向属性绑定，如果属性不存在则创建并初始化。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|
|defaultValue|T|是|-|属性的默认值。|

**返回值：**

|类型|说明|
|:----|:----|
|ObservedProperty\<T>|返回双向绑定的数据。|

### func setAndProp\<T>(String, T)

```cangjie
public func setAndProp<T>(propName: String, defaultValue: T): ObservedProperty<T>
```

**功能：** 与LocalStorage中对应的propName建立单向属性绑定，如果属性不存在则创建并初始化。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|
|defaultValue|T|是|-|属性的默认值。|

**返回值：**

|类型|说明|
|:----|:----|
|ObservedProperty\<T>|返回单向绑定的数据。|

### func setOrCreate\<T>(String, T)

```cangjie
public func setOrCreate<T>(propName: String, newValue: T): Bool
```

**功能：** 设置LocalStorage中propName对应的属性值，如果属性不存在则创建并初始化。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|LocalStorage中的属性名。|
|newValue|T|是|-|要设置的新值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|操作成功返回true，否则返回false。|

### func size()

```cangjie
public func size(): Int64
```

**功能：** 获取LocalStorage中属性的数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回LocalStorage中属性的数量。|