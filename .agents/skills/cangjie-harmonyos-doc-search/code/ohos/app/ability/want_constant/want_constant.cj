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

package ohos.app.ability.want_constant

import ohos.labels.APILevel

/**
 * The constant for params of the want.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityBase"
]
public class Params {
    init() {}
    /**
     * Indicates the ability in this want can back to the current top ability even though they are not in the same
     * mission stack.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public static const ABILITY_BACK_TO_OTHER_MISSION_STACK: String = "ability.params.backToOtherMissionStack"
    /**
     * Indicates the param of ability failure restart recovery identification.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public static const ABILITY_RECOVERY_RESTART: String = "ohos.ability.params.abilityRecoveryRestart"
    /**
     * Indicates the param of extra content title.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public static const CONTENT_TITLE_KEY: String = "ohos.extra.param.key.contentTitle"
    /**
     * Indicates the param of extra shared abstract.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public static const SHARE_ABSTRACT_KEY: String = "ohos.extra.param.key.shareAbstract"
    /**
     * Indicates the param of extra shareURL.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public static const SHARE_URL_KEY: String = "ohos.extra.param.key.shareUrl"
    /**
     * Indicates the param of extra support continue page stack.
     * The default value of the param is true,
     * and the system will automatically flow the page stack information by default.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public static const SUPPORT_CONTINUE_PAGE_STACK_KEY: String = "ohos.extra.param.key.supportContinuePageStack"
    /**
     * Indicates the param of extra stop source ability on continue.
     * The default value of the param is true,
     * and the system will exit the source application by default.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public static const SUPPORT_CONTINUE_SOURCE_EXIT_KEY: String = "ohos.extra.param.key.supportContinueSourceExit"
}

/**
 * Used to indicate how Want is handled.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityBase"
]
public class Flags {
    init() {}
    /**
     * Indicates the grant to perform read operations on the URI.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public static const FLAG_AUTH_READ_URI_PERMISSION: UInt32 = 0x00000001
    /**
     * Indicates the grant to perform write operations on the URI.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public static const FLAG_AUTH_WRITE_URI_PERMISSION: UInt32 = 0x00000002
    /**
     * Indicates that the URI can be persisted by the callee.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public static const FLAG_AUTH_PERSISTABLE_URI_PERMISSION: UInt32 = 0x00000040
    /**
     * Install the specified ability if it's not installed.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public static const FLAG_INSTALL_ON_DEMAND: UInt32 = 0x00000800
    /**
     * Indicates that if implicit start ability couldn't match any application, no tip dialog will be pulled up.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public static const FLAG_START_WITHOUT_TIPS: UInt32 = 0x40000000
}
