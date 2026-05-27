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

package ohos.app.ability.ui_ability

import ohos.app.ability.configuration.{CConfiguration, Configuration}
import ohos.bundle.bundle_manager.{HapModuleInfo, RetHapModuleInfoV2}
import ohos.labels.{APILevel, Hide}

@C
struct CurrentHapModuleInfo {
    CurrentHapModuleInfo(
        let name: CString,
        let icon: CString,
        let iconId: Int32,
        let label: CString,
        let labelId: Int32,
        let description: CString,
        let descriptionId: Int32,
        let mainElementName: CString,
        let installationFree: Bool,
        let hashValue: CString
    ) {}

    func free(): Unit {
        unsafe {
            LibC.free(this.name)
            LibC.free(this.icon)
            LibC.free(this.label)
            LibC.free(this.description)
            LibC.free(this.mainElementName)
            LibC.free(this.hashValue)
        }
    }
}

foreign func FFICJGetHapModuleInfo(id: Int64): RetHapModuleInfoV2

foreign func FFICJGetConfiguration(id: Int64): CConfiguration

/**
 * The context of an abilityStage. It allows access to abilityStage-specific resources.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public class AbilityStageContext <: Context {
    /**
     * Indicates configuration information about an module.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var currentHapModuleInfo: HapModuleInfo

    @!Hide[isChecked: true]
    internal var config: Configuration = Configuration()

    protected init(id: Int64) {
        super(id)
        unsafe {
            let hapInfo = FFICJGetHapModuleInfo(id)
            this.currentHapModuleInfo = HapModuleInfo(hapInfo)
            hapInfo.free()
        }
    }
}
