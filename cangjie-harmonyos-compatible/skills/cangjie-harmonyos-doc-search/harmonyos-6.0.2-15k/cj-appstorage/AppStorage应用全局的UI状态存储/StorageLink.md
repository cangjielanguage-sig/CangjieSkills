## @StorageLink

@StorageLink(key)是和AppStorage中key对应的属性建立双向数据同步：

1. 本地修改发生，该修改会被写回AppStorage中。
2. AppStorage中的修改发生后，该修改会被同步到所有绑定AppStorage对应key的属性上，包括单向（@StorageProp和通过Prop创建的单向绑定变量）、双向（@StorageLink和通过Link创建的双向绑定变量）变量和其他实例（比如PersistentStorage）。

### 宏使用规则说明

|@StorageLink变量宏|说明|
|:---|:---|
|宏参数|key：常量字符串，必填（字符串需要有引号）。|
|允许装饰的变量类型|class、String、整数、浮点、Bool、enum类型，以及这些类型的数组。<br>支持Datetime，Map，Set类型。嵌套类型的场景请参见[观察变化和行为表现](#观察变化和行为表现)。<br>类型必须被指定，建议和LocalStorage中对应属性类型相同，否则会发生类型隐式转换，从而导致应用行为异常。<br>不支持Any。|
|同步类型|双向同步：从AppStorage的对应属性到自定义组件，从自定义组件到AppStorage对应属性。|
|被装饰变量的初始值|必须指定，如果AppStorage实例中不存在属性，则用该初始值初始化该属性，并存入AppStorage中。|

### 变量的传递/访问规则说明

|传递/访问|说明|
|:---|:---|
|从父节点初始化和更新|禁止。|
|初始化子节点|支持，可用于初始化常规变量、@State、@Link、@Prop、@Provide。|
|是否支持组件外访问|否。|

**@StorageLink初始化规则图示**

![StorageLink](figures/StorageLink.png)

### 观察变化和行为表现

#### 观察变化

- 当装饰的数据类型为Bool、String、整数、浮点类型时，可以观察到数值的变化。
- 当装饰的数据类型为class时，可以观察到对象整体赋值和对象属性变化（详见[从ui内部使用appstorage和localstorage](#从ui内部使用appstorage和localstorage)）。
- 当装饰的对象是Array时，可以观察到数组添加、删除、更新数组单元的变化。
- 当装饰的对象是Datetime时，可以观察到Datetime整体的赋值，同时可通过调用Datetime的接口addYears，addMonths，addWeeks，addMinutes，addSeconds，addNanoseconds更新Datetime的属性。详见[装饰Datetime类型变量](#装饰datetime类型变量)。
- 当装饰的变量是Map时，可以观察到Map整体的赋值，同时可通过调用Map的接口add，clear，remove更新Map的值。详见[装饰Map类型变量](#装饰map类型变量)。
- 当装饰的变量是Set时，可以观察到Set整体的赋值，同时可通过调用Set的接口add，clear，remove更新Set的值。详见[装饰Set类型变量](#装饰set类型变量)。

#### 框架行为

1. 当@StorageLink(key)装饰的数值改变被观察到时，修改将被同步回AppStorage对应属性键值key的属性中。
2. AppStorage中属性键值key对应的数据一旦改变，属性键值key绑定的所有的数据（包括双向@StorageLink和单向@StorageProp）都将同步修改。
3. 当@StorageLink(key)装饰的数据本身是状态变量，它的改变不仅仅会同步回AppStorage中，还会引起所属的自定义组件的重新渲染。