'use client'
import React, { Suspense } from "react"
import Modal from "react-modal"
// import { IStaticMethods } from "preline/preline"

import List from "../(components)/list"
import CompanyInfo from "../(components)/company_info"

Modal.setAppElement('.App')

export type ModalContentType = {
    companyCode: string,
}

export default function Page() {
    const [modalIsOpen, setIsOpen] = React.useState(false)
    const [modalContent, setModalContent] = React.useState('')

    return (
        <>
        <main
            className="
                flex flex-col gap-8 row-start-2
                items-center sm:items-start
            ">
            <div className="justify-center border-b border-gray-200 dark:border-neutral-700">
                <nav className="-mb-0.5 flex justify-center gap-x-6" aria-label="Tabs" role="tablist" aria-orientation="horizontal">
                    <button
                        type="button"
                        className="
                            hs-tab-active:font-semibold hs-tab-active:border-blue-600
                            hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center
                            gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap
                            text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600
                            disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400
                            dark:hover:text-blue-500 active"
                        id="horizontal-alignment-item-1"
                        aria-selected="false"
                        data-hs-tab="#horizontal-alignment-1"
                        aria-controls="horizontal-alignment-1"
                        role="tab">
                    前日
                    </button>
                    <button
                        type="button"
                        className="
                            hs-tab-active:font-semibold hs-tab-active:border-blue-600
                            hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center
                            gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap
                            text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600
                            disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400
                            dark:hover:text-blue-500"
                        id="horizontal-alignment-item-2"
                        aria-selected="false"
                        data-hs-tab="#horizontal-alignment-2"
                        aria-controls="horizontal-alignment-2"
                        role="tab">
                    2日前
                    </button>
                    <button
                        type="button"
                        className="
                            hs-tab-active:font-semibold hs-tab-active:border-blue-600
                            hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center
                            gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap
                            text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600
                            disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400
                            dark:hover:text-blue-500"
                        id="horizontal-alignment-item-3"
                        aria-selected="false"
                        data-hs-tab="#horizontal-alignment-3"
                        aria-controls="horizontal-alignment-3"
                        role="tab">
                    3日前
                    </button>
                    <button
                        type="button"
                        className="
                            hs-tab-active:font-semibold hs-tab-active:border-blue-600
                            hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center
                            gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap
                            text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600
                            disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400
                            dark:hover:text-blue-500"
                        id="horizontal-alignment-item-4"
                        aria-selected="false"
                        data-hs-tab="#horizontal-alignment-4"
                        aria-controls="horizontal-alignment-4"
                        role="tab">
                    1週前
                    </button>
                    <button
                        type="button"
                        className="
                            hs-tab-active:font-semibold hs-tab-active:border-blue-600
                            hs-tab-active:text-blue-600 py-4 px-1 inline-flex items-center
                            gap-x-2 border-b-2 border-transparent text-sm whitespace-nowrap
                            text-gray-500 hover:text-blue-600 focus:outline-none focus:text-blue-600
                            disabled:opacity-50 disabled:pointer-events-none dark:text-neutral-400
                            dark:hover:text-blue-500"
                        id="horizontal-alignment-item-5"
                        aria-selected="false"
                        data-hs-tab="#horizontal-alignment-5"
                        aria-controls="horizontal-alignment-5"
                        role="tab">
                    2週前
                    </button>
                </nav>
            </div>
            <div className="mt-3">
                <div
                    id="horizontal-alignment-1"
                    role="tabpanel"
                    aria-labelledby="horizontal-alignment-item-1">
                    <p className="text-gray-500 dark:text-neutral-400">
                        前日との変動ランキング [上昇ランク、下降ランク]
                    </p>
                
                    <div className="flex gap-4 items-center flex-col sm:flex-row">
                        <Suspense fallback={<div>Loading...</div>}>
                        <div className="grid grid-cols-2 gap-1">
                            <div>
                                <List
                                    target={'dayone'}
                                    sort={'upper'}
                                    setModalOpen={setIsOpen}
                                    setModalOption={setModalContent} />
                            </div>
                            <div>
                                <List
                                    target={'dayone'}
                                    sort={'lower'}
                                    setModalOpen={setIsOpen}
                                    setModalOption={setModalContent} />
                            </div>
                        </div>
                        </Suspense>
                    </div>
                </div>
                <div
                    id="horizontal-alignment-2"
                    role="tabpanel"
                    className="hidden"
                    aria-labelledby="horizontal-alignment-item-2">
                    <p className="text-gray-500 dark:text-neutral-400">
                        2日前との変動ランキング [上昇ランク、下降ランク]
                    </p>
                    
                    <div className="flex gap-4 items-center flex-col sm:flex-row">
                        <Suspense fallback={<div>Loading...</div>}>
                        <div className="grid grid-cols-2 gap-1">
                            <div>
                                <List
                                    target={'daytwo'}
                                    sort={'upper'}
                                    setModalOpen={setIsOpen}
                                    setModalOption={setModalContent} />
                            </div>
                            <div>
                                <List
                                    target={'daytwo'}
                                    sort={'lower'}
                                    setModalOpen={setIsOpen}
                                    setModalOption={setModalContent} />
                            </div>
                        </div>
                        </Suspense>
                    </div>
                </div>
                <div
                    id="horizontal-alignment-3"
                    role="tabpanel"
                    className="hidden"
                    aria-labelledby="horizontal-alignment-item-3">
                    <p className="text-gray-500 dark:text-neutral-400">
                        3日前との変動ランキング [上昇ランク、下降ランク]
                    </p>
                    <div className="flex gap-4 items-center flex-col sm:flex-row">
                        <Suspense fallback={<div>Loading...</div>}>
                        <div className="grid grid-cols-2 gap-1">
                            <div>
                                <List
                                    target={'daythree'}
                                    sort={'upper'}
                                    setModalOpen={setIsOpen}
                                    setModalOption={setModalContent} />
                            </div>
                            <div>
                                <List
                                    target={'daythree'}
                                    sort={'lower'}
                                    setModalOpen={setIsOpen}
                                    setModalOption={setModalContent} />
                            </div>
                        </div>
                        </Suspense>
                    </div>
                </div>
                <div
                    id="horizontal-alignment-4"
                    role="tabpanel"
                    className="hidden"
                    aria-labelledby="horizontal-alignment-item-4">
                    <p className="text-gray-500 dark:text-neutral-400">
                        １週間前との変動ランキング [上昇ランク、下降ランク]
                    </p>
                    <div className="flex gap-4 items-center flex-col sm:flex-row">
                        <Suspense fallback={<div>Loading...</div>}>
                        <div className="grid grid-cols-2 gap-1">
                            <div>
                                <List
                                    target={'weekone'}
                                    sort={'upper'}
                                    setModalOpen={setIsOpen}
                                    setModalOption={setModalContent} />
                            </div>
                            <div>
                                <List
                                    target={'daythree'}
                                    sort={'lower'}
                                    setModalOpen={setIsOpen}
                                    setModalOption={setModalContent} />
                            </div>
                        </div>
                        </Suspense>
                    </div>
                </div>
                <div
                    id="horizontal-alignment-5"
                    role="tabpanel"
                    className="hidden"
                    aria-labelledby="horizontal-alignment-item-5">
                    <p className="text-gray-500 dark:text-neutral-400">
                        ２週間前との変動ランキング [上昇ランク、下降ランク]
                    </p>
                    <div className="flex gap-4 items-center flex-col sm:flex-row">
                        <Suspense fallback={<div>Loading...</div>}>
                        <div className="grid grid-cols-2 gap-1">
                            <div>
                                <List
                                    target={'weektwo'}
                                    sort={'upper'}
                                    setModalOpen={setIsOpen}
                                    setModalOption={setModalContent} />
                            </div>
                            <div>
                                <List
                                    target={'daythree'}
                                    sort={'lower'}
                                    setModalOpen={setIsOpen}
                                    setModalOption={setModalContent} />
                            </div>
                        </div>
                        </Suspense>
                    </div>
                </div>
            </div>
            <div className="App">
                <Modal isOpen={modalIsOpen} className="">
                    <CompanyInfo
                        companyCode={modalContent}
                    />
                    <button
                        type="button"
                        className="
                            absolute bottom-0 end-0 mt-2 mr-2
                            py-2 px-3 inline-flex items-center gap-x-2
                            text-sm font-medium
                            rounded-lg border border-gray-200 bg-white
                            text-gray-800 shadow-sm
                            hover:bg-gray-50 focus:outline-none focus:bg-gray-50
                            disabled:opacity-50 disabled:pointer-events-none
                            dark:bg-neutral-800 dark:border-neutral-700
                            dark:text-white dark:hover:bg-neutral-700
                            dark:focus:bg-neutral-700"
                        data-hs-overlay="#hs-full-screen-modal"
                        onClick={() => setIsOpen(false)}>
                    Close
                    </button>
                </Modal>
            </div>
    </main>
    </>
    )
}
