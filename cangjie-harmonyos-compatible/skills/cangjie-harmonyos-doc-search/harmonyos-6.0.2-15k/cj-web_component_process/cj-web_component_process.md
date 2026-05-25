# ArkWeb进程

ArkWeb是多进程模型，分为应用进程、Foundation进程、Web孵化进程、Web渲染进程和Web GPU进程。

> **说明：**
>
> Web内核没有明确的内存大小申请约束，理论上可以无限大，直到被资源管理释放。

**图1** ArkWeb进程模型图

![web-component-process](figures/arkweb_component_process.png)

- 应用进程中Web相关线程（应用唯一）

    - 应用进程为主进程。包含网络线程、Video线程、Audio线程和IO线程等。
    - 负责Web组件的北向接口与回调处理，网络请求、媒体服务等需要与其他系统服务交互的功能。

- Foundation进程（系统唯一）

    负责接收应用进程进行孵化进程的请求，管理应用进程和Web渲染进程的绑定关系。

- Web孵化进程（系统唯一）

    - 负责接收Foundation进程的请求，执行孵化Web渲染进程与Web GPU进程。
    - 执行孵化后处理安全沙箱降权、预加载动态库，以提升性能。

- Web渲染进程（应用可指定多Web实例间共享或独立进程）

    - 负责运行Web渲染进程引擎（HTML解析、排版、绘制、渲染）。
    - 负责运行ArkWeb执行引擎（JavaScript、Web Assembly）。
    - 提供接口供应用选择多Web实例间是否共享渲染进程，满足不同场景对安全性、稳定性、内存占用的诉求。
    - 默认策略：移动设备上共享渲染进程以节省内存，2in1设备上独立渲染进程提升安全与稳定性。

- Web GPU进程（应用唯一）

    负责光栅化、合成送显等与GPU、RenderService交互功能。提升应用进程稳定性、安全性。

相关API如下：

1. 可通过[setRenderProcessMode](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#static-func-setrenderprocessmoderenderprocessmode)设置渲染子进程的模式，从而控制渲染过程的单进程或多进程状态。

    移动设备默认为单进程渲染，而2in1设备则默认采用多进程渲染。通过调用[getRenderProcessMode](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#static-func-getrenderprocessmode)可查询当前的渲染子进程模式，其中枚举值0表示单进程模式，枚举值1对应多进程模式。若获取的值超出[RenderProcessMode](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#enum-renderprocessmode)枚举范围，系统将自动采用多进程渲染模式作为默认设置。

    ```cangjie
    // xxx.cj
    import kit.ArkWeb.{WebviewController, RenderProcessMode}
    import kit.UIKit.{Web, BusinessException}

    @Entry
    @Component
    class EntryView {
        let webController = WebviewController()

        func build() {
            Column {
                Button("getRenderProcessMode").onClick {
                    evt =>
                    // 查询当前的渲染子进程模式
                    let mode = WebviewController.getRenderProcessMode()
                    AppLog.info("getRenderProcessMode: ${mode}")
                }.margin(10)

                Button("setRenderProcessMode").onClick {
                    evt => try {
                        // 设置渲染子进程的模式
                        WebviewController.setRenderProcessMode(RenderProcessMode.MULTIPLE)
                    } catch (e: BusinessException) {
                        AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                    }
                }.margin(10)
                Web(src: 'www.example.com', controller: this.webController)
            }
        }
    }
    ```

2. 可通过[terminateRenderProcess](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-terminaterenderprocess)来主动关闭渲染进程。若渲染进程尚未启动或已销毁，此操作将不会产生任何影响。此外，销毁渲染进程将同时影响所有与之关联的其他实例。

    ```cangjie
    // xxx.cj
    import kit.ArkWeb.WebviewController
    import kit.UIKit.{Web, BusinessException}

    @Entry
    @Component
    class EntryView {
        let webController = WebviewController()

        func build() {
            Column {
                Button("terminateRenderProcess").onClick {
                    evt => try {
                        let result = webController.terminateRenderProcess()
                        AppLog.info("terminateRenderProcess result: ${result}")
                    } catch (e: BusinessException) {
                        AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}");
                    }
                }
                Web(src: 'www.example.com', controller: this.webController)
            }
        }
    }
    ```
