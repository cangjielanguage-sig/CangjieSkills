## `cjdb` 命令

> **说明：**
>
> 获取更多命令，可以在命令行窗口执行`help`：
>
> ```text
> (cjdb) help
> Debugger commands:
>   apropos           -- List debugger commands related to a word or subject.
>   breakpoint        -- Commands for operating on breakpoints (see 'help b' for shorthand.)
>   cjthread          -- Commands for operating on one or more cjthread in the current process.
>   command           -- Commands for managing custom LLDB commands.
>   disassemble       -- Disassemble specified instructions in the current target.  Defaults to the current function for the current thread and stack frame.
>   expression        -- Evaluate an expression on the current thread.  Displays any returned value with LLDB's default formatting.
>   frame             -- Commands for selecting and examing the current thread's stack frames.
> ...
> ```
>

### 日志

为了方便定位问题，可以使用 `log <subcommand> [<command-options>]` 命令记录 `cjdb` 日志。

- `help log` 查看 `log` 命令帮助

  ```text
  (cjdb) help log
  Commands controlling LLDB internal logging.
  Syntax: log <subcommand> [<command-options>]
  The following subcommands are supported:
        disable -- Disable one or more log channel categories.
        enable  -- Enable logging for a single log channel.
        list    -- List the log categories for one or more log channels.  If none specified, lists them all.
        timers  -- Enable, disable, dump, and reset LLDB internal performance timers.
  For more help on any particular subcommand, type 'help <command> <subcommand>'.
  ```

- `log list` 查看支持的日志列表

  ```text
  (cjdb) log list
  ```

  其他命令可结合 help 命令自行获取。

### 平台

`cjdb` 中用于管理和创建平台的命令有`platform [connect|disconnect|info|list|status|select] ...`

- `windows` 平台查看 `platform` 帮助的信息。

  ```text
  (cjdb) help platform
  Commands to manage and create platforms.
  Syntax: platform [connect|disconnect|info|list|status|select] ...
  The following subcommands are supported:
        connect        -- Select the current platform by providing a connection URL.
        disconnect     -- Disconnect from the current platform.
        file           -- Commands to access files on the current platform.
        get-file       -- Transfer a file from the remote end to the local host.
        get-size       -- Get the file size from the remote end.
        list           -- List all platforms that are available.
        mkdir          -- Make a new directory on the remote end.
        process        -- Commands to query, launch and attach to processes on the current platform.
        put-file       -- Transfer a file from this system to the remote end.
        select         -- Create a platform if needed and select it as the current platform.
        settings       -- Set settings for the current target's platform, or for a platform by name.
        shell          -- Run a shell command on the current platform.  Expects 'raw' input (see 'help raw-input'.)
        status         -- Display status for the current platform.
        target-install -- Install a target (bundle or executable file) to the remote end.
  For more help on any particular subcommand, type 'help <command> <subcommand>'.
  (cjdb)
  ```