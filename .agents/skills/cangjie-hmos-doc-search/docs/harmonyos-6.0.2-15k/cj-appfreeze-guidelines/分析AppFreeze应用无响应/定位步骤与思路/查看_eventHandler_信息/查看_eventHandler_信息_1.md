### 查看 eventHandler 信息

开发者可以通过 “mainHandler dump is” 关键字搜索日志中的 eventHandler dump 信息。

1. dump begin curTime & Current Running。

    ```text
    mainHandler dump is:
    EventHandler dump begin curTime: 2024-08-08 12:17:43.544      --> 开始 dump 时间
    Event runner (Thread name = , Thread ID = 35854) is running   --> 正在运行的线程信息
    Current Running: start at 2024-08-08 12:17:16.629, Event { send thread = 35882, send time = 2024-08-08 12:17:16.628,  handle time = 2024-08-08 12:17:16.629, trigger time = 2024-08-08 12:17:16.630, task name = , caller = xx }  
    --> trigger time--> 任务开始运行的时间
    ```

    当前任务运行时长 = dump begin curTime - trigger time, 如示例中当前任务运行达到27s。

    若任务运行时长 > 故障检测时长，表示当前正在运行的任务是导致应用appfreeze的任务，需对该任务进行排查。

    若任务运行时长较小，表示当前任务仅是检测时间区间内主线程运行的任务之一，主要耗时不一定是该任务，建议优先查看近期耗时最长任务（History event queue information中）。该情形多为线程繁忙导致的watchdog无法调度执行。

2. History event queue information。

    ```text
    Current Running: start at 2024-08-08 12:17:16.629, Event { send thread = 35882, send time = 2024-08-08 12:17:16.628, handle time = 2024-08-08 12:17:16.629, trigger time = 2024-08-08 12:17:16.630, task name = , caller = [extension_ability_thread.cpp(ScheduleAbilityTransaction:393)]}
    History event queue information:
    No. 0 : Event { send thread = 35854, send time = 2024-08-08 12:17:15.525, handle time = 2024-08-08 12:17:15.525, trigger time = 2024-08-08 12:17:15.527, completeTime time = 2024-08-08 12:17:15.528, priority = High, id = 1 }
    No. 1 : Event { send thread = 35854, send time = 2024-08-08 12:17:15.525, handle time = 2024-08-08 12:17:15.525, trigger time = 2024-08-08 12:17:15.527, completeTime time = 2024-08-08 12:17:15.527, priority = Low, task name = MainThread:SetRunnerStarted }
    No. 2 : Event { send thread = 35856, send time = 2024-08-08 12:17:15.765, handle time = 2024-08-08 12:17:15.765, trigger time = 2024-08-08 12:17:15.766, completeTime time = 2024-08-08 12:17:15.800, priority = Low, task name = MainThread:LaunchApplication }
    No. 3 : Event { send thread = 35856, send time = 2024-08-08 12:17:15.767, handle time = 2024-08-08 12:17:15.767, trigger time = 2024-08-08 12:17:15.800, completeTime time = 2024-08-08 12:17:16.629, priority = Low, task name = MainThread:LaunchAbility }
    No. 4 : Event { send thread = 35854, send time = 2024-08-08 12:17:15.794, handle time = 2024-08-08 12:17:15.794, trigger time = 2024-08-08 12:17:16.629, completeTime time = 2024-08-08 12:17:16.629, priority = IDEL, task name = IdleTime:PostTask }
    No. 5 : Event { send thread = 35852, send time = 2024-08-08 12:17:16.629, handle time = 2024-08-08 12:17:16.629, trigger time = 2024-08-08 12:17:16.629, completeTime time = , priority = Low, task name =  }
    ```

    可以从历史任务队列中寻找故障发生时间区间内较为耗时的任务。其中CompleteTime time 为空的任务是当前任务。

    任务运行耗时 = CompleteTime time - trigger time。

    筛选出耗时较高的任务，排查其运行情况。

3. VIP priority event queue information。