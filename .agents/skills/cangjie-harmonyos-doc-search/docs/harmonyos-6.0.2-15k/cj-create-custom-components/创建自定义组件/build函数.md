## build()函数

所有声明在build()函数的语句统称为UI描述，需要遵循以下规则：

- @Entry装饰的自定义组件，其build()函数下的根节点唯一且必要，且必须为容器组件，其中ForEach禁止作为根节点。
- @Component装饰的自定义组件，其build()函数下的根节点唯一且必要，可以为非容器组件，其中ForEach禁止作为根节点。

  <!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry

  import kit.UIKit.*
  import ohos.state_macro_manage.*
  import kit.LocalizationKit.*

  @Entry
  @Component
  class EntryView {
      func build() {
          // 根节点唯一且必要，必须为容器组件
          Row() {
              ChildComponent()
          }
      }
  }

  @Component
  class ChildComponent {
      func build() {
          // 根节点唯一且必要，可为非容器组件
          Image(@r(app.media.startIcon))
      }
  }
  ```

- 不允许声明本地变量，反例如下。

  ```cangjie
  func build() {
      let num: Int64 = 0
  }
  ```

- 不允许在UI描述里直接使用Hilog.info，但允许在方法或者函数里使用，反例如下。

  ```cangjie
  func build() {
      //反例：不允许Hilog.info
      Hilog.info(0, "test", "print debug log")
  }
  ```

- 不允许创建本地的作用域，反例如下。

  ```cangjie
  func build() {
      // 反例：不允许本地作用域
      {
          // ...
      }
  }
  ```

- 不允许调用没有用@Builder装饰的方法，允许系统组件的参数是CJ方法的返回值。

  ```cangjie
  @Component
  class EntryView {
      func doSomeCalculations() {
      }
      func calcTextValue(): String {
          return "Hello World"
      }
      @Builder
      func doSomeRender() {
          Text("Hello World")
      }
      func build() {
          Column() {
              // 反例：不能调用没有用@Builder装饰的方法
              this.doSomeCalculations()
              // 正例：可以调用
              this.doSomeRender()
              // 正例：参数可以为调用CJ方法的返回值
              Text(this.calcTextValue())
          }
      }
  }
  ```

- 不允许使用match语法，如果需要使用条件判断，请使用[if](../rendering_control/cj-rendering-control-ifelse.md)。示例如下。

  ```cangjie
  func build() {
      Column() {
          // 反例：不允许使用match语法
          match (expression) {
              case 0 => Text("...")
              case 1 => Text("...")
              case _ => Text("...")
          }
          // 正例：使用if
          if (expression == 1) {
              Text("...")
          } else if (expression == 2) {
              Button("...")
          } else {
              Text("...")
          }
      }
  }
  ```

- 不允许直接改变状态变量，反例如下。详细分析见[@State常见问题：不允许在build里改状态变量](../state_management/cj-macro-state.md#不允许在build里改状态变量)。

  ```cangjie
  @Component
  class EntryView {
      @State
      var textColor: Color = Color.YELLOW
      @State
      var columnColor: Color = Color.GREEN
      @State
      var count: Int64 = 1
      func build() {
          Column() {
              // 不允许直接在Text组件内改变count的值
              Text("${this.count++}").width(50).height(50).fontColor(this.textColor).onClick(
                  {etv => this.columnColor = Color.RED})
              Button("change textColor").onClick({etv => this.textColor = Color.PINK})
          }.backgroundColor(this.columnColor)
      }
  }
  ```