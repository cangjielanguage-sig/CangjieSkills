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

package ohos.application.test_runner

import std.collection.HashMap
import ohos.ffi.{FFIData, FFIDataManager}
import ohos.labels.{APILevel, Hide}
import ohos.ui_test.UITest
import ohos.business_exception.BusinessException

const ERROR_CODE_INNER: Int32 = 16000050

@C
struct CJTestRunnerFuncs {
    CJTestRunnerFuncs(
        let createTestRunner: CFunc<(CString) -> Int64>,
        let releaseTestRunner: CFunc<(Int64) -> Unit>,
        let testRunnerOnRun: CFunc<(Int64) -> Unit>,
        let testRunnerOnPrepare: CFunc<(Int64) -> Unit>
    ) {}
}

@C
func createTestRunner(name: CString): Int64 {
    let optTestRunner = TestRunner.create(name.toString())
    match (optTestRunner) {
        case None =>
            TEST_RUNNER_LOG.error("Failed to load TestRunner: " + name.toString())
            0
        case Some(testRunner) =>
            FFIDataManager.getInstance().register(testRunner)
            testRunner.getID()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func releaseTestRunner(id: Int64): Unit {
    let optTestRunner = FFIDataManager.getInstance().getData<TestRunner>(id)
    match (optTestRunner) {
        case None =>
            TEST_RUNNER_LOG.error("No such TestRunner: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(testRunner) => TEST_RUNNER_LOG.info("Release abilityContext end")
    }
    FFIDataManager.getInstance().releaseData(id)
    TEST_RUNNER_LOG.info("Release ability end")
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func testRunnerOnRun(id: Int64): Unit {
    let optTestRunner = FFIDataManager.getInstance().getData<TestRunner>(id)
    match (optTestRunner) {
        case None =>
            TEST_RUNNER_LOG.error("No such TestRunner: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(testRunner) => testRunner.onRun()
    }
}

/**
 * @throws { BusinessException } 16000050 - Internal error.
 */
@C
func testRunnerOnPrepare(id: Int64): Unit {
    let optTestRunner = FFIDataManager.getInstance().getData<TestRunner>(id)
    match (optTestRunner) {
        case None =>
            TEST_RUNNER_LOG.error("No such TestRunner: " + id.toString())
            throw BusinessException(ERROR_CODE_INNER, "Internal error.")
        case Some(testRunner) =>
            UITest.setup()
            testRunner.onPrepare()
    }
}

class TestRunnerImpl {}
/**
 * Base class for the test framework.
 * If you want to implement your own unit test framework, you must inherit this class and overrides all its methods.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public open class TestRunner <: FFIData {
    private static let CREATORS = HashMap<String, () -> TestRunner>()
    private let impl_: TestRunnerImpl = TestRunnerImpl()
    @!Hide
    protected init() {}
    /**
     * TestRunner register.
     *
     * @param { String } name - The module name of the TestRunner.
     * @param { () -> TestRunner } creator - The creator of the TestRunner.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public static func registerCreator(name: String, creator: () -> TestRunner): Unit {
        let optCreator = CREATORS.get(name)
        match (optCreator) {
            case None =>
                CREATORS.add(name, creator)
                TEST_RUNNER_LOG.info("Register creator of " + name + " successfully.")
            case Some(creatorFunc) => TEST_RUNNER_LOG.error(
                "Repeated registration for TestRunner in " + name + ", please check.")
        }
    }

    // protected function: available only for this package.
    static func create(name: String): Option<TestRunner> {
        let optCreator = CREATORS.get(name)
        match (optCreator) {
            case None =>
                TEST_RUNNER_LOG.error("No such create functions for Ability: " + name)
                Option<TestRunner>.None
            case Some(creator) => creator()
        }
    }

    /**
     * Prepare the unit testing environment for running test cases.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public open func onPrepare(): Unit {}

    /**
     * Run all test cases.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public open func onRun(): Unit {}
}

@C
func testRunnerCjFuncsRegister(result: CPointer<CJTestRunnerFuncs>): Unit {
    let atCFuncs = CJTestRunnerFuncs(
        createTestRunner,
        releaseTestRunner,
        testRunnerOnRun,
        testRunnerOnPrepare
    )
    unsafe { result.write(atCFuncs) }
}

foreign func RegisterCJTestRunnerFuncs(funcs: CFunc<(CPointer<CJTestRunnerFuncs>) -> Unit>): Unit

let REGISTER_TESTRUNNER = unsafe { RegisterCJTestRunnerFuncs(testRunnerCjFuncsRegister) }
