### 结合 hilog

#### DFX 相关日志

1. 故障上报（reportEvent）。

    ![appfreeze_01](figures/appfreeze_01.png)

2. 抓栈（signal: 35）。

    ![appfreeze_02](figures/appfreeze_02.png)

3. 后台应用检测（5次后上报），21s 左右。

    ![appfreeze_03](figures/appfreeze_03.png)

4. 记录查杀原因。

    ![appfreeze_04](figures/appfreeze_04.png)

5. APPFREEZE kill 应用appfreeze。

    ![appfreeze_05](figures/appfreeze_05.png)

#### 一般分析步骤

根据故障日志确定上报时间点，再根据具体场景下的故障类型推断appfreeze开始发生的时间点，查看对应时间段的hilog日志，分析日志得出应用对应线程运行状态：

- 应用日志完全无打印输出：appfreeze在最后日志打印的接口调用处。

   ![appfreeze_06](figures/appfreeze_06.png)

   ![appfreeze_07](figures/appfreeze_07.png)

   例如上图案例：APP_INPUT_BLOCK 类型在 07:24:08.167 上报，应用主线程在 07:24:01.581 后就没有打印了，可排查是否为 FormManagerService：

   [form_mgr_proxy.cpp(GetFormsInfoByApp:1128)] 中的逻辑超时。

- 应用频繁打印输出日志：分析对应输出表示的场景及其合理性。

   ![appfreeze_08](figures/appfreeze_08.png)

   例如上图案例：进程在被 APP_FREEZE 杀死前在大量输出，对应的 ImageEffect 领域需排查此日志是否正常。

### 结合 trace

存在以下可能：

1. 进程每一小段业务时间并不长，但是较长时间段运行非常密集，占满了主线程。

    ![appfreeze_09](figures/appfreeze_09.png)

    ![appfreeze_10](figures/appfreeze_10.png)

    上图案例为：PriviewArea::updateShotComponent（更新组件） -> animator （执行动画）-> 密集的动画执行过程达 9.2s；

    线程繁忙地循环执行某业务，分析每一小段业务：

    - 不符合业务场景（此处不应该频繁调用），分析业务代码，为何会循环执行；
    - 符合业务场景，分析每一小段业务是否耗时超过预期，性能为何不满足设计规格。

2. 进程执行某一函数接口超时。

    ![appfreeze_11](figures/appfreeze_11.png)

    上图案例为：OHOS::AppExecFwk::FormMgrAdapter::GetFormsInfoByApp 接口执行时长达到 8s。