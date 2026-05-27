/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// The Cangjie API is in Beta. For details on its capabilities and limitations, please refer to the README file.

package ohos.app.ability.start_options

import ohos.app.ability.ability_constant.{WindowMode, WINDOW_MODE_UNDEFINED}
import ohos.app.ability.completion_handler.CompletionHandler
import ohos.app.ability.context_constant.{ProcessMode, StartupVisibility, PROCESS_MODE_UNSPECIFIED, STARTUP_VISIBILITY_UNSPECIFIED}
import ohos.bundle.bundle_manager.SupportedWindowMode
import ohos.multimedia.image.PixelMap
import ohos.labels.{APILevel, Hide}
import ohos.window.WindowCreateParams

class StartOptionsImpl {}

/**
 * StartOptions is the basic communication component of the system.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public open class StartOptions {
    /**
     * The type of WindowMode
     * WindowModeSplitPrimary and WindowModeSplitSecondary are
     * valid only in intra-app redirection scenarios.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var windowMode: ?WindowMode

    /**
     * The type of displayId
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var displayId: Int32
    var withAnimation: Bool = true
    var windowLeft: Int32 = 0
    var windowTop: Int32 = 0
    var windowWidth: Int32 = 0
    var windowHeight: Int32 = 0
    var windowFocused: Bool = false
    var processMode: ?ProcessMode = None
    var startupVisibility: ?StartupVisibility = None
    var startWindowIcon: ?PixelMap = None
    var startWindowBackgroundColor = ""
    var supportWindowModes = Array<SupportedWindowMode>()
    var minWindowWidth: Int32 = 0
    var minWindowHeight: Int32 = 0
    var maxWindowWidth: Int32 = 0
    var maxWindowHeight: Int32 = 0
    var completionHandler: ?CompletionHandler = None
    var hideStartWindow: Bool = false
    private let impl_: StartOptionsImpl = StartOptionsImpl()

    @!Hide[isChecked: true]
    internal var windowCreateParams: Option<WindowCreateParams> = None

    /**
     * StartOptions constructor.
     *
     * @param { ?WindowMode } [windowMode] - The type of WindowMode. The default value is None.
     * @param { Int32 } [displayId] - The type of displayId. The default value is 0.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public init(
        windowMode!: ?WindowMode = None,
        displayId!: Int32 = 0
    ) {
        this.windowMode = windowMode
        this.displayId = displayId
    }

    func toExternal(): CJStartOptions {
        return CJStartOptions(windowMode?.getValue() ?? WINDOW_MODE_UNDEFINED, displayId)
    }

    func toCJNewStartOptions(): CJNewStartOptions {
        return CJNewStartOptions(
            windowMode?.getValue() ?? WINDOW_MODE_UNDEFINED,
            displayId,
            withAnimation,
            windowLeft,
            windowTop,
            windowWidth,
            windowHeight,
            processMode?.getValue() ?? PROCESS_MODE_UNSPECIFIED,
            startupVisibility?.getValue() ?? STARTUP_VISIBILITY_UNSPECIFIED
        )
    }
}

protected func startOptionsToExternal(startOptions: StartOptions): CJStartOptions {
    return startOptions.toExternal()
}

protected func startOptionsToCJNewStartOptions(startOptions: StartOptions): CJNewStartOptions {
    return startOptions.toCJNewStartOptions()
}

@C
protected struct CJStartOptions {
    protected CJStartOptions(
        let windowMode: Int32,
        let displayId: Int32
    ) {}
}

@C
protected struct CJNewStartOptions {
    protected CJNewStartOptions(
        let windowMode: Int32,
        let displayId: Int32,
        let withAnimation: Bool,
        let windowLeft: Int32,
        let windowTop: Int32,
        let windowWidth: Int32,
        let windowHeight: Int32,
        let processMode: Int32,
        let startupVisibility: Int32
    ) {}
}
