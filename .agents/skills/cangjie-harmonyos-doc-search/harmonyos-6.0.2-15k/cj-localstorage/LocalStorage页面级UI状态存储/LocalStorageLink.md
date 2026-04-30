## @LocalStorageLink

如果我们需要将自定义组件的状态变量的更新同步回LocalStorage，就需要用到@LocalStorageLink。

@LocalStorageLink(key)是和LocalStorage中key对应的属性建立双向数据同步：

1. 本地修改发生，该修改会被写回LocalStorage中。
2. LocalStorage中的修改发生后，该修改会被同步到所有绑定LocalStorage对应key的属性上，包括单向（@LocalStorageProp和通过prop创建的单向绑定变量）、双向（@LocalStorageLink和通过link创建的双向绑定变量）变量。

### 宏使用规则说明

|@LocalStorageLink变量宏|说明|
|:---|:---|
|宏参数|key：常量字符串，必填（字符串需要有引号）。|
|允许装饰的变量类型|class、String、整数、浮点、Bool、enum类型，以及这些类型的数组。<br>支持Datetime，Map，Set类型。嵌套类型的场景请参见[观察变化和行为表现](#观察变化和行为表现)。<br>类型必须被指定，建议和LocalStorage中对应属性类型相同，否则会发生类型隐式转换，从而导致应用行为异常。<br>不支持Any。|
|同步类型|双向同步：从LocalStorage的对应属性到自定义组件，从自定义组件到LocalStorage对应属性。|
|被装饰变量的初始值|必须指定，如果LocalStorage实例中不存在属性，则用该初始值初始化该属性，并存入LocalStorage中。|

### 变量的传递/访问规则说明

|传递/访问|说明|
|:---|:---|
|从父节点初始化和更新|禁止，@LocalStorageLink不支持从父节点初始化，只能从LocalStorage中key对应的属性初始化，如果没有对应key的话，将使用本地默认值初始化。|
|初始化子节点|支持，可用于初始化@State、@Link、@Prop、@Provide。|
|是否支持组件外访问|否。|

**@LocalStorageLink初始化规则图示**

![LocalStorageLink](figures/LocalStorageLink.png)

### 观察变化和行为表现

#### 观察变化

- 当装饰的数据类型为Bool、String、整数、浮点类型时，可以观察到数值的变化。
- 当装饰的数据类型为class时，可以观察到对象整体赋值和对象属性变化（详见[从ui内部使用localstorage](#从ui内部使用localstorage)）。
- 当装饰的对象是Array时，可以观察到数组添加、删除、更新数组单元的变化。
- 当装饰的对象是Datetime时，可以观察到Datetime整体的赋值，同时可通过调用Datetime的接口addYears，addMonths，addWeeks，addMinutes，addSeconds，addNanoseconds更新Datetime的属性。详见[装饰Datetime类型变量](#装饰datetime类型变量)。
- 当装饰的变量是Map时，可以观察到Map整体的赋值，同时可通过调用Map的接口add，clear，remove更新Map的值。详见[装饰Map类型变量](#装饰map类型变量)。
- 当装饰的变量是Set时，可以观察到Set整体的赋值，同时可通过调用Set的接口add，clear，remove更新Set的值。详见[装饰Set类型变量](#装饰set类型变量)。

#### 框架行为

1. 当@LocalStorageLink(key)装饰的数值改变被观察到时，修改将被同步回LocalStorage对应属性键值key的属性中。
2. LocalStorage中属性键值key对应的数据一旦改变，属性键值key绑定的所有的数据（包括双向@LocalStorageLink和单向@LocalStorageProp）都将同步修改。
3. 当@LocalStorageLink(key)装饰的数据本身是状态变量，它的改变不仅仅会同步回LocalStorage中，还会引起所属的自定义组件的重新渲染。

![LocalStorageLink(key)](figures/LocalStorageLink_key.png)