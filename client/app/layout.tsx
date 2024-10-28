'use client'
import React, { useEffect } from "react"
import "./globals.css"

import LeftBar from "./(components)/left_bar"
import PrelineScript from "./(components)/PrelineScript"

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {

  return (
  <html lang="ja" className="dark">
    <head>
      <meta charSet="utf-8" />
      <meta name="robots" content="max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
      <link rel="canonical" href="https://preline.co/" />
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
      <meta name="description" content="Comprehensive overview with charts, tables, and a streamlined dashboard layout for easy data visualization and analysis." />
    
      <title>KABU</title>
      <link rel="shortcut icon" href="../../favicon.ico" />
    </head>
      <body
        className='antialiased'
      >
        <LeftBar />
        {children}
        <PrelineScript />
      </body>
  </html>
  )
}
