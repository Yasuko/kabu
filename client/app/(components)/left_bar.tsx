import React from "react"
import Link from "next/link"
import {
    ChartBarIcon
} from '@heroicons/react/24/outline'

export default function LeftBar() {

    return (
    <>
            <div className="sticky top-0 inset-x-0 z-20 bg-white border-y px-4 sm:px-6 lg:px-8 lg:hidden dark:bg-neutral-800 dark:border-neutral-700">
            <div className="flex items-center py-2">

            <button
                type="button"
                className="
                    size-8 flex justify-center items-center gap-x-2
                    border border-gray-200 text-gray-800 hover:text-gray-500
                    rounded-lg focus:outline-none focus:text-gray-500 disabled:opacity-50
                    disabled:pointer-events-none dark:border-neutral-700
                    dark:text-neutral-200 dark:hover:text-neutral-500 dark:focus:text-neutral-500
                "
                aria-haspopup="dialog"
                aria-expanded="false"
                aria-controls="hs-application-sidebar"
                aria-label="Toggle navigation"
                data-hs-overlay="#hs-application-sidebar">
                <span className="sr-only">Toggle Navigation</span>
                <svg
                    className="shrink-0 size-4"
                    xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                    viewBox="0 0 24 24" fill="none"
                    stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <rect width="18" height="18" x="3" y="3" rx="2" />
                    <path d="M15 3v18" />
                    <path d="m8 9 3 3-3 3" />
                </svg>
            </button>

            <ol className="ms-3 flex items-center whitespace-nowrap">
                <li className="flex items-center text-sm text-gray-800 dark:text-neutral-400">
                KABU Nav
                <svg className="shrink-0 mx-3 overflow-visible size-2.5 text-gray-400 dark:text-neutral-500" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M5 1L10.6869 7.16086C10.8637 7.35239 10.8637 7.64761 10.6869 7.83914L5 14" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
                </svg>
                </li>
                <li className="text-sm font-semibold text-gray-800 truncate dark:text-neutral-400" aria-current="page">
                Dashboard
                </li>
            </ol>

            </div>
        </div>



        <div
            id="hs-application-sidebar"
            className="hs-overlay  [--auto-close:lg]
                hs-overlay-open:translate-x-0
                -translate-x-full transition-all duration-300 transform
                w-[260px] h-full
                hidden
                fixed inset-y-0 start-0 z-[60]
                bg-white border-e border-gray-200
                lg:block lg:translate-x-0 lg:end-auto lg:bottom-0
                dark:bg-neutral-800 dark:border-neutral-700"
            role="dialog"
            tabIndex={-1}
            aria-label="Sidebar">
            <div className="relative flex flex-col h-full max-h-full">
            <div className="px-6 pt-4">

                <a className="flex-none rounded-xl text-xl inline-block font-semibold focus:outline-none focus:opacity-80" href="#" aria-label="Preline">
                KABU
                </a>

            </div>


            <div className="h-full overflow-y-auto [&::-webkit-scrollbar]:w-2 [&::-webkit-scrollbar-thumb]:rounded-full [&::-webkit-scrollbar-track]:bg-gray-100 [&::-webkit-scrollbar-thumb]:bg-gray-300 dark:[&::-webkit-scrollbar-track]:bg-neutral-700 dark:[&::-webkit-scrollbar-thumb]:bg-neutral-500">
                <nav className="hs-accordion-group p-3 w-full flex flex-col flex-wrap" data-hs-accordion-always-open>
                <ul className="flex flex-col space-y-1">
                    <li>
                    <Link
                        className="
                            flex items-center gap-x-3.5 py-2 px-2.5 bg-gray-100
                            text-sm text-gray-800 rounded-lg hover:bg-gray-100
                            focus:outline-none focus:bg-gray-100 dark:bg-neutral-700 dark:text-white"
                        href="/">
                        <svg className="shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
                        <polyline points="9 22 9 12 15 12 15 22" />
                        </svg>
                        Dashboard
                    </Link>
                    </li>

                    <li className="hs-accordion" id="users-accordion">
                    <Link
                        className="
                            hs-accordion-toggle w-full text-start flex items-center gap-x-3.5 py-2 px-2.5
                            text-sm text-gray-800 rounded-lg hover:bg-gray-100 focus:outline-none
                            focus:bg-gray-100 dark:bg-neutral-800 dark:hover:bg-neutral-700
                            dark:text-neutral-200"
                        aria-expanded="true"
                        aria-controls="users-accordion-child"
                        href='/rank'>
                        <ChartBarIcon className="shrink-0 size-5" />
                        Rank

                        <svg className="hs-accordion-active:block ms-auto hidden size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <path d="m18 15-6-6-6 6" />
                        </svg>
                    </Link>
                    </li>

                    <li className="hs-accordion" id="account-accordion">
                    <Link
                        className="
                            hs-accordion-toggle w-full text-start flex items-center gap-x-3.5 py-2 px-2.5
                            text-sm text-gray-800 rounded-lg hover:bg-gray-100 focus:outline-none
                            focus:bg-gray-100 dark:bg-neutral-800 dark:hover:bg-neutral-700
                            dark:text-neutral-200
                        "
                        aria-expanded="true"
                        aria-controls="account-accordion-child"
                        href="/pressure">
                        <svg className="shrink-0 mt-0.5 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <circle cx="18" cy="15" r="3" />
                        <circle cx="9" cy="7" r="4" />
                        <path d="M10 15H6a4 4 0 0 0-4 4v2" />
                        <path d="m21.7 16.4-.9-.3" />
                        <path d="m15.2 13.9-.9-.3" />
                        <path d="m16.6 18.7.3-.9" />
                        <path d="m19.1 12.2.3-.9" />
                        <path d="m19.6 18.7-.4-1" />
                        <path d="m16.8 12.3-.4-1" />
                        <path d="m14.3 16.6 1-.4" />
                        <path d="m20.7 13.8 1-.4" />
                        </svg>
                        Pressure

                        <svg className="hs-accordion-active:block ms-auto hidden size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <path d="m18 15-6-6-6 6" />
                        </svg>

                    </Link>

                    </li>

                    <li className="hs-accordion" id="projects-accordion">
                    <Link
                        className="
                            hs-accordion-toggle w-full text-start flex items-center gap-x-3.5 py-2 px-2.5
                            text-sm text-gray-800 rounded-lg hover:bg-gray-100 focus:outline-none
                            focus:bg-gray-100 dark:bg-neutral-800 dark:hover:bg-neutral-700
                            dark:text-neutral-200
                            "
                        aria-expanded="true"
                        aria-controls="projects-accordion-child"
                        href="/vector">
                        <svg className="shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <rect width="20" height="14" x="2" y="7" rx="2" ry="2" />
                        <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16" />
                        </svg>
                        Vector

                        <svg className="hs-accordion-active:block ms-auto hidden size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <path d="m18 15-6-6-6 6" />
                        </svg>

                    </Link>

                    </li>

                    <li>
                        <Link
                            className="
                                w-full flex items-center gap-x-3.5 py-2 px-2.5 text-sm text-gray-800
                                rounded-lg hover:bg-gray-100 dark:hover:bg-neutral-700
                                dark:text-neutral-200 dark:hover:text-neutral-300"
                            href="/gold_cross">
                            <svg className="shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <rect width="18" height="18" x="3" y="4" rx="2" ry="2" />
                            <line x1="16" x2="16" y1="2" y2="6" />
                            <line x1="8" x2="8" y1="2" y2="6" />
                            <line x1="3" x2="21" y1="10" y2="10" />
                            <path d="M8 14h.01" />
                            <path d="M12 14h.01" />
                            <path d="M16 14h.01" />
                            <path d="M8 18h.01" />
                            <path d="M12 18h.01" />
                            <path d="M16 18h.01" />
                            </svg>
                            Gold Cross
                        </Link>
                    </li>
                    <li>
                        <Link
                            className="
                                w-full flex items-center gap-x-3.5 py-2 px-2.5 text-sm text-gray-800
                                rounded-lg hover:bg-gray-100 dark:hover:bg-neutral-900
                                dark:text-neutral-200 dark:hover:text-neutral-300"
                            href="simulate">
                            <svg className="shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />
                            <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />
                            </svg>
                            Simulate
                        </Link>
                    </li>
                </ul>
                </nav>
            </div>
            </div>
        </div>
    </>
    )
}