## @StorageProp

在上文中已经提到，如果要建立AppStorage和自定义组件的联系，需要使用@StorageProp和@StorageLink宏。使用@StorageProp(key)/@StorageLink(key)装饰组件内的变量，key标识了AppStorage的属性。

当自定义组件初始化的时候，会使用AppStorage中对应key的属性值将@StorageProp(key)/@StorageLink(key)装饰的变量初始化。由于应用逻辑的差异，无法确认是否在组件初始化之前向AppStorage实例中存入了对应的属性，所以AppStorage不一定存在key对应的属性，因此@StorageProp(key)/@StorageLink(key)装饰的变量进行本地初始化是必要的。

@StorageProp(key)是和AppStorage中key对应的属性建立单向数据同步，如果AppStorage给定key的属性发生改变，改变会被同步给@StorageProp，并覆盖掉本地的修改。

### 宏使用规则说明

|@StorageProp变量宏|说明|
|:---|:---|
|宏参数|key：常量字符串，必填（字符串需要有引号）。|
|允许装饰的变量类型|class、String、整数、浮点、Bool、enum类型，以及这些类型的数组。<br>支持Datetime，Map，Set类型。嵌套类型的场景请参见[观察变化和行为表现](#观察变化和行为表现)。<br>类型必须被指定，建议和LocalStorage中对应属性类型相同，否则会发生类型隐式转换，从而导致应用行为异常。<br>不支持Any。|
|同步类型|单向同步：从AppStorage的对应属性到组件的状态变量。AppStorage中给定的属性一旦发生变化，将覆盖本地的修改。|
|被装饰变量的初始值|必须指定，如果AppStorage实例中不存在属性，则用该初始值初始化该属性，并存入AppStorage中。|

### 变量的传递/访问规则说明

|传递/访问|说明|
|:---|:---|
|从父节点初始化和更新|禁止，@StorageProp不支持从父节点初始化，只能AppStorage中key对应的属性初始化，如果没有对应key的话，将使用本地默认值初始化。|
|初始化子节点|支持，可用于初始化@State、@Link、@Prop、@Provide。|
|是否支持组件外访问|否。|

**@StorageProp初始化规则图示**

![StorageProp](figures/StorageProp.png)

### 观察变化和行为表现

#### 观察变化

- 当装饰的数据类型为Bool、String、整数、浮点类型时，可以观察到数值的变化。
- 当装饰的数据类型为class时，可以观察到对象整体赋值和对象属性变化（详见[从ui内部使用appstorage和localstorage](#从ui内部使用appstorage和localstorage)）。
- 当装饰的对象是Array时，可以观察到数组添加、删除、更新数组单元的变化。
- 当装饰的对象是Datetime时，可以观察到Datetime整体的赋值，同时可通过调用Datetime的接口addYears，addMonths，addWeeks，addMinutes，addSeconds，addNanoseconds更新Datetime的属性。详见[装饰Datetime类型变量](#装饰datetime类型变量)。
- 当装饰的变量是Map时，可以观察到Map整体的赋值，同时可通过调用Map的接口add，clear，remove 更新Map的值。详见[装饰Map类型变量](#装饰map类型变量)。
- 当装饰的变量是Set时，可以观察到Set整体的赋值，同时可通过调用Set的接口add，clear，remove 更新Set的值。详见[装饰Set类型变量](#装饰set类型变量)。

#### 框架行为

- 被@StorageProp装饰的变量为不可变类型。
- 当@StorageProp(key)装饰的数据本身是状态变量，会引起所属的自定义组件重新渲染。
- 当AppStorage中key对应的属性发生改变时，会同步给所有@StorageProp(key)装饰的数据，@StorageProp(key)本地的修改将被覆盖。